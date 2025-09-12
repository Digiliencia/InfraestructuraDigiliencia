from typing import Generator

import pytest

from digiliencia.data.services.neomodel.author_service import AuthorService
from digiliencia.data.services.neomodel.config import configure_neomodel
from digiliencia.data.services.neomodel.field.field_service import FieldService
from digiliencia.data.services.neomodel.news_service import NewsService
from digiliencia.data.services.neomodel.topic.topic_service import TopicService


@pytest.fixture(scope="session")
def setup_neomodel() -> Generator[None, None, None]:
    """Setup neomodel for testing."""
    configure_neomodel()
    yield


@pytest.fixture
def news_service(setup_neomodel) -> NewsService:
    """Create a news service instance."""
    return NewsService()


@pytest.fixture
def topic_service(setup_neomodel) -> TopicService:
    """Create a topic service instance."""
    return TopicService()


@pytest.fixture
def field_service(setup_neomodel) -> FieldService:
    """Create a field service instance."""
    return FieldService()


@pytest.fixture
def author_service(setup_neomodel) -> AuthorService:
    """Create an author service instance."""
    return AuthorService()
