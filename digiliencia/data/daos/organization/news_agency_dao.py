from typing import Any, List

from loguru import logger
from neo4j.graph import Node

from digiliencia.data.daos.organization.abc_organization_dao import OrganizationDAO
from digiliencia.data.db.access_mode_enum import AccessMode
from digiliencia.data.models.organization.news_agency_model import NewsAgencyModel
from digiliencia.exc.dao_create_exc import DAOCreateError
from digiliencia.exc.dao_read_exc import DAOReadError


class NewsAgencyDAO(OrganizationDAO[NewsAgencyModel]):
    """Data Access Object (DAO) for News Agencies."""

    _organization_type = "NewsAgency"

    def _build_model(self, raw_data: Any) -> NewsAgencyModel:
        """
        Builds a NewsAgencyModel from raw data.

        Args:
            raw_data (Any): Raw data retrieved from the database.

        Returns:
            NewsAgencyModel: A news agency model instance.
        """
        return NewsAgencyModel(
            id=raw_data.get("id"),
            name=raw_data.get("name"),
            description=raw_data.get("description"),
        )

    def create(  # type: ignore
        self, name: str, description: str, **kwargs
    ) -> NewsAgencyModel:
        """
        Creates a new news agency in the database.

        Args:
            name (str): The name of the news agency.
            description (str): A description of the news agency.
            **kwargs: Additional fields for news agencies.

        Returns:
            NewsAgencyModel: The created news agency model.

        Raises:
            DAOCreateError: If creation fails.
        """
        if not name:
            logger.error("Name is required to create a news agency")
            raise DAOCreateError("Name is required to create a news agency")
        try:
            query = """
                CREATE (o:Organization:NewsAgency {
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
                    logger.error("Failed to create news agency")
                    raise DAOCreateError("Failed to create news agency")

                org_node: Node = record["o"]
                logger.debug(f"Created news agency: {org_node}")
                return self._build_model(org_node)

        except Exception as e:
            logger.error(f"Error creating news agency: {e}")
            raise DAOCreateError("Failed to create news agency") from e

    def read_all(self) -> List[NewsAgencyModel]:
        """
        Reads all news agencies from the database.

        Returns:
            List[NewsAgencyModel]: A list of all news agency models.

        Raises:
            DAOReadError: If reading fails.
        """
        try:
            query = """
                MATCH (o:Organization:NewsAgency)
                RETURN o
            """
            with self.db.get_connection(AccessMode.READ) as session:
                result = session.run(query)
                agencies = [self._build_model(record["o"]) for record in result]
                logger.debug(f"Read {len(agencies)} news agencies")
                return agencies

        except Exception as e:
            logger.error(f"Error reading all news agencies: {e}")
            raise DAOReadError("Failed to read all news agencies") from e
