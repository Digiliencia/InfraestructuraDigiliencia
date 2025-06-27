"""Updated tests using neomodel services instead of DAOs."""

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


class TestTopicService:
    """Test cases for TopicService - replacing TopicDAO tests."""

    def test_create_topic(self, topic_service: TopicService):
        """Test creating a topic."""
        topic = topic_service.create_topic("Test Topic", "Test definition")

        assert isinstance(topic, Topic)
        assert topic.name == "Test Topic"
        assert topic.definition == "Test definition"

    def test_create_duplicate_topic(self, topic_service: TopicService):
        """Test creating a duplicate topic returns existing one."""
        topic1 = topic_service.create_topic("Duplicate Topic", "First definition")
        topic2 = topic_service.create_topic("Duplicate Topic", "Second definition")

        # Should return the same topic (first one created)
        assert topic1.uid == topic2.uid
        assert topic1.definition == "First definition"  # Original definition preserved

    def test_get_topic_by_name(self, topic_service: TopicService):
        """Test retrieving topic by name."""
        created_topic = topic_service.create_topic("Searchable Topic", "Definition")
        retrieved_topic = topic_service.get_topic_by_name("Searchable Topic")

        assert retrieved_topic is not None
        assert retrieved_topic.uid == created_topic.uid
        assert retrieved_topic.name == created_topic.name

    def test_get_nonexistent_topic(self, topic_service: TopicService):
        """Test retrieving nonexistent topic."""
        topic = topic_service.get_topic_by_name("Nonexistent Topic")
        assert topic is None

    def test_get_all_topics(self, topic_service: TopicService):
        """Test retrieving all topics."""
        initial_count = len(topic_service.get_all_topics())

        topic_service.create_topic("Topic A", "Description A")
        topic_service.create_topic("Topic B", "Description B")

        all_topics = topic_service.get_all_topics()
        assert len(all_topics) >= initial_count + 2

        # Verify our topics are in the results
        topic_names = [topic.name for topic in all_topics]
        assert "Topic A" in topic_names
        assert "Topic B" in topic_names


class TestAuthorService:
    """Test cases for AuthorService - replacing AuthorDAO tests."""

    def test_create_author(self, author_service: AuthorService):
        """Test creating an author."""
        author = author_service.create_author(
            "Test Author", "test@example.com", "Test author description"
        )

        assert isinstance(author, Author)
        assert author.name == "Test Author"
        assert author.email == "test@example.com"
        assert author.description == "Test author description"

    def test_create_duplicate_author(self, author_service: AuthorService):
        """Test creating a duplicate author returns existing one."""
        author1 = author_service.create_author("Duplicate Author", "first@example.com")
        author2 = author_service.create_author("Duplicate Author", "second@example.com")

        # Should return the same author (first one created)
        assert author1.uid == author2.uid
        assert author1.email == "first@example.com"  # Original email preserved

    def test_create_author_minimal(self, author_service: AuthorService):
        """Test creating an author with minimal information."""
        author = author_service.create_author("Minimal Author")

        assert isinstance(author, Author)
        assert author.name == "Minimal Author"
        assert author.email == ""
        assert author.description == ""

    def test_get_author_by_name(self, author_service: AuthorService):
        """Test retrieving author by name."""
        created_author = author_service.create_author(
            "Searchable Author", "search@example.com"
        )
        retrieved_author = author_service.get_author_by_name("Searchable Author")

        assert retrieved_author is not None
        assert retrieved_author.uid == created_author.uid
        assert retrieved_author.name == created_author.name
        assert retrieved_author.email == created_author.email

    def test_get_all_authors(self, author_service: AuthorService):
        """Test retrieving all authors."""
        initial_count = len(author_service.get_all_authors())

        author_service.create_author("Author X", "x@example.com")
        author_service.create_author("Author Y", "y@example.com")

        all_authors = author_service.get_all_authors()
        assert len(all_authors) >= initial_count + 2

        # Verify our authors are in the results
        author_names = [author.name for author in all_authors]
        assert "Author X" in author_names
        assert "Author Y" in author_names


class TestNewsServiceExtended:
    """Extended test cases for NewsService - replacing NewsDAO tests."""

    def test_create_news_with_relationships(
        self,
        news_service: NewsService,
        topic_service: TopicService,
        author_service: AuthorService,
    ):
        """Test creating news with full relationships."""
        # Pre-create some topics
        topic_service.create_topic("Security", "Security topics")
        topic_service.create_topic("Privacy", "Privacy topics")

        news = news_service.create_news(
            header="Comprehensive Security News",
            date=datetime(2023, 6, 15, 14, 30),
            content="This is comprehensive security news content with multiple relationships.",
            url="https://example.com/comprehensive",
            source_name="Comprehensive News Agency",
            author_names=["Security Expert", "Privacy Specialist"],
            topic_names=["Security", "Privacy"],
        )

        assert isinstance(news, News)
        assert news.header == "Comprehensive Security News"
        assert (
            news.content
            == "This is comprehensive security news content with multiple relationships."
        )

        # Test agency relationship
        agency = news.published_by.single()
        assert agency is not None
        assert agency.name == "Comprehensive News Agency"

        # Test author relationships
        authors = news.written_by.all()
        assert len(authors) == 2
        author_names = [author.name for author in authors]
        assert "Security Expert" in author_names
        assert "Privacy Specialist" in author_names

        # Test topic relationships
        topics = news.covers.all()
        assert len(topics) == 2
        topic_names = [topic.name for topic in topics]
        assert "Security" in topic_names
        assert "Privacy" in topic_names

    def test_create_news_minimal(self, news_service: NewsService):
        """Test creating news with minimal information."""
        news = news_service.create_news(
            header="Minimal News",
            date=datetime(2023, 1, 1),
            content="Minimal content",
            url="https://example.com/minimal",
            source_name="Minimal Source",
        )

        assert isinstance(news, News)
        assert news.header == "Minimal News"

        # Should have agency relationship
        agency = news.published_by.single()
        assert agency is not None
        assert agency.name == "Minimal Source"

        # Should have no authors or topics
        assert len(news.written_by.all()) == 0
        assert len(news.covers.all()) == 0

    def test_create_duplicate_news(self, news_service: NewsService):
        """Test creating duplicate news (same header and date)."""
        date = datetime(2023, 3, 15, 10, 0)

        news1 = news_service.create_news(
            header="Duplicate News",
            date=date,
            content="First content",
            url="https://example.com/first",
            source_name="First Source",
        )

        news2 = news_service.create_news(
            header="Duplicate News",
            date=date,
            content="Second content",
            url="https://example.com/second",
            source_name="Second Source",
        )

        # Should return the same news (existing one)
        assert news1.uid == news2.uid
        assert news1.content == "First content"  # Original content preserved

    def test_create_from_scraped_data_comprehensive(
        self, news_service: NewsService, topic_service: TopicService
    ):
        """Test creating news from scraped data with comprehensive validation."""
        # Pre-create topics
        topic_service.create_topic("Cybersecurity", "Cybersecurity topics")
        topic_service.create_topic("AI Security", "AI Security topics")

        scraped_data = ScrapedNewsData(
            header="Comprehensive Scraped News",
            date=datetime(2023, 4, 20, 16, 45),
            source="Scraped News Agency",
            content="This is comprehensive scraped news content with validation.",
            url="https://example.com/scraped-comprehensive",
            authors=["Scraped Author 1", "Scraped Author 2"],
            topics=["Cybersecurity", "AI Security"],
        )

        news = news_service.create_from_scraped_data(scraped_data)

        assert isinstance(news, News)
        assert news.header == scraped_data.header
        assert news.content == scraped_data.content
        assert news.url == str(scraped_data.url)
        assert news.date == scraped_data.date

        # Verify relationships
        agency = news.published_by.single()
        assert agency.name == scraped_data.source

        authors = news.written_by.all()
        assert len(authors) == 2
        author_names = [author.name for author in authors]
        assert "Scraped Author 1" in author_names
        assert "Scraped Author 2" in author_names

        topics = news.covers.all()
        assert len(topics) == 2
        topic_names = [topic.name for topic in topics]
        assert "Cybersecurity" in topic_names
        assert "AI Security" in topic_names

    def test_news_crud_operations(self, news_service: NewsService):
        """Test full CRUD operations on news."""
        # Create
        news = news_service.create_news(
            header="CRUD Test News",
            date=datetime(2023, 5, 10),
            content="Original content",
            url="https://example.com/crud",
            source_name="CRUD Source",
        )

        original_uid = news.uid

        # Read
        retrieved_news = news_service.get_news_by_id(original_uid)
        assert retrieved_news is not None
        assert retrieved_news.uid == original_uid
        assert retrieved_news.header == "CRUD Test News"

        # Update
        updated_news = news_service.update_news(
            original_uid, header="Updated CRUD Test News", content="Updated content"
        )
        assert updated_news is not None
        assert updated_news.header == "Updated CRUD Test News"
        assert updated_news.content == "Updated content"
        assert updated_news.url == "https://example.com/crud"  # Unchanged

        # Verify update persisted
        retrieved_again = news_service.get_news_by_id(original_uid)
        assert retrieved_again is not None
        assert retrieved_again.header == "Updated CRUD Test News"

        # Delete
        delete_result = news_service.delete_news(original_uid)
        assert delete_result is True

        # Verify deletion
        deleted_news = news_service.get_news_by_id(original_uid)
        assert deleted_news is None

        # Try to delete again (should return False)
        delete_again = news_service.delete_news(original_uid)
        assert delete_again is False
