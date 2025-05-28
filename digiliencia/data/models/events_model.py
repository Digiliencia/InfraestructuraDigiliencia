from dataclasses import dataclass
from datetime import datetime
from digiliencia.data.models.interface_model import IModel

@dataclass(frozen=True)
class ScrapedEventsModel(IModel):
    """Represents an event scraped from the website."""

    type: str
    header: str
    location: str
    address: str
    description: str
    date: datetime
    url: str
    organizer: str
