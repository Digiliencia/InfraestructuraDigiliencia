from typing import Any, Optional, List

from loguru import logger

from digiliencia.data.daos.abc_dao import AbstractDAO
from digiliencia.exc.dao_create_exc import DAOCreateError
from digiliencia.exc.dao_read_exc import DAOReadError
from digiliencia.exc.dao_update_exc import DAOUpdateError
from digiliencia.exc.dao_delete_exc import DAODeleteError
from digiliencia.data.models.person_model import PersonModel
from digiliencia.data.db.access_mode_enum import AccessMode


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
            id=raw_data.id,
            full_name=raw_data.full_name,
            email=raw_data.email,
            decription=raw_data.description,
        )

    def create( 
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
                result = session.run(query, {
                    "full_name": full_name,
                    "email": email,
                    "description": description,
                })
                record = result.single()
                if record is None:
                    logger.error("Failed to create person")
                    raise DAOCreateError("Failed to create person")
                
                person_node = record["p"]
                logger.debug(f"Created person: {person_node}")
                return self._build_model(person_node)
            
        except Exception as e:
            logger.error(f"Error creating person: {e}")
            raise DAOCreateError("Failed to create person") from e
        
        # TODO: Test this method and add the rest of them.
        
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
        pass
        
    def read_all(self) -> List[PersonModel]:
        """
        Reads all persons from the database.
        
        Returns:
            List[PersonModel]: A list of all person models.
            
        Raises:
            DAOReadError: If reading fails.
        """
        pass
        
    def update(self, id: str, **kwargs) -> PersonModel:
        """
        Updates a person in the database.
        
        Args:
            id (str): The ID of the person to update.
            **kwargs: The fields to update.
            
        Returns:
            PersonModel: The updated person model.
            
        Raises:
            DAOUpdateError: If updating fails.
        """
        pass
        
    def delete(self, id: str) -> None:
        """
        Deletes a person from the database.
        
        Args:
            id (str): The ID of the person to delete.
            
        Raises:
            DAODeleteError: If deletion fails.
        """
        pass