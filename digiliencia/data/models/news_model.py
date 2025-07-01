"""Pydantic models for data validation."""

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, HttpUrl


class ScrapedNews(BaseModel):
    """Pydantic model for scraped news data validation."""

    header: str
    date: datetime
    source: str
    content: str
    url: HttpUrl
    authors: List[str]
    topics: Optional[List[str]] = None

    model_config = ConfigDict(str_strip_whitespace=True, validate_assignment=True)
