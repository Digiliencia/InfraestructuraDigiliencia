from datetime import datetime

import pytest
from pydantic import HttpUrl

from digiliencia.data.models.neomodel.news import News
from digiliencia.data.schemas import ScrapedNewsData
from digiliencia.data.services.neomodel.author_service import AuthorService
from digiliencia.data.services.neomodel.news_service import NewsService
from digiliencia.data.services.neomodel.topic_service import TopicService


@pytest.fixture
def sample_scraped_data() -> ScrapedNewsData:
    """Sample scraped news data for testing."""
    return ScrapedNewsData(
        header="Test Cybersecurity News",
        date=datetime(2023, 1, 1, 12, 0),
        source="Test News Agency",
        content="This is test cybersecurity news content.",
        url=HttpUrl("https://example.com/test-news"),
        authors=["John Doe", "Jane Smith"],
        topics=["Cybersecurity", "AI Security"],
    )


def test_create_from_scraped_data(
    news_service: NewsService, sample_scraped_data: ScrapedNewsData
):
    """Test creating news from scraped data."""
    news = news_service.create_from_scraped_data(sample_scraped_data)

    assert isinstance(news, News)
    assert news.header == sample_scraped_data.header
    assert news.content == sample_scraped_data.content
    assert news.url == str(sample_scraped_data.url)
    assert news.date == sample_scraped_data.date


def test_create_news_direct(news_service: NewsService):
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
    news_service: NewsService, sample_scraped_data: ScrapedNewsData
):
    """Test retrieving news by ID."""
    created_news = news_service.create_from_scraped_data(sample_scraped_data)
    retrieved_news = news_service.get_news_by_id(created_news.uid)

    assert retrieved_news is not None
    assert retrieved_news.uid == created_news.uid
    assert retrieved_news.header == created_news.header


def test_get_news_by_nonexistent_id(news_service: NewsService):
    """Test retrieving news with nonexistent ID."""
    news = news_service.get_news_by_id("nonexistent-id")
    assert news is None


def test_update_news(news_service: NewsService, sample_scraped_data: ScrapedNewsData):
    """Test updating news."""
    created_news = news_service.create_from_scraped_data(sample_scraped_data)

    updated_news = news_service.update_news(
        created_news.uid, header="Updated Header", content="Updated content"
    )

    assert updated_news is not None
    assert updated_news.header == "Updated Header"
    assert updated_news.content == "Updated content"
    assert updated_news.url == created_news.url  # Unchanged


def test_delete_news(news_service: NewsService, sample_scraped_data: ScrapedNewsData):
    """Test deleting news."""
    created_news = news_service.create_from_scraped_data(sample_scraped_data)

    # Delete the news
    result = news_service.delete_news(created_news.uid)
    assert result is True

    # Verify it's deleted
    retrieved_news = news_service.get_news_by_id(created_news.uid)
    assert retrieved_news is None


def test_get_all_news(news_service: NewsService):
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


def test_news_with_relationships(
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


def test_create_news_with_relationships(
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


def test_create_news_minimal(news_service: NewsService):
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


def test_create_duplicate_news(news_service: NewsService):
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
    news_service: NewsService, topic_service: TopicService
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


def test_news_crud_operations(news_service: NewsService):
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
