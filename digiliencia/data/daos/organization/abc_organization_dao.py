from abc import ABC, abstractmethod
from typing import Any, Generic, Sequence, TypeVar

from loguru import logger
from neo4j.graph import Node

from digiliencia.data.daos.abc_dao import AbstractDAO
from digiliencia.data.db.access_mode_enum import AccessMode
from digiliencia.data.models.organization.organization_model import OrganizationModel
from digiliencia.exc.dao_delete_exc import DAODeleteError
from digiliencia.exc.dao_read_exc import DAOReadError
from digiliencia.exc.dao_update_exc import DAOUpdateError

T = TypeVar("T", bound=OrganizationModel)


class OrganizationDAO(AbstractDAO, Generic[T], ABC):
    """
    Abstract Data Access Object (DAO) for Organizations.
    Cannot be instantiated directly - must use a concrete subclass.
    """

    # Class attribute to be overridden by subclasses
    _organization_type: str

    def __init__(self) -> None:
        super().__init__()
        # Ensure that it cannot be instantiated directly
        if self.__class__ == OrganizationDAO:
            raise TypeError(
                "OrganizationDAO is an abstract class and cannot be instantiated directly"
            )

        # Validate that the subclass has set _organization_type
        if not self._organization_type:
            raise ValueError(
                f"Subclass {self.__class__.__name__} must set _organization_type"
            )

    @abstractmethod
    def _build_model(self, raw_data: Any) -> T:
        """
        Builds a specific organization model from raw data.
        Must be implemented by subclasses.

        Args:
            raw_data (Any): Raw data retrieved from the database.

        Returns:
            T: A specific organization model instance.
        """
        pass

    @abstractmethod
    def create(self, name: str, description: str, **kwargs) -> T:  # type: ignore
        """
        Creates a new specific organization in the database.
        Must be implemented by subclasses.

        Args:
            name (str): The name of the organization.
            description (str): A description of the organization.
            **kwargs: Additional fields for specific organization types.

        Returns:
            T: The created organization model.

        Raises:
            DAOCreateError: If creation fails.
        """
        pass

    def read_by_id(self, id: str) -> T:
        """
        Reads a specific organization from the database by ID.

        Args:
            id (str): The ID of the organization to read.

        Returns:
            T: The specific organization model.

        Raises:
            DAOReadError: If reading fails.
        """
        try:
            # Construir la consulta con la etiqueta directamente en la cadena
            query = f"""
                MATCH (o:Organization:{self._organization_type} {{id: $id}})
                RETURN o
            """
            with self.db.get_connection(AccessMode.READ) as session:
                result = session.run(query, {"id": id})  # type: ignore
                record = result.single()
                if record is None:
                    logger.warning(f"No {self._organization_type} found with id: {id}")
                    raise DAOReadError(
                        f"No {self._organization_type} found with id: {id}"
                    )

                organization_node = record["o"]
                logger.debug(f"Read {self._organization_type}: {organization_node}")
                return self._build_model(organization_node)

        except Exception as e:
            logger.error(f"Error reading {self._organization_type} by id {id}: {e}")
            raise DAOReadError(
                f"Failed to read {self._organization_type} with id: {id}"
            ) from e

    def read_all(self) -> Sequence[T]:
        """
        Reads all specific organizations from the database.
        This method should be overridden by subclasses to return only
        their specific organization type.

        Returns:
            List[T]: A list of all specific organization models.

        Raises:
            DAOReadError: If reading fails.
        """
        raise NotImplementedError("read_all() should be implemented by subclasses")

    def update(self, id: str, **kwargs) -> T:  # type: ignore
        """
        Updates a specific organization in the database.

        Args:
            id (str): The ID of the organization to update.
            **kwargs: Fields to update (name, description)

        Returns:
            T: The updated organization model.

        Raises:
            DAOUpdateError: If updating fails.
        """
        try:
            update_items = []
            for key, value in kwargs.items():
                if value is not None:
                    update_items.append(f"o.{key} = ${key}")

            if not update_items:
                logger.warning("No valid fields to update")
                return self.read_by_id(id)

            query = f"""
                MATCH (o:Organization:{self._organization_type} {{id: $id}})
                SET {", ".join(update_items)}
                RETURN o
            """
            with self.db.get_connection(AccessMode.WRITE) as session:
                result = session.run(query, {"id": id, **kwargs})  # type: ignore
                record = result.single()
                if record is None:
                    logger.warning(f"No {self._organization_type} found with id: {id}")
                    raise DAOUpdateError(
                        f"No {self._organization_type} found with id: {id}"
                    )

                org_node: Node = record["o"]
                logger.debug(f"Updated {self._organization_type}: {org_node}")
                return self._build_model(org_node)

        except Exception as e:
            logger.error(f"Error updating {self._organization_type} with id {id}: {e}")
            raise DAOUpdateError(
                f"Failed to update {self._organization_type} with id: {id}"
            ) from e

    def delete(self, id: str) -> None:
        """
        Deletes a specific organization from the database.

        Args:
            id (str): The ID of the organization to delete.

        Raises:
            DAODeleteError: If deletion fails.
        """
        try:
            query = f"""
                MATCH (o:Organization:{self._organization_type} {{id: $id}})
                DELETE o
            """
            with self.db.get_connection(AccessMode.WRITE) as session:
                result = session.run(query, {"id": id})  # type: ignore
                summary = result.consume()
                if summary.counters.nodes_deleted == 0:
                    logger.warning(f"No {self._organization_type} found with id: {id}")
                    raise DAODeleteError(
                        f"No {self._organization_type} found with id: {id}"
                    )

                logger.debug(f"Deleted {self._organization_type} with id: {id}")

        except Exception as e:
            logger.error(f"Error deleting {self._organization_type} with id {id}: {e}")
            raise DAODeleteError(
                f"Failed to delete {self._organization_type} with id: {id}"
            ) from e
