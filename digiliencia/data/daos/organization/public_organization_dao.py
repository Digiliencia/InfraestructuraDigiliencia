from typing import Any, List

from loguru import logger
from neo4j.graph import Node

from digiliencia.data.daos.organization.abc_organization_dao import OrganizationDAO
from digiliencia.data.db.access_mode_enum import AccessMode
from digiliencia.data.models.organization.public_organization_model import (
    PublicOrganizationModel,
)
from digiliencia.exc.dao_create_exc import DAOCreateError
from digiliencia.exc.dao_read_exc import DAOReadError


class PublicOrganizationDAO(OrganizationDAO[PublicOrganizationModel]):
    """Data Access Object (DAO) for Public Organizations."""

    _organization_type = "PublicOrganization"

    def _build_model(self, raw_data: Any) -> PublicOrganizationModel:
        """
        Builds a PublicOrganizationModel from raw data.

        Args:
            raw_data (Any): Raw data retrieved from the database.

        Returns:
            PublicOrganizationModel: A public organization model instance.
        """
        return PublicOrganizationModel(
            id=raw_data.get("id"),
            name=raw_data.get("name"),
            description=raw_data.get("description"),
        )

    def create(  # type: ignore
        self, name: str, description: str, **kwargs
    ) -> PublicOrganizationModel:
        """
        Creates a new public organization in the database.

        Args:
            name (str): The name of the public organization.
            description (str): A description of the public organization.
            **kwargs: Additional fields for public organizations.

        Returns:
            PublicOrganizationModel: The created public organization model.

        Raises:
            DAOCreateError: If creation fails.
        """
        if not name:
            logger.error("Name is required to create a public organization")
            raise DAOCreateError("Name is required to create a public organization")
        try:
            query = """
                CREATE (o:Organization:PublicOrganization {
                    id: randomUUID(),
                    name: $name,
                    description: $description
                })
                RETURN o
            """
            with self.db.get_connection(AccessMode.WRITE) as session:
                result = session.run(
                    query,
                    {"name": name, "description": description, **kwargs},
                )
                record = result.single()
                if record is None:
                    logger.error("Failed to create public organization")
                    raise DAOCreateError("Failed to create public organization")

                org_node: Node = record["o"]
                logger.debug(f"Created public organization: {org_node}")
                return self._build_model(org_node)

        except Exception as e:
            logger.error(f"Error creating public organization: {e}")
            raise DAOCreateError("Failed to create public organization") from e

    def read_all(self) -> List[PublicOrganizationModel]:
        """
        Reads all public organizations from the database.

        Returns:
            List[PublicOrganizationModel]: A list of all public organization models.

        Raises:
            DAOReadError: If reading fails.
        """
        try:
            query = """
                MATCH (o:Organization:PublicOrganization)
                RETURN o
            """
            with self.db.get_connection(AccessMode.READ) as session:
                result = session.run(query)
                public_orgs = [self._build_model(record["o"]) for record in result]
                logger.debug(f"Read {len(public_orgs)} public organizations")
                return public_orgs

        except Exception as e:
            logger.error(f"Error reading all public organizations: {e}")
            raise DAOReadError("Failed to read all public organizations") from e
