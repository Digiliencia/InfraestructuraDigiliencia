from typing import Any, List, Optional

from loguru import logger
from neo4j.exceptions import ConstraintError
from neo4j.graph import Node

from digiliencia.data.daos.abc_dao import AbstractDAO
from digiliencia.data.db.access_mode_enum import AccessMode
from digiliencia.data.models.person_model import PersonModel
from digiliencia.exc.dao_create_exc import DAOCreateError
from digiliencia.exc.dao_delete_exc import DAODeleteError
from digiliencia.exc.dao_read_exc import DAOReadError
from digiliencia.exc.dao_update_exc import DAOUpdateError


class PersonDAO(AbstractDAO):
    """Data Access Object (DAO) for Persons."""

    def __init__(self) -> None:
        super().__init__()

    def _build_model(self, raw_data: Any) -> PersonModel:
        """
        Builds a PersonModel from raw data.

        Args:
            raw_data (Any): Raw data retrieved from the database.

        Returns:
            PersonModel: A person model instance.
        """
        return PersonModel(
            id=raw_data.get("id"),
            full_name=raw_data.get("full_name"),
            email=raw_data.get("email"),
            description=raw_data.get("description"),
        )

    def create(  # type: ignore
        self,
        full_name: str,
        email: Optional[str],
        description: Optional[str],
    ) -> PersonModel:
        """
        Creates a new person in the database.

        Args:
            full_name (str): The full name of the person.
            email (str): The email address of the person.
            description (str): A description of the person.
        """
        try:
            query = """
                CREATE (p:Person {
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
                    logger.error("Failed to create person")
                    raise DAOCreateError("Failed to create person")

                person_node: Node = record["p"]
                print(type(person_node))
                logger.debug(f"Created person: {person_node}")
                return self._build_model(person_node)

        except ConstraintError as e:
            logger.error(f"Constraint error creating person: {e}")
            raise DAOCreateError("Failed to create person due to constraint") from e

    def read_by_id(self, id: str) -> PersonModel:
        """
        Reads a person from the database by ID.

        Args:
            id (str): The ID of the person to read.

        Returns:
            PersonModel: The person model.

        Raises:
            DAOReadError: If reading fails.
        """
        try:
            query = """
                MATCH (p:Person {id: $id})
                RETURN p
            """
            with self.db.get_connection(AccessMode.READ) as session:
                result = session.run(query, {"id": id})
                record = result.single()
                if record is None:
                    logger.warning(f"No person found with id: {id}")
                    raise DAOReadError(f"No person found with id: {id}")

                person_node: Node = record["p"]
                logger.debug(f"Read person by id: {person_node}")
                return self._build_model(person_node)

        except Exception as e:
            logger.error(f"Error reading person by id {id}: {e}")
            raise DAOReadError(f"Failed to read person with id: {id}") from e

    def read_all(self) -> List[PersonModel]:
        """
        Reads all persons from the database.

        Returns:
            List[PersonModel]: A list of all person models.

        Raises:
            DAOReadError: If reading fails.
        """
        try:
            query = """
                MATCH (p:Person)
                RETURN p
            """
            with self.db.get_connection(AccessMode.READ) as session:
                result = session.run(query)
                persons = [self._build_model(record["p"]) for record in result]
                logger.debug(f"Read {len(persons)} persons")
                return persons

        except Exception as e:
            logger.error(f"Error reading all persons: {e}")
            raise DAOReadError("Failed to read all persons") from e

    def update(self, id: str, **kwargs) -> PersonModel:  # type: ignore
        """
        Updates a person in the database.

        Args:
            id (str): The ID of the person to update.
            full_name (str): The new full name of the person.
            email (str): The new email address of the person.
            description (str): The new description of the person.

        Returns:
            PersonModel: The updated person model.

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
                MATCH (p:Person {{id: $id}})
                SET {", ".join(update_items)}
                RETURN p
            """
            with self.db.get_connection(AccessMode.WRITE) as session:
                result = session.run(query, {"id": id, **kwargs})
                record = result.single()
                if record is None:
                    logger.warning(f"No person found with id: {id}")
                    raise DAOUpdateError(f"No person found with id: {id}")

                person_node: Node = record["p"]
                logger.debug(f"Updated person: {person_node}")
                return self._build_model(person_node)

        except Exception as e:
            logger.error(f"Error updating person with id {id}: {e}")
            raise DAOUpdateError(f"Failed to update person with id: {id}") from e

    def delete(self, id: str) -> None:
        """
        Deletes a person from the database.

        Args:
            id (str): The ID of the person to delete.

        Raises:
            DAODeleteError: If deletion fails.
        """
        try:
            query = """
                MATCH (p:Person {id: $id})
                DELETE p
            """
            with self.db.get_connection(AccessMode.WRITE) as session:
                result = session.run(query, {"id": id})
                if result.consume().counters.nodes_deleted == 0:
                    logger.warning(f"No person found with id: {id}")
                    raise DAODeleteError(f"No person found with id: {id}")
                logger.debug(f"Deleted person with id: {id}")

        except Exception as e:
            logger.error(f"Error deleting person with id {id}: {e}")
            raise DAODeleteError(f"Failed to delete person with id: {id}") from e
