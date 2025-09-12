from datetime import datetime
from unittest.mock import patch

import pytest
from pydantic import HttpUrl

from digiliencia.data.models.neomodel.news import News
from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.data.services.neomodel.author_service import AuthorService
from digiliencia.data.services.neomodel.field.field_service import FieldService
from digiliencia.data.services.neomodel.news_service import NewsService
from digiliencia.data.services.neomodel.topic.topic_service import TopicService

# =============================================================================
# Helper Functions
# =============================================================================


def create_scraped_news_data(**kwargs) -> ScrapedNews:
    """Helper to create ScrapedNews with custom parameters."""
    defaults = {
        "header": "Test News",
        "date": datetime(2023, 1, 1, 12, 0),
        "source": "Test Source",
        "content": "Test content",
        "url": HttpUrl("https://example.com/test"),
        "authors": ["Test Author"],
        "topics": ["Test Topic"],
    }
    defaults.update(kwargs)
    return ScrapedNews(**defaults)


# =============================================================================
# Tests
# =============================================================================


def test_create_from_scraped_data(news_service: NewsService, sample_scraped_data):
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


def test_get_news_by_id(news_service: NewsService, sample_scraped_data):
    """Test retrieving news by ID."""
    created_news = news_service.create_from_scraped_data(sample_scraped_data)
    retrieved_news = news_service.get_news_by_id(str(created_news.uid))

    assert retrieved_news is not None
    assert retrieved_news.uid == created_news.uid
    assert retrieved_news.header == created_news.header


def test_get_news_by_nonexistent_id(news_service: NewsService):
    """Test retrieving news with nonexistent ID."""
    news = news_service.get_news_by_id("nonexistent-id")
    assert news is None


def test_update_news(news_service: NewsService, sample_scraped_data):
    """Test updating news."""
    created_news = news_service.create_from_scraped_data(sample_scraped_data)

    updated_news = news_service.update_news(
        str(created_news.uid), header="Updated Header", content="Updated content"
    )

    assert updated_news is not None
    assert updated_news.header == "Updated Header"
    assert updated_news.content == "Updated content"
    assert updated_news.url == created_news.url  # Unchanged


def test_update_news_nonexistent_id(news_service: NewsService):
    """Test updating news with nonexistent ID."""
    result = news_service.update_news(
        "nonexistent-id", header="New Header", content="New Content"
    )
    assert result is None


def test_delete_news(news_service: NewsService, sample_scraped_data):
    """Test deleting news."""
    created_news = news_service.create_from_scraped_data(sample_scraped_data)

    # Delete the news
    result = news_service.delete_news(str(created_news.uid))
    assert result is True

    # Verify it's deleted
    retrieved_news = news_service.get_news_by_id(str(created_news.uid))
    assert retrieved_news is None


def test_delete_news_nonexistent_id(news_service: NewsService):
    """Test deleting news with nonexistent ID."""
    result = news_service.delete_news("nonexistent-id")
    assert result is False


def test_create_news_with_relationships(
    news_service: NewsService,
    topic_service: TopicService,
    author_service: AuthorService,
):
    """Test creating news with topics and authors."""
    # Create some topics first
    topic_service.create_topic(
        "Cybersecurity", "Security-related topics", "https://example.com/cybersecurity"
    )
    topic_service.create_topic(
        "Privacy", "Privacy-related topics", "https://example.com/privacy"
    )

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
    connected_agency = news.published_by.single()  # type: ignore
    assert connected_agency is not None
    assert connected_agency.name == "Integration Source"

    connected_authors = news.written_by.all()  # type: ignore
    assert len(connected_authors) == 2
    author_names = [author.name for author in connected_authors]
    assert "Alice Johnson" in author_names
    assert "Bob Wilson" in author_names

    connected_topics = news.topics.all()  # type: ignore
    assert len(connected_topics) == 2
    topic_names = [topic.name for topic in connected_topics]
    assert "Cybersecurity" in topic_names
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
    agency = news.published_by.single()  # type: ignore
    assert agency is not None
    assert agency.name == "Minimal Source"

    # Should have no authors or topics
    assert len(news.written_by.all()) == 0  # type: ignore
    assert len(news.topics.all()) == 0  # type: ignore


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
    topic_service.create_topic(
        "Cybersecurity", "Cybersecurity topics", "https://example.com/cybersecurity-2"
    )
    topic_service.create_topic(
        "AI Security", "AI Security topics", "https://example.com/ai-security"
    )

    scraped_data = create_scraped_news_data(
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
    agency = news.published_by.single()  # type: ignore
    assert agency.name == scraped_data.source

    authors = news.written_by.all()  # type: ignore
    assert len(authors) == 2
    author_names = [author.name for author in authors]
    assert "Scraped Author 1" in author_names
    assert "Scraped Author 2" in author_names

    topics = news.topics.all()  # type: ignore
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
    retrieved_news = news_service.get_news_by_id(str(original_uid))
    assert retrieved_news is not None
    assert retrieved_news.uid == original_uid
    assert retrieved_news.header == "CRUD Test News"

    # Update
    updated_news = news_service.update_news(
        str(original_uid), header="Updated CRUD Test News", content="Updated content"
    )
    assert updated_news is not None
    assert updated_news.header == "Updated CRUD Test News"
    assert updated_news.content == "Updated content"
    assert updated_news.url == "https://example.com/crud"  # Unchanged

    # Verify update persisted
    retrieved_again = news_service.get_news_by_id(str(original_uid))
    assert retrieved_again is not None
    assert retrieved_again.header == "Updated CRUD Test News"

    # Delete
    delete_result = news_service.delete_news(str(original_uid))
    assert delete_result is True

    # Verify deletion
    deleted_news = news_service.get_news_by_id(str(original_uid))
    assert deleted_news is None

    # Try to delete again (should return False)
    delete_again = news_service.delete_news(str(original_uid))
    assert delete_again is False


def test_create_from_scraped_data_exception_handling(news_service: NewsService):
    """Test exception handling in create_from_scraped_data."""
    sample_data = create_scraped_news_data()

    # Mock News.get_or_create_with_relationships to raise an exception
    with patch(
        "digiliencia.data.models.neomodel.news.News.get_or_create_with_relationships"
    ) as mock_create:
        mock_create.side_effect = Exception("Database connection error")

        with pytest.raises(Exception) as exc_info:
            news_service.create_from_scraped_data(sample_data)

        assert "Database connection error" in str(exc_info.value)


def test_get_all_news_empty_database(news_service: NewsService):
    """Test get_all_news when database might be empty."""
    # Even if database has items, this exercises the list() conversion
    all_news = news_service.get_all_news()
    assert isinstance(all_news, list)


def test_update_news_all_parameters(news_service: NewsService, sample_scraped_data):
    """Test updating news with all possible parameters."""
    created_news = news_service.create_from_scraped_data(sample_scraped_data)

    # Update with all parameters
    updated_news = news_service.update_news(
        str(created_news.uid),
        header="New Header",
        content="New Content",
        url="https://new-url.com",
    )

    assert updated_news is not None
    assert updated_news.header == "New Header"
    assert updated_news.content == "New Content"
    assert updated_news.url == "https://new-url.com"


def test_update_news_partial_parameters(news_service: NewsService, sample_scraped_data):
    """Test updating news with only some parameters."""
    created_news = news_service.create_from_scraped_data(sample_scraped_data)
    original_content = created_news.content
    original_url = created_news.url

    # Update only header
    updated_news = news_service.update_news(
        str(created_news.uid), header="Only Header Changed"
    )

    assert updated_news is not None
    assert updated_news.header == "Only Header Changed"
    assert updated_news.content == original_content  # Unchanged
    assert updated_news.url == original_url  # Unchanged


def test_get_all_news_without_topics(
    news_service: NewsService, topic_service: TopicService
):
    """Test retrieving all news items without topics."""
    # Create news with topics
    topic_service.create_topic("Tech", "Technology news", "https://example.com/tech")
    news_service.create_news(
        header="News with Topics",
        date=datetime(2023, 1, 1),
        content="Content with topics",
        url="https://example.com/with-topics",
        source_name="Source 1",
        topic_names=["Tech"],
    )

    # Create news without topics
    news_without_topics = news_service.create_news(
        header="News without Topics",
        date=datetime(2023, 1, 2),
        content="Content without topics",
        url="https://example.com/without-topics",
        source_name="Source 2",
    )

    # Get news without topics
    news_list = news_service.get_all_news_without_topics()

    # Should only return news without topics
    assert len(news_list) == 1
    assert news_list[0].uid == news_without_topics.uid
    assert news_list[0].header == "News without Topics"


def test_get_all_news_without_topics_empty_database(news_service: NewsService):
    """Test get_all_news_without_topics when database is empty."""
    news_list = news_service.get_all_news_without_topics()
    assert isinstance(news_list, list)
    assert len(news_list) == 0


def test_get_all_news_without_topics_all_have_topics(
    news_service: NewsService, topic_service: TopicService
):
    """Test get_all_news_without_topics when all news have topics."""
    # Create topic
    topic_service.create_topic("General", "General news", "https://example.com/general")

    # Create multiple news items, all with topics
    news_service.create_news(
        header="News 1",
        date=datetime(2023, 1, 1),
        content="Content 1",
        url="https://example.com/news1",
        source_name="Source 1",
        topic_names=["General"],
    )

    news_service.create_news(
        header="News 2",
        date=datetime(2023, 1, 2),
        content="Content 2",
        url="https://example.com/news2",
        source_name="Source 2",
        topic_names=["General"],
    )

    # Should return empty list
    news_list = news_service.get_all_news_without_topics()
    assert isinstance(news_list, list)
    assert len(news_list) == 0


def test_set_topics_relations(news_service: NewsService, topic_service: TopicService):
    """Test setting topic relationships for news."""
    # Create news without topics initially
    news = news_service.create_news(
        header="Test News for Topics",
        date=datetime(2023, 1, 1),
        content="Test content",
        url="https://example.com/test-topics",
        source_name="Test Source",
    )

    # Create topics
    topic1 = topic_service.create_topic(
        "Topic 1", "Description 1", "https://example.com/topic1"
    )
    topic2 = topic_service.create_topic(
        "Topic 2", "Description 2", "https://example.com/topic2"
    )

    # Initially should have no topics
    assert len(news.topics.all()) == 0  # type: ignore

    # Set topic relationships
    news_service.set_topics_relations(news, [topic1, topic2])

    # Verify relationships were created
    connected_topics = news.topics.all()  # type: ignore
    assert len(connected_topics) == 2

    topic_names = [topic.name for topic in connected_topics]
    assert "Topic 1" in topic_names
    assert "Topic 2" in topic_names


def test_set_topics_relations_empty_list(news_service: NewsService):
    """Test setting empty topic relationships list."""
    # Create news
    news = news_service.create_news(
        header="Test News Empty Topics",
        date=datetime(2023, 1, 1),
        content="Test content",
        url="https://example.com/empty-topics",
        source_name="Test Source",
    )

    # Set empty topics list
    news_service.set_topics_relations(news, [])

    # Should still have no topics
    assert len(news.topics.all()) == 0  # type: ignore


def test_set_fields_relations(news_service: NewsService):
    """Test setting field relationships for news."""
    field_service = FieldService()

    # Create news without fields initially
    news = news_service.create_news(
        header="Test News for Fields",
        date=datetime(2023, 1, 1),
        content="Test content",
        url="https://example.com/test-fields",
        source_name="Test Source",
    )

    # Create fields
    field1 = field_service.create_field("Field 1", "Description 1")
    field2 = field_service.create_field("Field 2", "Description 2")

    # Initially should have no fields
    assert len(news.fields.all()) == 0  # type: ignore

    # Set field relationships
    news_service.set_fields_relations(news, [field1, field2])

    # Verify relationships were created
    connected_fields = news.fields.all()  # type: ignore
    assert len(connected_fields) == 2

    field_names = [field.name for field in connected_fields]
    assert "Field 1" in field_names
    assert "Field 2" in field_names


def test_set_fields_relations_empty_list(news_service: NewsService):
    """Test setting empty field relationships list."""
    # Create news
    news = news_service.create_news(
        header="Test News Empty Fields",
        date=datetime(2023, 1, 1),
        content="Test content",
        url="https://example.com/empty-fields",
        source_name="Test Source",
    )

    # Set empty fields list
    news_service.set_fields_relations(news, [])

    # Should still have no fields
    assert len(news.fields.all()) == 0  # type: ignore


def test_set_fields_relations_duplicate_fields(news_service: NewsService):
    """Test setting field relationships with duplicate fields."""
    field_service = FieldService()

    # Create news
    news = news_service.create_news(
        header="Test News Duplicate Fields",
        date=datetime(2023, 1, 1),
        content="Test content",
        url="https://example.com/duplicate-fields",
        source_name="Test Source",
    )

    # Create field
    field1 = field_service.create_field("Duplicate Field", "Description")

    # Set same field twice
    news_service.set_fields_relations(news, [field1])
    news_service.set_fields_relations(news, [field1])

    # Should still only have one relationship (neomodel handles duplicates)
    connected_fields = news.fields.all()  # type: ignore
    assert len(connected_fields) == 1
    assert connected_fields[0].name == "Duplicate Field"


def test_create_news_error_handling_database_connection(news_service: NewsService):
    """Test error handling when database connection fails during news creation."""
    with patch(
        "digiliencia.data.models.neomodel.news.News.get_or_create_with_relationships"
    ) as mock_create:
        mock_create.side_effect = Exception("Database connection failed")

        with pytest.raises(Exception) as exc_info:
            news_service.create_news(
                header="Test News",
                date=datetime(2023, 1, 1),
                content="Test content",
                url="https://example.com/test",
                source_name="Test Source",
            )

        assert "Database connection failed" in str(exc_info.value)


def test_get_news_by_id_does_not_exist_exception(news_service: NewsService):
    """Test handling when News.DoesNotExist is raised during retrieval."""
    with patch("digiliencia.data.models.neomodel.news.News.nodes.get") as mock_get:
        mock_get.side_effect = News.DoesNotExist("News not found")

        # Should return None when DoesNotExist is raised
        result = news_service.get_news_by_id("test-id")
        assert result is None


def test_update_news_does_not_exist_exception(news_service: NewsService):
    """Test handling when News.DoesNotExist is raised during update."""
    with patch("digiliencia.data.models.neomodel.news.News.nodes.get") as mock_get:
        mock_get.side_effect = News.DoesNotExist("News not found")

        # Should return None when DoesNotExist is raised
        result = news_service.update_news("test-id", header="Updated Header")
        assert result is None


def test_delete_news_does_not_exist_exception(news_service: NewsService):
    """Test handling when News.DoesNotExist is raised during deletion."""
    with patch("digiliencia.data.models.neomodel.news.News.nodes.get") as mock_get:
        mock_get.side_effect = News.DoesNotExist("News not found")

        # Should return False when DoesNotExist is raised
        result = news_service.delete_news("test-id")
        assert result is False


def test_news_service_initialization():
    """Test NewsService initialization."""
    service = NewsService()
    assert isinstance(service, NewsService)


def test_create_news_with_none_optional_parameters(news_service: NewsService):
    """Test creating news with explicitly None optional parameters."""
    news = news_service.create_news(
        header="Test News None Params",
        date=datetime(2023, 1, 1),
        content="Test content",
        url="https://example.com/none-params",
        source_name="Test Source",
        author_names=None,
        topic_names=None,
    )

    assert isinstance(news, News)
    assert news.header == "Test News None Params"
    assert len(news.written_by.all()) == 0  # type: ignore
    assert len(news.topics.all()) == 0  # type: ignore


def test_get_all_news_multiple_items(news_service: NewsService):
    """Test retrieving multiple news items."""
    # Create multiple news items
    news_service.create_news(
        header="News 1",
        date=datetime(2023, 1, 1),
        content="Content 1",
        url="https://example.com/news1",
        source_name="Source 1",
    )
    news_service.create_news(
        header="News 2",
        date=datetime(2023, 1, 2),
        content="Content 2",
        url="https://example.com/news2",
        source_name="Source 2",
    )

    all_news = news_service.get_all_news()

    assert len(all_news) >= 2  # May have other news from other tests
    news_headers = [news.header for news in all_news]
    assert "News 1" in news_headers
    assert "News 2" in news_headers


def test_set_topics_relations_existing_connections(
    news_service: NewsService, topic_service: TopicService
):
    """Test setting topic relationships when connections already exist."""
    # Create news and topics
    news = news_service.create_news(
        header="Test News Existing Topics",
        date=datetime(2023, 1, 1),
        content="Test content",
        url="https://example.com/existing-topics",
        source_name="Test Source",
    )

    topic1 = topic_service.create_topic(
        "Existing Topic 1", "Description 1", "https://example.com/topic1"
    )
    topic2 = topic_service.create_topic(
        "Existing Topic 2", "Description 2", "https://example.com/topic2"
    )

    # Set topics twice - should handle existing connections gracefully
    news_service.set_topics_relations(news, [topic1])
    news_service.set_topics_relations(news, [topic1, topic2])

    # Should have both topics connected
    connected_topics = news.topics.all()  # type: ignore
    assert len(connected_topics) == 2

    topic_names = [topic.name for topic in connected_topics]
    assert "Existing Topic 1" in topic_names
    assert "Existing Topic 2" in topic_names


def test_create_from_scraped_data_with_empty_lists(news_service: NewsService):
    """Test creating news from scraped data with empty authors and topics lists."""
    scraped_data = create_scraped_news_data(
        authors=[],
        topics=[],
    )

    news = news_service.create_from_scraped_data(scraped_data)

    assert isinstance(news, News)
    assert news.header == scraped_data.header
    assert len(news.written_by.all()) == 0  # type: ignore
    assert len(news.topics.all()) == 0  # type: ignore


def test_get_all_news_without_topics_mixed_scenarios(
    news_service: NewsService, topic_service: TopicService
):
    """Test get_all_news_without_topics with mixed scenarios."""
    # Create topic
    topic_service.create_topic(
        "Mixed Topic", "Mixed description", "https://example.com/mixed"
    )

    # Create news with different topic configurations
    news_service.create_news(
        header="News With Topic",
        date=datetime(2023, 1, 1),
        content="Content with topic",
        url="https://example.com/with-topic",
        source_name="Source 1",
        topic_names=["Mixed Topic"],
    )

    news_service.create_news(
        header="First News Without Topic",
        date=datetime(2023, 1, 2),
        content="First content without topic",
        url="https://example.com/without-topic1",
        source_name="Source 2",
    )

    news_service.create_news(
        header="Second News Without Topic",
        date=datetime(2023, 1, 3),
        content="Second content without topic",
        url="https://example.com/without-topic2",
        source_name="Source 3",
    )

    # Get news without topics
    news_without_topics = news_service.get_all_news_without_topics()

    # Should return only the news without topics
    assert len(news_without_topics) >= 2  # At least our 2 news items
    news_headers = [news.header for news in news_without_topics]
    assert "First News Without Topic" in news_headers
    assert "Second News Without Topic" in news_headers
    assert "News With Topic" not in news_headers
