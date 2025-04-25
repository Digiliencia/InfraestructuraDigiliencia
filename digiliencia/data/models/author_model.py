from dataclasses import dataclass
from typing import List

from digiliencia.data.models.person_model import PersonModel
from digiliencia.data.models.news_model import NewsModel


@dataclass(frozen=True)
class RawAuthorModel(PersonModel):
    """Represents an author in the database."""

    news_ids: List[str]


@dataclass(frozen=True)
class AuthorModel(PersonModel):
    """Represents an author"""

    news: List[NewsModel]
