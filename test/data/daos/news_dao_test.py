from datetime import datetime

import pytest

from digiliencia.data.daos.news_dao import NewsDAO
from digiliencia.data.daos.organization.news_agency_dao import NewsAgencyDAO
from digiliencia.data.daos.person.person_dao import PersonDAO
from digiliencia.data.daos.topic_dao import TopicDAO
from digiliencia.data.models.news_model import RawNewsModel, ScrapedNewsModel
from digiliencia.exc.dao_create_exc import DAOCreateError
from digiliencia.exc.dao_delete_exc import DAODeleteError
from digiliencia.exc.dao_read_exc import DAOReadError
from digiliencia.exc.dao_update_exc import DAOUpdateError

# These tests require a test Neo4j database to be running with test fixtures preloaded.


@pytest.fixture(scope="module")
def news_dao():
    return NewsDAO()


@pytest.fixture
def sample_data():
    return {
        "header": "Test Headline",
        "date": datetime(2023, 1, 1, 12, 0),
        "source_id": "source-uuid",
        "content": "Test news content",
        "url": "https://example.com/news",
        "author_ids": ["author1-uuid", "author2-uuid"],
        "topic_ids": ["topic1-uuid", "topic2-uuid"],
    }


@pytest.fixture
def sample_scraped_news():
    return ScrapedNewsModel(
        header="Scraped Headline",
        date=datetime(2023, 1, 1, 12, 0),
        source="Test Source",
        content="Scraped content",
        url="https://example.com/scraped",
        authors=["Author 1", "Author 2"],
        topics=["Topic 1", "Topic 2"],
    )


@pytest.fixture
def daos():
    return {
        "news": NewsDAO(),
        "agency": NewsAgencyDAO(),
        "person": PersonDAO(),
        "topic": TopicDAO(),
    }


@pytest.fixture
def test_date():
    return datetime(2023, 1, 1, 12, 0)


def test_build_model(news_dao, sample_data):
    news = news_dao._build_model({"id": "test-uuid", **sample_data})
    assert isinstance(news, RawNewsModel)
    assert news.header == sample_data["header"]


def test_create_success(news_dao, sample_data):
    result = news_dao.create(**sample_data)
    assert isinstance(result, RawNewsModel)
    assert result.header == sample_data["header"]


def test_create_constraint_error(news_dao, sample_data):
    news_dao.create(**sample_data)
    with pytest.raises(DAOCreateError):
        news_dao.create(**sample_data)


def test_create_from_scrap_success(news_dao, sample_scraped_news):
    result = news_dao.create_from_scrap(sample_scraped_news)
    assert isinstance(result, RawNewsModel)
    assert result.header == sample_scraped_news.header


def test_create_from_scrap_no_source(news_dao, sample_scraped_news):
    modified_scraped_news = ScrapedNewsModel(
        header=sample_scraped_news.header,
        date=sample_scraped_news.date,
        source="non-existent",
        content=sample_scraped_news.content,
        url=sample_scraped_news.url,
        authors=sample_scraped_news.authors,
        topics=sample_scraped_news.topics,
    )

    created = news_dao.create_from_scrap(modified_scraped_news)

    # Verify that a new source was created with the name "non-existent"
    agency_dao = NewsAgencyDAO()
    non_existent_source = agency_dao.read_by_id(created.source_id)
    assert non_existent_source is not None, (
        "Source 'non-existent' should have been created"
    )

    # Verify that the created news has correct fields
    assert created.header == modified_scraped_news.header
    assert created.content == modified_scraped_news.content
    assert created.url == modified_scraped_news.url
    assert created.source_id == non_existent_source.id


def test_read_by_id_success(news_dao):
    agency_dao = NewsAgencyDAO()
    agency = agency_dao.create(name="Test Agency", description="desc")
    sample_data = {
        "header": "Test Headline",
        "date": datetime(2023, 1, 1, 12, 0),
        "source_id": agency.id,
        "content": "Test news content",
        "url": "https://example.com/news",
        "author_ids": [],
        "topic_ids": [],
    }
    created = news_dao.create(**sample_data)
    result = news_dao.read_by_id(created.id)
    assert isinstance(result, RawNewsModel)
    assert result.id == created.id
    assert result.header == sample_data["header"]
    assert result.content == sample_data["content"]
    assert result.url == sample_data["url"]
    assert result.date == sample_data["date"]


def test_read_by_id_not_found(news_dao):
    with pytest.raises(DAOReadError):
        news_dao.read_by_id("non-existent")


def test_read_all(news_dao):
    results = news_dao.read_all()
    assert isinstance(results, list)
    assert all(isinstance(r, RawNewsModel) for r in results)


def test_update_success(news_dao, sample_data):
    created = news_dao.create(**sample_data)
    updated = news_dao.update(
        created.id, header="Updated Headline", content="Updated content"
    )
    assert updated.header == "Updated Headline"


def test_update_not_found(news_dao):
    with pytest.raises(DAOUpdateError):
        news_dao.update("non-existent", header="Fail")


def test_delete_success(news_dao, sample_data):
    created = news_dao.create(**sample_data)
    news_dao.delete(created.id)
    with pytest.raises(DAOReadError):
        news_dao.read_by_id(created.id)


def test_delete_not_found(news_dao):
    with pytest.raises(DAODeleteError):
        news_dao.delete("non-existent")


def test_read_by_source(news_dao):
    # Create a source
    agency_dao = NewsAgencyDAO()
    agency = agency_dao.create(name="Test Source", description="Test Organization")
    assert agency is not None
    assert agency.id is not None

    # Check there are no news for this source
    results = news_dao.read_by_source(agency.id)
    assert isinstance(results, list)
    assert all(isinstance(r, RawNewsModel) for r in results)
    assert len(results) == 0

    # Create a news item for this source
    sample_data = {
        "header": "Source Test Headline",
        "date": datetime(2023, 1, 1, 12, 0),
        "source_id": agency.id,
        "content": "Source Test Content",
        "url": "https://example.com/source-test",
        "author_ids": [],
        "topic_ids": [],
    }
    created_news = news_dao.create(**sample_data)
    assert created_news is not None
    assert created_news.source_id == agency.id
    assert created_news.header == sample_data["header"]
    assert created_news.content == sample_data["content"]

    # Read news by source
    results = news_dao.read_by_source(agency.id)
    assert isinstance(results, list)
    assert all(isinstance(r, RawNewsModel) for r in results)
    assert len(results) == 1
    assert results[0].id == created_news.id
    assert results[0].header == sample_data["header"]
    assert results[0].content == sample_data["content"]

    # Create another two news items for the same source
    for i in range(2):
        sample_data["header"] = f"Source Test Headline {i + 2}"
        sample_data["content"] = f"Source Test Content {i + 2}"
        news_dao.create(**sample_data)

    # Read news by source again
    results = news_dao.read_by_source(agency.id)
    assert isinstance(results, list)
    assert all(isinstance(r, RawNewsModel) for r in results)
    assert len(results) == 3  # Should have 3 news items now
    assert all(r.source_id == agency.id for r in results)
    assert all(r.header.startswith("Source Test Headline") for r in results)


def test_read_by_source_exception(news_dao):
    with pytest.raises(DAOReadError):
        news_dao.read_by_source("invalid-source")


def test_read_by_topic_exception(news_dao):
    with pytest.raises(DAOReadError):
        news_dao.read_by_topic("invalid-topic")


def test_read_by_id_with_real_db(daos, test_date):
    source_dao = daos["agency"]
    author_dao = daos["person"]
    topic_dao = daos["topic"]
    news_dao = daos["news"]

    source = source_dao.create(name="Read Test Source", description="Test Organization")
    author = author_dao.create(name="Read Test Author")  # type: ignore
    topic = topic_dao.create(name="Read Test Topic", definition="Test Topic Definition")

    created_news = news_dao.create(
        header="Read Test Headline",
        date=test_date,
        source_id=source.id,
        content="Read Test Content",
        url="https://example.com/read-test",
        author_ids=[author.id],
        topic_ids=[topic.id],
    )

    read_news = news_dao.read_by_id(created_news.id)

    assert read_news is not None
    assert read_news.id == created_news.id
    assert read_news.header == created_news.header

    news_dao.delete(created_news.id)
    topic_dao.delete(topic.id)
    author_dao.delete(author.id)
    source_dao.delete(source.id)

    with pytest.raises(DAOReadError):
        news_dao.read_by_id(created_news.id)


def test_create_from_scrap_with_new_entities_real_db():
    news_dao = NewsDAO()
    agency_dao = NewsAgencyDAO()
    person_dao = PersonDAO()

    test_prefix = f"test_{datetime.now().strftime('%Y%m%d%H%M%S')}"
    test_source = f"{test_prefix}_TestSource"
    test_author = f"{test_prefix}_TestAuthor"

    scraped_news = ScrapedNewsModel(
        header=f"{test_prefix} Test Headline",
        date=datetime.now(),
        source=test_source,
        content="Test content for integration test",
        url=f"https://example.com/{test_prefix}",
        authors=[test_author],
        topics=[],  # No topics for this test
    )

    created_news = None
    created_author_id = None
    created_source_id = None

    try:
        created_news = news_dao.create_from_scrap(scraped_news)

        assert created_news is not None
        assert created_news.header == scraped_news.header
        assert created_news.content == scraped_news.content
        assert created_news.url == scraped_news.url

        assert created_news.source_id is not None
        created_source_id = created_news.source_id

        source = agency_dao.read_by_id(created_source_id)
        assert source.name == test_source

        assert len(created_news.author_ids) == 1
        created_author_id = created_news.author_ids[0]

        author = person_dao.read_by_id(created_author_id)
        assert author.name == test_author

        assert len(created_news.topic_ids) == 0

    finally:
        if created_news:
            try:
                news_dao.delete(created_news.id)
            except Exception as e:
                print(f"Error cleaning up test news: {e}")
        if created_author_id:
            try:
                person_dao.delete(created_author_id)
            except Exception as e:
                print(f"Error cleaning up test author: {e}")
        if created_source_id:
            try:
                agency_dao.delete(created_source_id)
            except Exception as e:
                print(f"Error cleaning up test source: {e}")
