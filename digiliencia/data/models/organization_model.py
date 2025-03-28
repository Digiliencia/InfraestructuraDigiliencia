from dataclasses import dataclass
from digiliencia.data.models.interface_model import IModel


@dataclass(frozen=True)
class OrganizationModel(IModel):
    """Represents an organization in the database."""

    id: int
    name: str
    description: str


@dataclass(frozen=True)
class NewsAgencyModel(OrganizationModel):
    """Represents a news agency in the database with models instead of IDs for its references."""

    pass


@dataclass(frozen=True)
class PublicOrganizationModel(OrganizationModel):
    """Represents a public organization in the database with models instead of IDs for its references."""

    pass
