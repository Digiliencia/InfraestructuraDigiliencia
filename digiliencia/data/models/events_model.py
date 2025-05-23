from dataclasses import dataclass
from datetime import datetime
from digiliencia.data.models.interface_model import IModel
from digiliencia.data.models.organization.organization_model import OrganizationModel

@dataclass(frozen=True)
class ScrapedEventsModel(IModel):
    """Represents an event scraped from the website."""

    header: str
    localitation: str
    address: str
    description: str
    date: datetime
    url: str
    organization: OrganizationModel
