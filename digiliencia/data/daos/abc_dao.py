from abc import ABC, abstractmethod
from typing import Any, Sequence

from digiliencia.data.models.interface_model import IModel
from digiliencia.data.db.db import Database


class AbstractDAO(ABC):
    """Abstract class for Data Access Object (DAO).

    This class defines the interface for DAOs, which handle the database operation for different models.
    """

    def __init__(self) -> None:
        """Initialize the DAO with a Database instance."""
        self.db = Database()

    @abstractmethod
    def _build_model(self, raw_data: Any) -> IModel:
        """
        Converts raw data form the database into a model instance.

        This method must be implemented by subclasses.

        Args:
            raw_data (Any): The raw data from the database.

        Returns:
            An instance of a model.
        """
        pass

    @abstractmethod
    def create(self, *args: Any, **kwargs: Any) -> None:
        """
        Creates a new record in the database.

        This method must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def read_by_id(self, id: int) -> IModel:
        """
        Reads a model instance by its ID.

        This method must be implemented by subclasses.

        Args:
            id (int): The ID of the record.

        Returns:
            The model instance corresponding to the record.
        """
        pass

    @abstractmethod
    def read_all(self) -> Sequence[IModel]:
        """
        Reads all model instances.

        This method must be implemented by subclasses.

        Returns:
            A sequence of all model instances.
        """
        pass

    @abstractmethod
    def update(self, id: int, *args: Any, **kwargs: Any) -> None:
        """
        Updates a record in the database.

        This method must be implemented by subclasses.

        Arguments:
            id: The ID of the record to update.
        """
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        """
        Deletes a record from the database.

        This method must be implemented by subclasses.

        Arguments:
            id: The ID of the record to delete.
        """
        pass
