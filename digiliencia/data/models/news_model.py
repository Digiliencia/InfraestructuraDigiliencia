from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class ScrapedNewsModel:
    """Represents a news scraped from the web."""

    header: str
    date: datetime
    source: str
    content: str
    url: str
    authors: list[str]
    topics: Optional[list[str]]
