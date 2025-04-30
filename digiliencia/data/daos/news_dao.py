from datetime import datetime
from typing import Any, Optional, Sequence

from loguru import logger
from neo4j.exceptions import ConstraintError
from neo4j.graph import Node

from digiliencia.data.daos.abc_dao import AbstractDAO
from digiliencia.data.daos.organization.news_agency_dao import NewsAgencyDAO
from digiliencia.data.daos.person.author_dao import AuthorDAO
from digiliencia.data.db.access_mode_enum import AccessMode
from digiliencia.data.models.news_model import RawNewsModel, ScrapedNewsModel
from digiliencia.exc.dao_create_exc import DAOCreateError
from digiliencia.exc.dao_delete_exc import DAODeleteError
from digiliencia.exc.dao_read_exc import DAOReadError
from digiliencia.exc.dao_update_exc import DAOUpdateError


class NewsDAO(AbstractDAO):
    """Data Access Object (DAO) for News."""

    def __init__(self) -> None:
        super().__init__()

    def _build_model(self, raw_data: Any) -> RawNewsModel:
        """
        Builds a RawNewsModel from raw data.

        Args:
            raw_data (Any): Raw data retrieved from the database.

        Returns:
            RawNewsModel: A news model instance.
        """
        # Convert date string to datetime if necessary
        date = raw_data.get("date")
        if isinstance(date, str):
            date = datetime.fromisoformat(date)

        return RawNewsModel(
            id=raw_data.get("id"),
            header=raw_data.get("header"),
            date=date,
            source_id=raw_data.get("source_id"),
            content=raw_data.get("content"),
            url=raw_data.get("url"),
            author_ids=raw_data.get("author_ids", []),
            topic_ids=raw_data.get("topic_ids", []),
        )

    def create_from_scrap(self, news: ScrapedNewsModel) -> RawNewsModel:
        """
        Creates a new news item in the database and establishes relationships.

        Args:
            news (ScrapedNewsModel): The news item to create.

        Returns:
            RawNewsModel: The created news model.

        Raises:
            DAOCreateError: If creation fails.
        """
        try:
            # Query to find source, authors, and topics by name in a single database call
            lookup_query = """
                // Get source ID
                MATCH (s:Organization {name: $source_name})
                WITH s
                
                // Get author IDs
                OPTIONAL MATCH (a:Author)
                WHERE a.name IN $author_names
                WITH s, collect({name: a.name, id: a.id}) as authors
                
                // Get topic IDs
                OPTIONAL MATCH (t:Topic)
                WHERE t.name IN $topic_names
                WITH s, authors, collect({name: t.name, id: t.id}) as topics
                
                RETURN s.id as source_id, authors, topics
            """

            author_names = news.authors or []
            topic_names = news.topics or []

            with self.db.get_connection(AccessMode.READ) as session:
                lookup_result = session.run(
                    lookup_query,
                    {
                        "source_name": news.source,
                        "author_names": author_names,
                        "topic_names": topic_names,
                    },
                )
                lookup_record = lookup_result.single()
                if lookup_record is None or lookup_record["source_id"] is None:
                    logger.warning(f"No source found with name: {news.source}")
                    news_agency_dao = NewsAgencyDAO()
                    createdAgency = news_agency_dao.create(
                        name=news.source, description=""
                    )
                    source_id = createdAgency.id
                else:
                    source_id = lookup_record["source_id"]

                # Process author IDs
                author_ids = []
                author_map = {}
                if lookup_record is not None and lookup_record["authors"] is not None:
                    author_map = {a["name"]: a["id"] for a in lookup_record["authors"]}  # type: ignore
                for author_name in author_names:
                    if author_name in author_map:
                        author_ids.append(author_map[author_name])
                    else:
                        logger.warning(f"Author not found: {author_name}.")
                        person_dao = AuthorDAO()
                        createdAuthor = person_dao.create(name=author_name)
                        author_ids.append(createdAuthor.id)

                # Process topic IDs
                topic_ids = []
                topic_map = {}
                if lookup_record is not None and lookup_record["topics"] is not None:
                    topic_map = {t["name"]: t["id"] for t in lookup_record["topics"]}  # type: ignore
                for topic_name in topic_names:
                    if topic_name in topic_map:
                        topic_ids.append(topic_map[topic_name])
                    else:
                        logger.warning(f"Topic not found: {topic_name}, skipping")
                        # TODO: Consider creating a new topic if not found?

            # Call the existing create method with IDs
            return self.create(
                header=news.header,
                date=news.date,
                source_id=source_id,
                content=news.content,
                url=news.url,
                author_ids=author_ids,
                topic_ids=topic_ids,
            )

        except Exception as e:
            logger.error(f"Error creating news from ScrapedNewsModel: {e}")
            raise DAOCreateError(f"Failed to create news: {str(e)}") from e

    def create(  # type: ignore
        self,
        header: str,
        date: datetime,
        source_id: str,
        content: str,
        url: str,
        author_ids: Optional[Sequence[str]] = None,
        topic_ids: Optional[Sequence[str]] = None,
    ) -> RawNewsModel:
        """
        Creates a new news item in the database and establishes relationships.

        Args:
            header (str): The headline of the news.
            date (datetime): The publication date of the news.
            source_id (str): The ID of the news agency source.
            content (str): The content/body of the news.
            url (str): The original URL of the news.
            author_ids (List[str]): List of author IDs associated with the news.
            topic_ids (List[str]): List of topic IDs associated with the news.

        Returns:
            RawNewsModel: The created news model.

        Raises:
            DAOCreateError: If creation fails.
        """
        try:
            author_ids = author_ids or []
            topic_ids = topic_ids or []

            # Crear el nodo de noticia
            news_data = self._create_news_node(header, date, content, url)
            news_id = news_data["id"]

            # Crear todas las relaciones necesarias
            self._create_news_relationships(news_id, source_id, author_ids, topic_ids)

            # Enriquecer los datos para el modelo
            news_data["source_id"] = source_id
            news_data["author_ids"] = author_ids
            news_data["topic_ids"] = topic_ids

            logger.debug(f"Created news: {news_data['header']}")
            return self._build_model(news_data)

        except ConstraintError as e:
            logger.error(f"Constraint error creating news: {e}")
            raise DAOCreateError("Failed to create news due to constraint") from e
        except Exception as e:
            logger.error(f"Error creating news: {e}")
            raise DAOCreateError(f"Failed to create news: {str(e)}") from e

    def _create_news_node(
        self, header: str, date: datetime, content: str, url: str
    ) -> dict:
        """Crea un nodo de noticia en la base de datos y devuelve sus datos."""
        create_query = """
            CREATE (n:News {
                id: randomUUID(),
                header: $header,
                date: $date,
                content: $content,
                url: $url
            })
            RETURN n
        """

        with self.db.get_connection(AccessMode.WRITE) as session:
            result = session.run(
                create_query,
                {
                    "header": header,
                    "date": date.isoformat(),
                    "content": content,
                    "url": url,
                },
            )

            record = result.single()
            if record is None:
                logger.error("Failed to create news node")
                raise DAOCreateError("Failed to create news node")

            return dict(record["n"])

    def _create_news_relationships(
        self,
        news_id: str,
        source_id: str,
        author_ids: Sequence[str],
        topic_ids: Sequence[str],
    ) -> None:
        """Crea todas las relaciones para una noticia."""
        with self.db.get_connection(AccessMode.WRITE) as session:
            try:
                # Relación con la fuente (NewsAgency)
                self._create_source_relationship(session, news_id, source_id)

                # Relaciones con autores
                if author_ids:
                    self._create_author_relationships(session, news_id, author_ids)

                # Relaciones con temas
                if topic_ids:
                    self._create_topic_relationships(session, news_id, topic_ids)

            except Exception as relation_error:
                logger.warning(
                    f"Error creating relationships for news {news_id}: {relation_error}"
                )
                # Continuar aunque haya errores en las relaciones

    def _create_source_relationship(
        self, session, news_id: str, source_id: str
    ) -> None:
        """Crea la relación entre una noticia y su fuente."""
        source_query = """
            MATCH (n:News {id: $news_id})
            MATCH (na:NewsAgency {id: $source_id})
            MERGE (n)-[:PUBLISHED_BY]->(na)
        """
        session.run(source_query, {"news_id": news_id, "source_id": source_id})

    def _create_author_relationships(
        self, session, news_id: str, author_ids: Sequence[str]
    ) -> None:
        """Crea las relaciones entre una noticia y sus autores."""
        author_query = """
            MATCH (n:News {id: $news_id})
            UNWIND $author_ids AS author_id
            MATCH (a:Person {id: author_id})
            MERGE (n)-[:WRITTEN_BY]->(a)
        """
        session.run(author_query, {"news_id": news_id, "author_ids": author_ids})

    def _create_topic_relationships(
        self, session, news_id: str, topic_ids: Sequence[str]
    ) -> None:
        """Crea las relaciones entre una noticia y sus temas."""
        topic_query = """
            MATCH (n:News {id: $news_id})
            UNWIND $topic_ids AS topic_id
            MATCH (t:Topic {id: topic_id})
            MERGE (n)-[:BELONGS_TO]->(t)
        """
        session.run(topic_query, {"news_id": news_id, "topic_ids": topic_ids})

    def read_by_id(self, id: str) -> RawNewsModel:
        """
        Reads a news item from the database by ID.

        Args:
            id (str): The ID of the news to read.

        Returns:
            RawNewsModel: The news model.

        Raises:
            DAOReadError: If reading fails.
        """
        try:
            query = """
                MATCH (n:News {id: $id})
                RETURN n
            """
            with self.db.get_connection(AccessMode.READ) as session:
                result = session.run(query, {"id": id})
                record = result.single()
                if record is None:
                    logger.warning(f"No news found with id: {id}")
                    raise DAOReadError(f"No news found with id: {id}")

                news_node: Node = record["n"]
                logger.debug(f"Read news by id: {news_node}")
                return self._build_model(news_node)

        except Exception as e:
            logger.error(f"Error reading news by id {id}: {e}")
            raise DAOReadError(f"Failed to read news with id: {id}") from e

    def read_all(self) -> Sequence[RawNewsModel]:
        """
        Reads all news items from the database.

        Returns:
            List[RawNewsModel]: A list of all news models.

        Raises:
            DAOReadError: If reading fails.
        """
        try:
            query = """
                MATCH (n:News)
                RETURN n
            """
            with self.db.get_connection(AccessMode.READ) as session:
                result = session.run(query)
                news_items = [self._build_model(record["n"]) for record in result]
                logger.debug(f"Read {len(news_items)} news items")
                return news_items

        except Exception as e:
            logger.error(f"Error reading all news: {e}")
            raise DAOReadError("Failed to read all news") from e

    def read_by_source(self, source_id: str) -> Sequence[RawNewsModel]:
        """
        Reads news items from a specific source.

        Args:
            source_id (str): The ID of the news source.

        Returns:
            List[RawNewsModel]: A list of news from the specified source.

        Raises:
            DAOReadError: If reading fails.
        """
        try:
            query = """
                MATCH (n:News)
                WHERE n.source_id = $source_id
                RETURN n
            """
            with self.db.get_connection(AccessMode.READ) as session:
                result = session.run(query, {"source_id": source_id})
                news_items = [self._build_model(record["n"]) for record in result]
                logger.debug(
                    f"Read {len(news_items)} news items from source {source_id}"
                )
                return news_items

        except Exception as e:
            logger.error(f"Error reading news by source {source_id}: {e}")
            raise DAOReadError(f"Failed to read news with source: {source_id}") from e

    def read_by_topic(
        self,
        topic_id: str,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        limit: int = 100,
    ) -> Sequence[RawNewsModel]:
        """
        Reads news items related to a specific topic with optional date range filtering.
        """
        try:
            base_query = """
                MATCH (n:News)-[:BELONGS_TO]->(t:Topic {id: $topic_id})
                RETURN n
                LIMIT $limit
            """

            query, params = self._build_date_filter_query(
                base_query, {"topic_id": topic_id, "limit": limit}, start_date, end_date
            )

            return self._execute_read_query(query, params, f"topic {topic_id}")

        except Exception as e:
            logger.error(f"Error reading news by topic {topic_id}: {e}")
            raise DAOReadError(f"Failed to read news with topic: {topic_id}") from e

    def read_by_organization(
        self,
        news_agency_id: str,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        limit: int = 100,
    ) -> Sequence[RawNewsModel]:
        """
        Reads news items published by a specific news agency with optional date range filtering.

        Args:
            news_agency_id (str): The ID of the news agency.
            start_date (Optional[datetime]): Filter news published on or after this date.
            end_date (Optional[datetime]): Filter news published on or before this date.
            limit (int): Maximum number of news items to return (default 100).

        Returns:
            List[RawNewsModel]: A list of news published by the specified news agency.

        Raises:
            DAOReadError: If reading fails.
        """
        try:
            query = """
                MATCH (n:News), (na:NewsAgency)
                WHERE (n)-[:PUBLISHED_BY]->(na:NewsAgency {id: $news_agency_id})
                RETURN n
                ORDER BY n.date DESC
                LIMIT $limit
            """
            query_params = {"news_agency_id": news_agency_id, "limit": limit}
            query, query_params = self._build_date_filter_query(
                query, query_params, start_date, end_date
            )

            with self.db.get_connection(AccessMode.READ) as session:
                result = session.run(query, query_params)  # type: ignore
                news_items = [self._build_model(record["n"]) for record in result]
                logger.debug(
                    f"Read {len(news_items)} news items from news agency {news_agency_id}"
                )
                return news_items

        except Exception as e:
            logger.error(f"Error reading news by news agency {news_agency_id}: {e}")
            raise DAOReadError(
                f"Failed to read news from news agency: {news_agency_id}"
            ) from e

    def read_by_date_range(
        self, start_date: datetime, end_date: datetime
    ) -> Sequence[RawNewsModel]:
        """
        Reads news items published within a date range.

        Args:
            start_date (datetime): The start date of the range.
            end_date (datetime): The end date of the range.

        Returns:
            List[RawNewsModel]: A list of news published within the specified date range.

        Raises:
            DAOReadError: If reading fails.
        """
        try:
            query = """
                MATCH (n:News)
                WHERE n.date >= $start_date AND n.date <= $end_date
                RETURN n
            """
            with self.db.get_connection(AccessMode.READ) as session:
                result = session.run(
                    query,
                    {
                        "start_date": start_date.isoformat(),
                        "end_date": end_date.isoformat(),
                    },
                )
                news_items = [self._build_model(record["n"]) for record in result]
                logger.debug(
                    f"Read {len(news_items)} news items between {start_date} and {end_date}"
                )
                return news_items

        except Exception as e:
            logger.error(f"Error reading news by date range: {e}")
            raise DAOReadError("Failed to read news within date range") from e

    def update(self, id: str, **kwargs) -> RawNewsModel:  # type: ignore
        """
        Updates a news item in the database.

        Args:
            id (str): The ID of the news to update.
            header (str): The new headline of the news.
            date (datetime): The new publication date of the news.
            source_id (str): The new ID of the news agency source.
            content (str): The new content/body of the news.
            url (str): The new original URL of the news.
            author_ids (List[str]): The new list of author IDs associated with the news.
            topic_ids (List[str]): The new list of topic IDs associated with the news.

        Returns:
            RawNewsModel: The updated news model.

        Raises:
            DAOUpdateError: If updating fails.
        """
        try:
            # Extract author_ids and topic_ids for relationship management
            author_ids = kwargs.pop("author_ids", None)
            topic_ids = kwargs.pop("topic_ids", None)

            # Handle date conversion if present
            if "date" in kwargs and isinstance(kwargs["date"], datetime):
                kwargs["date"] = kwargs["date"].isoformat()

            # First update node properties
            update_items = []
            for key, value in kwargs.items():
                if value is not None:
                    update_items.append(f"n.{key} = ${key}")

            with self.db.get_connection(AccessMode.WRITE) as session:
                # Update node properties if there are properties to update
                if update_items:
                    query = f"""
                        MATCH (n:News {{id: $id}})
                        SET {", ".join(update_items)}
                        RETURN n
                    """
                    result = session.run(query, {"id": id, **kwargs})
                    record = result.single()
                    if record is None:
                        logger.warning(f"No news found with id: {id}")
                        raise DAOUpdateError(f"No news found with id: {id}")

                # Update author relationships if specified
                if author_ids is not None:
                    author_query = """
                        MATCH (n:News {id: $id})
                        // Delete all existing author relationships
                        OPTIONAL MATCH (n)-[r:WRITTEN_BY]->(a:Author)
                        DELETE r
                        // Create new relationships
                        WITH n, $author_ids AS author_ids
                        UNWIND author_ids AS author_id
                        MATCH (a:Author {id: author_id})
                        MERGE (n)-[:WRITTEN_BY]->(a)
                        RETURN n
                    """
                    session.run(author_query, {"id": id, "author_ids": author_ids})
                    logger.debug(f"Updated author relationships for news {id}")

                # Update topic relationships if specified
                if topic_ids is not None:
                    topic_query = """
                        MATCH (n:News {id: $id})
                        // Delete all existing topic relationships
                        OPTIONAL MATCH (n)-[r:BELONGS_TO]->(t:Topic)
                        DELETE r
                        // Create new relationships
                        WITH n, $topic_ids AS topic_ids
                        UNWIND topic_ids AS topic_id
                        MATCH (t:Topic {id: topic_id})
                        MERGE (n)-[:BELONGS_TO]->(t)
                        RETURN n
                    """
                    session.run(topic_query, {"id": id, "topic_ids": topic_ids})
                    logger.debug(f"Updated topic relationships for news {id}")

            # Return updated news item
            return self.read_by_id(id)

        except Exception as e:
            logger.error(f"Error updating news with id {id}: {e}")
            raise DAOUpdateError(f"Failed to update news with id: {id}") from e

    def delete(self, id: str) -> None:
        """
        Deletes a news item from the database.

        Args:
            id (str): The ID of the news to delete.

        Raises:
            DAODeleteError: If deletion fails.
        """
        try:
            query = """
                MATCH (n:News {id: $id})
                DETACH DELETE n
            """
            with self.db.get_connection(AccessMode.WRITE) as session:
                result = session.run(query, {"id": id})
                if result.consume().counters.nodes_deleted == 0:
                    logger.warning(f"No news found with id: {id}")
                    raise DAODeleteError(f"No news found with id: {id}")
                logger.debug(f"Deleted news with id: {id}")

        except Exception as e:
            logger.error(f"Error deleting news with id {id}: {e}")
            raise DAODeleteError(f"Failed to delete news with id: {id}") from e

    def _build_date_filter_query(
        self,
        base_query: str,
        params: dict,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
    ) -> tuple:
        """
        Construye una consulta con filtros de fecha y sus parámetros.

        Returns:
            tuple: (query_string, parameters_dict)
        """
        conditions = []
        query_params = params.copy()

        if start_date:
            query_params["start_date"] = start_date.isoformat()
            conditions.append("n.date >= $start_date")

        if end_date:
            query_params["end_date"] = end_date.isoformat()
            conditions.append("n.date <= $end_date")

        if conditions:
            if "WHERE" in base_query:
                # Ya existe una cláusula WHERE, añadir con AND
                query = base_query.replace(
                    "WHERE", f"WHERE {' AND '.join(conditions)} AND"
                )
            else:
                # No hay cláusula WHERE, añadirla
                query = base_query.replace(
                    "RETURN", f"WHERE {' AND '.join(conditions)}\nRETURN"
                )
        else:
            query = base_query

        return query, query_params

    def _execute_read_query(
        self, query: str, params: dict, context: str = ""
    ) -> Sequence[RawNewsModel]:
        """Ejecuta una consulta de lectura y devuelve los resultados como modelos."""
        with self.db.get_connection(AccessMode.READ) as session:
            result = session.run(query, params)
            news_items = [self._build_model(record["n"]) for record in result]
            logger.debug(
                f"Read {len(news_items)} news items"
                + (f" with {context}" if context else "")
            )
            return news_items
