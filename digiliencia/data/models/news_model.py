from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from digiliencia.data.models.interface_model import IModel
from digiliencia.data.models.organization.news_agency_model import NewsAgencyModel
from digiliencia.data.models.topic_model import TopicModel
from digiliencia.data.models.person_model import PersonModel


@dataclass(frozen=True)
class RawNewsModel(IModel):
    """Represents a news in the database."""

    id: str
    header: str
    date: datetime
    source_id: str
    content: str
    url: str
    author_ids: list[str]
    topic_ids: list[str]


@dataclass(frozen=True)
class NewsModel(IModel):
    """Represents a product in the database with models instead of IDs for its references."""

    id: str
    header: str
    date: datetime
    source: NewsAgencyModel
    content: str
    url: str
    authors: list[PersonModel]
    topics: list[TopicModel]


@dataclass(frozen=True)
class ScrapedNewsModel(IModel):
    """Represents a news scraped from the web."""

    header: str
    date: datetime
    source: str
    content: str
    url: str
    authors: list[str]
    topics: Optional[list[str]]
