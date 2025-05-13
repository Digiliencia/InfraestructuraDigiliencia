from typing import Any, Sequence

from loguru import logger
from neo4j.exceptions import ConstraintError
from neo4j.graph import Node

from digiliencia.data.daos.abc_dao import AbstractDAO
from digiliencia.data.db.access_mode_enum import AccessMode
from digiliencia.data.models.topic_model import TopicModel
from digiliencia.exc.dao_create_exc import DAOCreateError
from digiliencia.exc.dao_delete_exc import DAODeleteError
from digiliencia.exc.dao_read_exc import DAOReadError
from digiliencia.exc.dao_update_exc import DAOUpdateError


class TopicDAO(AbstractDAO):
    """Data Access Object (DAO) for Topics."""

    def __init__(self) -> None:
        super().__init__()

    def _build_model(self, raw_data: Any) -> TopicModel:
        """
        Builds a TopicModel from raw data.

        Args:
            raw_data (Any): Raw data retrieved from the database.

        Returns:
            TopicModel: A topic model instance.
        """
        return TopicModel(
            id=raw_data.get("id"),
            name=raw_data.get("name"),
            definition=raw_data.get("definition"),
        )

    def create(  # type: ignore
        self,
        name: str,
        definition: str,
    ) -> TopicModel:
        """
        Creates a new topic in the database.

        Args:
            name (str): The name of the topic.
            definition (str): The definition of the topic.

        Returns:
            TopicModel: The created topic model.

        Raises:
            DAOCreateError: If creation fails.
        """
        try:
            query = """
                CREATE (t:Topic {
                    id: randomUUID(),
                    name: $name,
                    definition: $definition
                })
                RETURN t
            """
            with self.db.get_connection(AccessMode.WRITE) as session:
                result = session.run(
                    query,
                    {
                        "name": name,
                        "definition": definition,
                    },
                )
                record = result.single()
                if record is None:
                    logger.error("Failed to create topic")
                    raise DAOCreateError("Failed to create topic")

                topic_node: Node = record["t"]
                logger.debug(f"Created topic: {topic_node}")
                return self._build_model(topic_node)

        except ConstraintError as e:
            logger.error(f"Constraint error creating topic: {e}")
            raise DAOCreateError("Failed to create topic due to constraint") from e

    def read_by_id(self, id: str) -> TopicModel:
        """
        Reads a topic from the database by ID.

        Args:
            id (str): The ID of the topic to read.

        Returns:
            TopicModel: The topic model.

        Raises:
            DAOReadError: If reading fails.
        """
        try:
            query = """
                MATCH (t:Topic {id: $id})
                RETURN t
            """
            with self.db.get_connection(AccessMode.READ) as session:
                result = session.run(query, {"id": id})
                record = result.single()
                if record is None:
                    logger.warning(f"No topic found with id: {id}")
                    raise DAOReadError(f"No topic found with id: {id}")

                topic_node: Node = record["t"]
                logger.debug(f"Read topic by id: {topic_node}")
                return self._build_model(topic_node)

        except Exception as e:
            logger.error(f"Error reading topic by id {id}: {e}")
            raise DAOReadError(f"Failed to read topic with id: {id}") from e

    def read_all(self) -> Sequence[TopicModel]:
        """
        Reads all topics from the database.

        Returns:
            List[TopicModel]: A list of all topic models.

        Raises:
            DAOReadError: If reading fails.
        """
        try:
            query = """
                MATCH (t:Topic)
                RETURN t
            """
            with self.db.get_connection(AccessMode.READ) as session:
                result = session.run(query)
                topics = [self._build_model(record["t"]) for record in result]
                logger.debug(f"Read {len(topics)} topics")
                return topics

        except Exception as e:
            logger.error(f"Error reading all topics: {e}")
            raise DAOReadError("Failed to read all topics") from e

    def update(self, id: str, **kwargs) -> TopicModel:  # type: ignore
        """
        Updates a topic in the database.

        Args:
            id (str): The ID of the topic to update.
            name (str, optional): The new name of the topic.
            definition (str, optional): The new definition of the topic.

        Returns:
            TopicModel: The updated topic model.

        Raises:
            DAOUpdateError: If updating fails.
        """
        try:
            update_items = []
            for key, value in kwargs.items():
                if value is not None:
                    update_items.append(f"t.{key} = ${key}")

            if not update_items:
                logger.warning("No valid fields to update")
                return self.read_by_id(id)

            query = f"""
                MATCH (t:Topic {{id: $id}})
                SET {", ".join(update_items)}
                RETURN t
            """
            with self.db.get_connection(AccessMode.WRITE) as session:
                result = session.run(query, {"id": id, **kwargs})
                record = result.single()
                if record is None:
                    logger.warning(f"No topic found with id: {id}")
                    raise DAOUpdateError(f"No topic found with id: {id}")

                topic_node: Node = record["t"]
                logger.debug(f"Updated topic: {topic_node}")
                return self._build_model(topic_node)

        except Exception as e:
            logger.error(f"Error updating topic with id {id}: {e}")
            raise DAOUpdateError(f"Failed to update topic with id: {id}") from e

    def delete(self, id: str) -> None:
        """
        Deletes a topic from the database.

        Args:
            id (str): The ID of the topic to delete.

        Raises:
            DAODeleteError: If deletion fails.
        """
        try:
            query = """
                MATCH (t:Topic {id: $id})
                DELETE t
            """
            with self.db.get_connection(AccessMode.WRITE) as session:
                result = session.run(query, {"id": id})
                if result.consume().counters.nodes_deleted == 0:
                    logger.warning(f"No topic found with id: {id}")
                    raise DAODeleteError(f"No topic found with id: {id}")
                logger.debug(f"Deleted topic with id: {id}")

        except Exception as e:
            logger.error(f"Error deleting topic with id {id}: {e}")
            raise DAODeleteError(f"Failed to delete topic with id: {id}") from e

    def read_by_name(self, name: str) -> TopicModel:
        """
        Reads a topic from the database by name.

        Args:
            name (str): The name of the topic to read.

        Returns:
            TopicModel: The topic model.

        Raises:
            DAOReadError: If reading fails.
        """
        try:
            query = """
                MATCH (t:Topic {name: $name})
                RETURN t
            """
            with self.db.get_connection(AccessMode.READ) as session:
                result = session.run(query, {"name": name})
                record = result.single()
                if record is None:
                    logger.warning(f"No topic found with name: {name}")
                    raise DAOReadError(f"No topic found with name: {name}")

                topic_node: Node = record["t"]
                logger.debug(f"Read topic by name: {topic_node}")
                return self._build_model(topic_node)

        except Exception as e:
            logger.error(f"Error reading topic by name {name}: {e}")
            raise DAOReadError(f"Failed to read topic with name: {name}") from e