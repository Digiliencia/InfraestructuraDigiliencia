from dataclasses import dataclass

from digiliencia.data.models.organization.organization_model import OrganizationModel


@dataclass(frozen=True)
class PublicOrganizationModel(OrganizationModel):
    """Represents a public organization in the database with models instead of IDs for its references."""

    pass
