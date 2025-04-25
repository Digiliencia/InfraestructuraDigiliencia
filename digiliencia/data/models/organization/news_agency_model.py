from dataclasses import dataclass

from digiliencia.data.models.organization.organization_model import OrganizationModel


@dataclass(frozen=True)
class NewsAgencyModel(OrganizationModel):
    """Represents a news agency in the database with models instead of IDs for its references."""

    pass
