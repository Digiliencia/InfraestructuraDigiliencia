from typing import Any, Optional, Sequence

from loguru import logger
from neo4j.exceptions import ConstraintError
from neo4j.graph import Node

from digiliencia.data.daos.abc_dao import AbstractDAO
from digiliencia.data.db.access_mode_enum import AccessMode
from digiliencia.data.models.author_model import RawAuthorModel
from digiliencia.exc.dao_create_exc import DAOCreateError
from digiliencia.exc.dao_delete_exc import DAODeleteError
from digiliencia.exc.dao_read_exc import DAOReadError
from digiliencia.exc.dao_update_exc import DAOUpdateError


class AuthorDAO(AbstractDAO):
    """Data Access Object (DAO) for Authors."""

    def __init__(self) -> None:
        super().__init__()

    def _build_model(self, raw_data: Any) -> RawAuthorModel:
        """
        Builds an AuthorModel from raw data.

        Args:
            raw_data (Any): Raw data retrieved from the database.

        Returns:
            AuthorModel: An author model instance.
        """
        return RawAuthorModel(
            id=raw_data.get("id"),
            full_name=raw_data.get("full_name"),
            email=raw_data.get("email"),
            description=raw_data.get("description"),
            news_ids=raw_data.get("news", []),
        )

    def create(  # type: ignore
        self,
        full_name: str,
        email: Optional[str] = None,
        description: Optional[str] = None,
    ) -> RawAuthorModel:
        """
        Creates a new author in the database.

        Args:
            full_name (str): The full name of the author.
            email (Optional[str]): The email address of the author.
            description (Optional[str]): A description of the author.

        Returns:
            AuthorModel: The created author model.

        Raises:
            DAOCreateError: If creation fails.
        """
        try:
            query = """
                CREATE (p:Person:Author {
                    id: randomUUID(),
                    full_name: $full_name,
                    email: $email,
                    description: $description
                })
                RETURN p
            """
            with self.db.get_connection(AccessMode.WRITE) as session:
                result = session.run(
                    query,
                    {
                        "full_name": full_name,
                        "email": email,
                        "description": description,
                    },
                )
                record = result.single()
                if record is None:
                    logger.error("Failed to create author")
                    raise DAOCreateError("Failed to create author")

                author_node: Node = record["p"]
                logger.debug(f"Created author: {author_node}")

                # Al crear un nuevo autor, inicialmente no tiene noticias asociadas
                author_data = dict(author_node)
                author_data["news"] = []

                return self._build_model(author_data)

        except ConstraintError as e:
            logger.error(f"Constraint error creating author: {e}")
            raise DAOCreateError("Failed to create author due to constraint") from e

    def read_by_id(self, id: str) -> RawAuthorModel:
        """
        Reads an author from the database by ID.

        Args:
            id (str): The ID of the author to read.

        Returns:
            AuthorModel: The author model.

        Raises:
            DAOReadError: If reading fails.
        """
        try:
            query = """
                MATCH (a:Author {id: $id})
                OPTIONAL MATCH (n:News)-[:WRITTEN_BY]->(a)
                RETURN a as p, collect(n.id) as news
            """
            with self.db.get_connection(AccessMode.READ) as session:
                result = session.run(query, {"id": id})
                record = result.single()
                if record is None:
                    logger.warning(f"No author found with id: {id}")
                    raise DAOReadError(f"No author found with id: {id}")

                author_node: Node = record["p"]
                news_ids = record["news"]

                # Combinar los datos del autor con la lista de IDs de noticias
                author_data = dict(author_node)
                author_data["news"] = news_ids

                logger.debug(
                    f"Read author by id: {author_node} with {len(news_ids)} news"
                )
                return self._build_model(author_data)

        except Exception as e:
            logger.error(f"Error reading author by id {id}: {e}")
            raise DAOReadError(f"Failed to read author with id: {id}") from e

    def read_all(self) -> Sequence[RawAuthorModel]:
        """
        Reads all authors from the database.

        Returns:
            Sequence[AuthorModel]: A sequence of all author models.

        Raises:
            DAOReadError: If reading fails.
        """
        try:
            query = """
                MATCH (a:Author)
                OPTIONAL MATCH (n:News)-[:WRITTEN_BY]->(a)
                RETURN a as p, collect(n.id) as news
            """
            with self.db.get_connection(AccessMode.READ) as session:
                result = session.run(query)
                authors = []
                for record in result:
                    author_node = record["p"]
                    news_ids = record["news"]

                    # Combinar los datos del autor con la lista de IDs de noticias
                    author_data = dict(author_node)
                    author_data["news"] = news_ids

                    authors.append(self._build_model(author_data))

                logger.debug(f"Read {len(authors)} authors")
                return authors

        except Exception as e:
            logger.error(f"Error reading all authors: {e}")
            raise DAOReadError("Failed to read all authors") from e

    def update(self, id: str, **kwargs) -> RawAuthorModel:  # type: ignore
        """
        Updates an author in the database.

        Args:
            id (str): The ID of the author to update.
            full_name (str): The new full name of the author.
            email (str): The new email address of the author.
            description (str): The new description of the author.

        Returns:
            AuthorModel: The updated author model.

        Raises:
            DAOUpdateError: If updating fails.
        """
        try:
            update_items = []
            for key, value in kwargs.items():
                if value is not None:
                    update_items.append(f"p.{key} = ${key}")

            if not update_items:
                logger.warning("No valid fields to update")
                return self.read_by_id(id)

            query = f"""
                MATCH (p:Author {{id: $id}})
                SET {", ".join(update_items)}
                RETURN p
            """
            with self.db.get_connection(AccessMode.WRITE) as session:
                result = session.run(query, {"id": id, **kwargs})
                record = result.single()
                if record is None:
                    logger.warning(f"No author found with id: {id}")
                    raise DAOUpdateError(f"No author found with id: {id}")

                author_node: Node = record["p"]
                logger.debug(f"Updated author: {author_node}")

                # Después de actualizar, leer el autor completo con sus noticias
                return self.read_by_id(id)

        except Exception as e:
            logger.error(f"Error updating author with id {id}: {e}")
            raise DAOUpdateError(f"Failed to update author with id: {id}") from e

    def delete(self, id: str) -> None:
        """
        Deletes an author from the database.

        Args:
            id (str): The ID of the author to delete.

        Raises:
            DAODeleteError: If deletion fails.
        """
        try:
            query = """
                MATCH (p:Author {id: $id})
                DELETE p
            """
            with self.db.get_connection(AccessMode.WRITE) as session:
                result = session.run(query, {"id": id})
                if result.consume().counters.nodes_deleted == 0:
                    logger.warning(f"No author found with id: {id}")
                    raise DAODeleteError(f"No author found with id: {id}")
                logger.debug(f"Deleted author with id: {id}")

        except Exception as e:
            logger.error(f"Error deleting author with id {id}: {e}")
            raise DAODeleteError(f"Failed to delete author with id: {id}") from e
