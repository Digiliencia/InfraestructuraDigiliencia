"""Tests for neomodel-based news service."""

from datetime import datetime
from typing import Generator

import pytest

from digiliencia.data.neomodel_manager import (
    Author,
    AuthorService,
    News,
    NewsService,
    ScrapedNewsData,
    Topic,
    TopicService,
    configure_neomodel,
)


@pytest.fixture(scope="session")
def setup_neomodel() -> Generator[None, None, None]:
    """Setup neomodel for testing."""
    configure_neomodel()
    yield
    # Cleanup will be handled by conftest.py database cleanup


@pytest.fixture
def news_service(setup_neomodel) -> NewsService:
    """Create a news service instance."""
    return NewsService()


@pytest.fixture
def topic_service(setup_neomodel) -> TopicService:
    """Create a topic service instance."""
    return TopicService()


@pytest.fixture
def author_service(setup_neomodel) -> AuthorService:
    """Create an author service instance."""
    return AuthorService()


@pytest.fixture
def sample_scraped_data() -> ScrapedNewsData:
    """Sample scraped news data for testing."""
    return ScrapedNewsData(
        header="Test Cybersecurity News",
        date=datetime(2023, 1, 1, 12, 0),
        source="Test News Agency",
        content="This is test cybersecurity news content.",
        url="https://example.com/test-news",
        authors=["John Doe", "Jane Smith"],
        topics=["Cybersecurity", "AI Security"],
    )


class TestNewsService:
    """Test cases for NewsService."""

    def test_create_from_scraped_data(
        self, news_service: NewsService, sample_scraped_data: ScrapedNewsData
    ):
        """Test creating news from scraped data."""
        news = news_service.create_from_scraped_data(sample_scraped_data)

        assert isinstance(news, News)
        assert news.header == sample_scraped_data.header
        assert news.content == sample_scraped_data.content
        assert news.url == str(sample_scraped_data.url)
        assert news.date == sample_scraped_data.date

    def test_create_news_direct(self, news_service: NewsService):
        """Test creating news directly."""
        news = news_service.create_news(
            header="Direct Test News",
            date=datetime(2023, 2, 1, 10, 0),
            content="Direct test content",
            url="https://example.com/direct",
            source_name="Direct Source",
        )

        assert isinstance(news, News)
        assert news.header == "Direct Test News"

    def test_get_news_by_id(
        self, news_service: NewsService, sample_scraped_data: ScrapedNewsData
    ):
        """Test retrieving news by ID."""
        created_news = news_service.create_from_scraped_data(sample_scraped_data)
        retrieved_news = news_service.get_news_by_id(created_news.uid)

        assert retrieved_news is not None
        assert retrieved_news.uid == created_news.uid
        assert retrieved_news.header == created_news.header

    def test_get_news_by_nonexistent_id(self, news_service: NewsService):
        """Test retrieving news with nonexistent ID."""
        news = news_service.get_news_by_id("nonexistent-id")
        assert news is None

    def test_update_news(
        self, news_service: NewsService, sample_scraped_data: ScrapedNewsData
    ):
        """Test updating news."""
        created_news = news_service.create_from_scraped_data(sample_scraped_data)

        updated_news = news_service.update_news(
            created_news.uid, header="Updated Header", content="Updated content"
        )

        assert updated_news is not None
        assert updated_news.header == "Updated Header"
        assert updated_news.content == "Updated content"
        assert updated_news.url == created_news.url  # Unchanged

    def test_delete_news(
        self, news_service: NewsService, sample_scraped_data: ScrapedNewsData
    ):
        """Test deleting news."""
        created_news = news_service.create_from_scraped_data(sample_scraped_data)

        # Delete the news
        result = news_service.delete_news(created_news.uid)
        assert result is True

        # Verify it's deleted
        retrieved_news = news_service.get_news_by_id(created_news.uid)
        assert retrieved_news is None

    def test_get_all_news(self, news_service: NewsService):
        """Test retrieving all news."""
        initial_count = len(news_service.get_all_news())

        # Create some news
        news_service.create_news(
            header="Test News 1",
            date=datetime(2023, 1, 1),
            content="Content 1",
            url="https://example.com/1",
            source_name="Source 1",
        )
        news_service.create_news(
            header="Test News 2",
            date=datetime(2023, 1, 2),
            content="Content 2",
            url="https://example.com/2",
            source_name="Source 2",
        )

        all_news = news_service.get_all_news()
        assert len(all_news) >= initial_count + 2


class TestTopicService:
    """Test cases for TopicService."""

    def test_create_topic(self, topic_service: TopicService):
        """Test creating a topic."""
        topic = topic_service.create_topic(
            "Artificial Intelligence", "AI-related topics"
        )

        assert isinstance(topic, Topic)
        assert topic.name == "Artificial Intelligence"
        assert topic.definition == "AI-related topics"

    def test_get_topic_by_name(self, topic_service: TopicService):
        """Test retrieving topic by name."""
        created_topic = topic_service.create_topic("Machine Learning", "ML topics")
        retrieved_topic = topic_service.get_topic_by_name("Machine Learning")

        assert retrieved_topic is not None
        assert retrieved_topic.name == created_topic.name

    def test_get_nonexistent_topic(self, topic_service: TopicService):
        """Test retrieving nonexistent topic."""
        topic = topic_service.get_topic_by_name("Nonexistent Topic")
        assert topic is None

    def test_get_all_topics(self, topic_service: TopicService):
        """Test retrieving all topics."""
        initial_count = len(topic_service.get_all_topics())

        topic_service.create_topic("Topic 1", "Description 1")
        topic_service.create_topic("Topic 2", "Description 2")

        all_topics = topic_service.get_all_topics()
        assert len(all_topics) >= initial_count + 2


class TestAuthorService:
    """Test cases for AuthorService."""

    def test_create_author(self, author_service: AuthorService):
        """Test creating an author."""
        author = author_service.create_author(
            "Test Author", "test@example.com", "Test author description"
        )

        assert isinstance(author, Author)
        assert author.name == "Test Author"
        assert author.email == "test@example.com"
        assert author.description == "Test author description"

    def test_get_author_by_name(self, author_service: AuthorService):
        """Test retrieving author by name."""
        created_author = author_service.create_author("Jane Doe", "jane@example.com")
        retrieved_author = author_service.get_author_by_name("Jane Doe")

        assert retrieved_author is not None
        assert retrieved_author.name == created_author.name
        assert retrieved_author.email == created_author.email

    def test_get_nonexistent_author(self, author_service: AuthorService):
        """Test retrieving nonexistent author."""
        author = author_service.get_author_by_name("Nonexistent Author")
        assert author is None

    def test_get_all_authors(self, author_service: AuthorService):
        """Test retrieving all authors."""
        initial_count = len(author_service.get_all_authors())

        author_service.create_author("Author 1", "author1@example.com")
        author_service.create_author("Author 2", "author2@example.com")

        all_authors = author_service.get_all_authors()
        assert len(all_authors) >= initial_count + 2


class TestIntegration:
    """Integration tests for news, topics, and authors."""

    def test_news_with_relationships(
        self,
        news_service: NewsService,
        topic_service: TopicService,
        author_service: AuthorService,
    ):
        """Test creating news with topics and authors."""
        # Create some topics first
        topic_service.create_topic("Cybersecurity", "Security-related topics")
        topic_service.create_topic("Privacy", "Privacy-related topics")

        # Create news with existing topics
        news = news_service.create_news(
            header="Integration Test News",
            date=datetime(2023, 3, 1),
            content="Integration test content",
            url="https://example.com/integration",
            source_name="Integration Source",
            author_names=["Alice Johnson", "Bob Wilson"],
            topic_names=["Cybersecurity", "Privacy"],
        )

        assert isinstance(news, News)
        assert news.header == "Integration Test News"

        # Verify relationships exist
        connected_agency = news.published_by.single()
        assert connected_agency is not None
        assert connected_agency.name == "Integration Source"

        connected_authors = news.written_by.all()
        assert len(connected_authors) == 2
        author_names = [author.name for author in connected_authors]
        assert "Alice Johnson" in author_names
        assert "Bob Wilson" in author_names

        connected_topics = news.covers.all()
        assert len(connected_topics) == 2
        topic_names = [topic.name for topic in connected_topics]
        assert "Cybersecurity" in topic_names
        assert "Privacy" in topic_names
