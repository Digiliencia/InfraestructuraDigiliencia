from dataclasses import dataclass
from datetime import datetime

from pydantic import BaseModel


@dataclass(frozen=True)
class ScrapedEventsModel(BaseModel):
    """Represents an event scraped from the website."""

    type: str
    header: str
    location: str
    address: str
    description: str
    date: datetime
    url: str
    organizer: str
