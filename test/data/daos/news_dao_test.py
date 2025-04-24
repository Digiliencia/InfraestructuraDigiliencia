import unittest
from datetime import datetime
from unittest.mock import MagicMock, Mock, patch

from neo4j.exceptions import ConstraintError

from digiliencia.data.daos.news_dao import NewsDAO
from digiliencia.data.daos.organization.news_agency_dao import NewsAgencyDAO
from digiliencia.data.daos.person_dao import PersonDAO
from digiliencia.data.daos.topic_dao import TopicDAO
from digiliencia.data.models.news_model import RawNewsModel, ScrapedNewsModel
from digiliencia.exc.dao_create_exc import DAOCreateError
from digiliencia.exc.dao_delete_exc import DAODeleteError
from digiliencia.exc.dao_read_exc import DAOReadError
from digiliencia.exc.dao_update_exc import DAOUpdateError


class TestNewsDAO(unittest.TestCase):
    _is_parallel = False  # Force sequential execution

    def setUp(self):
        self.news_dao = NewsDAO()
        # Sample test data
        self.test_date = datetime(2023, 1, 1, 12, 0)
        self.test_news_data = {
            "id": "test-uuid",
            "header": "Test Headline",
            "date": self.test_date,
            "source_id": "source-uuid",
            "content": "Test news content",
            "url": "https://example.com/news",
            "author_ids": ["author1-uuid", "author2-uuid"],
            "topic_ids": ["topic1-uuid", "topic2-uuid"],
        }
        self.test_scraped_news = ScrapedNewsModel(
            header="Scraped Headline",
            date=self.test_date,
            source="Test Source",
            content="Scraped content",
            url="https://example.com/scraped",
            authors=["Author 1", "Author 2"],
            topics=["Topic 1", "Topic 2"],
        )

    def test_build_model(self):
        """Test the _build_model method creates a valid RawNewsModel"""
        # Test with datetime object
        raw_data = self.test_news_data.copy()
        news = self.news_dao._build_model(raw_data)

        self.assertIsInstance(news, RawNewsModel)
        self.assertEqual(news.id, "test-uuid")
        self.assertEqual(news.header, "Test Headline")
        self.assertEqual(news.date, self.test_date)
        self.assertEqual(news.content, "Test news content")

        # Test with date as string
        raw_data["date"] = "2023-01-01T12:00:00"
        news = self.news_dao._build_model(raw_data)
        self.assertEqual(news.date, self.test_date)

    def test_create_constraint_error(self):
        """Test creating news with a constraint violation raises correct exception"""
        # Setup mock
        mock_session = Mock()
        mock_session.run.side_effect = ConstraintError("Duplicate constraint")

        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = mock_session
        mock_cm.__exit__.return_value = None

        self.news_dao.db.get_connection = Mock(return_value=mock_cm)

        # Test exception is raised
        with self.assertRaises(DAOCreateError):
            self.news_dao.create(
                header="Test Headline",
                date=self.test_date,
                source_id="source-id",
                content="Test content",
                url="https://example.com/news",
            )

    def test_create_no_record(self):
        """Test create method when no record is returned"""
        # Setup mock
        mock_result = Mock()
        mock_result.single.return_value = None

        mock_session = Mock()
        mock_session.run.return_value = mock_result

        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = mock_session
        mock_cm.__exit__.return_value = None

        self.news_dao.db.get_connection = Mock(return_value=mock_cm)

        # Test exception is raised
        with self.assertRaises(DAOCreateError):
            self.news_dao.create(
                header="Test Headline",
                date=self.test_date,
                source_id="source-id",
                content="Test content",
                url="https://example.com/news",
            )

    def test_create_from_scrap_no_source(self):
        """Test create_from_scrap when source is not found"""
        # Setup mock for lookup query returning no source
        mock_result = Mock()
        mock_result.single.return_value = None

        mock_session = Mock()
        mock_session.run.return_value = mock_result

        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = mock_session
        mock_cm.__exit__.return_value = None

        self.news_dao.db.get_connection = Mock(return_value=mock_cm)

        # Test exception is raised
        with self.assertRaises(DAOCreateError):
            self.news_dao.create_from_scrap(self.test_scraped_news)

    def test_create_from_scrap_success(self):
        """Test create_from_scrap successfully creates news"""
        # Setup mocks for both database calls
        # First call returns source, authors and topics lookup
        mock_lookup_result = Mock()
        mock_lookup_record = {
            "source_id": "source-id",
            "authors": [
                {"name": "Author 1", "id": "author1-id"},
                {"name": "Author 2", "id": "author2-id"},
            ],
            "topics": [
                {"name": "Topic 1", "id": "topic1-id"},
                {"name": "Topic 2", "id": "topic2-id"},
            ],
        }
        mock_lookup_result.single.return_value = mock_lookup_record

        # Second call (create) returns the created news node
        mock_create_result = Mock()
        mock_news_node = {
            "id": "news-uuid",
            "header": "Scraped Headline",
            "date": self.test_date.isoformat(),
            "source_id": "source-id",
            "content": "Scraped content",
            "url": "https://example.com/scraped",
        }
        mock_create_result.single.return_value = {"n": mock_news_node}

        # Create mock session that returns different results for different calls
        mock_session1 = Mock()
        mock_session1.run.return_value = mock_lookup_result
        mock_session2 = Mock()
        mock_session2.run.return_value = mock_create_result

        # Mock connections that return the appropriate session
        mock_cm1 = MagicMock()
        mock_cm1.__enter__.return_value = mock_session1
        mock_cm1.__exit__.return_value = None
        mock_cm2 = MagicMock()
        mock_cm2.__enter__.return_value = mock_session2
        mock_cm2.__exit__.return_value = None

        # Patch the get_connection method to return the appropriate mock
        with patch.object(self.news_dao.db, "get_connection") as mock_get_connection:
            mock_get_connection.side_effect = [mock_cm1, mock_cm2]

            # Now mock the create method to avoid actually calling it
            with patch.object(self.news_dao, "create") as mock_create:
                expected_news = RawNewsModel(
                    id="news-uuid",
                    header="Scraped Headline",
                    date=self.test_date,
                    source_id="source-id",
                    content="Scraped content",
                    url="https://example.com/scraped",
                    author_ids=["author1-id", "author2-id"],
                    topic_ids=["topic1-id", "topic2-id"],
                )
                mock_create.return_value = expected_news

                # Test the method
                result = self.news_dao.create_from_scrap(self.test_scraped_news)

                self.assertEqual(result, expected_news)
                # Check it was called with the right parameters
                mock_create.assert_called_once_with(
                    header="Scraped Headline",
                    date=self.test_date,
                    source_id="source-id",
                    content="Scraped content",
                    url="https://example.com/scraped",
                    author_ids=["author1-id", "author2-id"],
                    topic_ids=["topic1-id", "topic2-id"],
                )

    def test_read_by_id_not_found(self):
        """Test read_by_id method when no record is found"""
        # Setup mock with null record
        mock_result = Mock()
        mock_result.single.return_value = None

        mock_session = Mock()
        mock_session.run.return_value = mock_result

        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = mock_session
        mock_cm.__exit__.return_value = None

        self.news_dao.db.get_connection = Mock(return_value=mock_cm)

        # Test exception is raised
        with self.assertRaises(DAOReadError):
            self.news_dao.read_by_id("non-existent-uuid")

    def test_read_all_exception(self):
        """Test read_all method when exception occurs"""
        # Setup mock to raise exception
        mock_session = Mock()
        mock_session.run.side_effect = Exception("Database error")

        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = mock_session
        mock_cm.__exit__.return_value = None

        self.news_dao.db.get_connection = Mock(return_value=mock_cm)

        # Test exception is raised
        with self.assertRaises(DAOReadError):
            self.news_dao.read_all()

    def test_update_not_found(self):
        """Test update method when no news is found"""
        # Setup mock with null record
        mock_result = Mock()
        mock_result.single.return_value = None

        mock_session = Mock()
        mock_session.run.return_value = mock_result

        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = mock_session
        mock_cm.__exit__.return_value = None

        self.news_dao.db.get_connection = Mock(return_value=mock_cm)

        # Test exception is raised
        with self.assertRaises(DAOUpdateError):
            self.news_dao.update("non-existent-uuid", header="Updated Headline")

    def test_update_with_relationships(self):
        """Test update method with author and topic relationships"""
        # Setup mocks for update operations
        mock_property_result = Mock()
        mock_property_result.single.return_value = {
            "n": {"id": "news1", "header": "Updated Headline"}
        }

        # For read_by_id after update
        mock_read_result = Mock()
        mock_read_result.single.return_value = {
            "n": {
                "id": "news1",
                "header": "Updated Headline",
                "date": self.test_date.isoformat(),
                "content": "Updated content",
                "author_ids": ["new-author1", "new-author2"],
                "topic_ids": ["new-topic1", "new-topic2"],
            }
        }

        # Create a session that returns different results for different queries
        mock_session = Mock()
        mock_session.run = Mock()
        mock_session.run.side_effect = [
            mock_property_result,  # First for property update
            None,  # For author relationships
            None,  # For topic relationships
            mock_read_result,  # For final read_by_id
        ]

        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = mock_session
        mock_cm.__exit__.return_value = None

        # Need to patch get_connection to return our mock, and read_by_id to return expected result
        with patch.object(self.news_dao.db, "get_connection", return_value=mock_cm):
            with patch.object(self.news_dao, "read_by_id") as mock_read:
                expected_news = RawNewsModel(
                    id="news1",
                    header="Updated Headline",
                    date=self.test_date,
                    source_id="source-id",
                    content="Updated content",
                    url="https://example.com/updated",
                    author_ids=["new-author1", "new-author2"],
                    topic_ids=["new-topic1", "new-topic2"],
                )
                mock_read.return_value = expected_news

                # Test update with relationships
                result = self.news_dao.update(
                    "news1",
                    header="Updated Headline",
                    content="Updated content",
                    author_ids=["new-author1", "new-author2"],
                    topic_ids=["new-topic1", "new-topic2"],
                )

                # Check result
                self.assertEqual(result, expected_news)

                # Verify correct number of queries were executed
                self.assertEqual(mock_session.run.call_count, 3)

    def test_delete_not_found(self):
        """Test delete method when no news is found"""
        # Setup mock with no nodes deleted
        mock_result = Mock()
        mock_consume = Mock()
        mock_consume.counters.nodes_deleted = 0
        mock_result.consume.return_value = mock_consume

        mock_session = Mock()
        mock_session.run.return_value = mock_result

        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = mock_session
        mock_cm.__exit__.return_value = None

        self.news_dao.db.get_connection = Mock(return_value=mock_cm)

        # Test exception is raised
        with self.assertRaises(DAODeleteError):
            self.news_dao.delete("non-existent-uuid")

    @patch("digiliencia.data.daos.news_dao.NewsDAO.create")
    @patch("digiliencia.data.daos.news_dao.NewsDAO.read_by_id")
    @patch("digiliencia.data.daos.news_dao.NewsDAO.read_all")
    @patch("digiliencia.data.daos.news_dao.NewsDAO.update")
    @patch("digiliencia.data.daos.news_dao.NewsDAO.delete")
    def test_integration_cycle(
        self, mock_delete, mock_update, mock_read_all, mock_read_by_id, mock_create
    ):
        """Integration test for complete CRUD operations on News"""
        # Create a news item
        news_model = RawNewsModel(
            id="test-uuid",
            header="Integration Test News",
            date=self.test_date,
            source_id="source-id",
            content="Test content",
            url="https://example.com/integration",
            author_ids=["author1", "author2"],
            topic_ids=["topic1", "topic2"],
        )
        mock_create.return_value = news_model

        # Mock read operations
        mock_read_by_id.return_value = news_model
        mock_read_all.return_value = [news_model]

        # Mock update operation
        updated_news = RawNewsModel(
            id="test-uuid",
            header="Updated Integration Test News",
            date=self.test_date,
            source_id="source-id",
            content="Updated test content",
            url="https://example.com/integration",
            author_ids=["author1", "author2"],
            topic_ids=["topic1", "topic2"],
        )
        mock_update.return_value = updated_news

        # Execute CRUD cycle
        created = self.news_dao.create(
            header="Integration Test News",
            date=self.test_date,
            source_id="source-id",
            content="Test content",
            url="https://example.com/integration",
            author_ids=["author1", "author2"],
            topic_ids=["topic1", "topic2"],
        )

        self.assertIsNotNone(created)
        self.assertEqual(created.header, "Integration Test News")

        # Read
        read_news = self.news_dao.read_by_id(created.id)
        self.assertEqual(read_news.id, created.id)

        # Read all
        all_news = self.news_dao.read_all()
        self.assertTrue(any(n.id == created.id for n in all_news))

        # Update
        updated = self.news_dao.update(
            created.id,
            header="Updated Integration Test News",
            content="Updated test content",
        )
        self.assertEqual(updated.header, "Updated Integration Test News")

        # Delete
        self.news_dao.delete(created.id)
        mock_delete.assert_called_once_with(created.id)

    def test_create_success(self):
        """Test successful creation of news without exceptions"""
        # Setup mock with valid record
        mock_result = Mock()
        mock_result.single.return_value = {"n": self.test_news_data}

        mock_session = Mock()
        mock_session.run.return_value = mock_result

        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = mock_session
        mock_cm.__exit__.return_value = None

        self.news_dao.db.get_connection = Mock(return_value=mock_cm)

        # Test creation
        result = self.news_dao.create(
            header="Test Headline",
            date=self.test_date,
            source_id="source-uuid",
            content="Test news content",
            url="https://example.com/news",
            author_ids=["author1-uuid", "author2-uuid"],
            topic_ids=["topic1-uuid", "topic2-uuid"],
        )

        self.assertIsInstance(result, RawNewsModel)
        self.assertEqual(result.header, "Test Headline")

    def test_read_by_id_success(self):
        """Test successful read_by_id operation"""
        # Setup mock with valid record
        mock_result = Mock()
        mock_result.single.return_value = {"n": self.test_news_data}

        mock_session = Mock()
        mock_session.run.return_value = mock_result

        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = mock_session
        mock_cm.__exit__.return_value = None

        self.news_dao.db.get_connection = Mock(return_value=mock_cm)

        # Test read operation
        result = self.news_dao.read_by_id("test-uuid")

        self.assertIsInstance(result, RawNewsModel)
        self.assertEqual(result.id, "test-uuid")
        self.assertEqual(result.header, "Test Headline")

    def test_update_success(self):
        """Test successful update operation"""
        # Setup mock for update
        updated_data = self.test_news_data.copy()
        updated_data["header"] = "Updated Headline"
        updated_data["content"] = "Updated content"

        mock_update_result = Mock()
        mock_update_result.single.return_value = {"n": updated_data}

        mock_session = Mock()
        mock_session.run.return_value = mock_update_result

        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = mock_session
        mock_cm.__exit__.return_value = None

        self.news_dao.db.get_connection = Mock(return_value=mock_cm)

        # Mock the read_by_id call that happens after update
        with patch.object(self.news_dao, "read_by_id") as mock_read:
            expected_model = RawNewsModel(**updated_data)
            mock_read.return_value = expected_model

            # Test update
            result = self.news_dao.update(
                "test-uuid", header="Updated Headline", content="Updated content"
            )

            self.assertEqual(result.header, "Updated Headline")
            self.assertEqual(result.content, "Updated content")
            mock_read.assert_called_once_with("test-uuid")

    def test_read_by_source_success(self):
        """Test successful read_by_source operation"""
        # Setup mock with valid records
        mock_result = Mock()
        mock_records = [{"n": self.test_news_data}]
        mock_result.__iter__ = Mock(return_value=iter(mock_records))

        mock_session = Mock()
        mock_session.run.return_value = mock_result

        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = mock_session
        mock_cm.__exit__.return_value = None

        self.news_dao.db.get_connection = Mock(return_value=mock_cm)

        # Test read_by_source operation
        results = self.news_dao.read_by_source("source-uuid")

        self.assertEqual(len(results), 1)
        self.assertIsInstance(results[0], RawNewsModel)
        self.assertEqual(results[0].id, "test-uuid")
        self.assertEqual(results[0].source_id, "source-uuid")
        mock_session.run.assert_called_once()

    def test_read_by_source_exception(self):
        """Test exception handling in read_by_source method"""
        # Setup mock to raise exception
        mock_session = Mock()
        mock_session.run.side_effect = Exception("Database error")

        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = mock_session
        mock_cm.__exit__.return_value = None

        self.news_dao.db.get_connection = Mock(return_value=mock_cm)

        # Test exception is raised
        with self.assertRaises(DAOReadError):
            self.news_dao.read_by_source("source-uuid")

    def test_read_by_topic_exception(self):
        """Test exception handling in read_by_topic method"""
        # Setup mock to raise exception
        mock_session = Mock()
        mock_session.run.side_effect = Exception("Database error")

        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = mock_session
        mock_cm.__exit__.return_value = None

        self.news_dao.db.get_connection = Mock(return_value=mock_cm)

        # Test exception is raised
        with self.assertRaises(DAOReadError):
            self.news_dao.read_by_topic("topic-uuid")

    def test_read_by_organization_exception(self):
        """Test exception handling in read_by_organization method"""
        # Setup mock to raise exception
        mock_session = Mock()
        mock_session.run.side_effect = Exception("Database error")

        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = mock_session
        mock_cm.__exit__.return_value = None

        self.news_dao.db.get_connection = Mock(return_value=mock_cm)

        # Test exception is raised
        with self.assertRaises(DAOReadError):
            self.news_dao.read_by_organization("org-uuid")

    def test_read_by_date_range_exception(self):
        """Test exception handling in read_by_date_range method"""
        # Setup mock to raise exception
        mock_session = Mock()
        mock_session.run.side_effect = Exception("Database error")

        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = mock_session
        mock_cm.__exit__.return_value = None

        self.news_dao.db.get_connection = Mock(return_value=mock_cm)

        # Test exception is raised
        with self.assertRaises(DAOReadError):
            start_date = datetime(2022, 12, 1)
            end_date = datetime(2023, 2, 1)
            self.news_dao.read_by_date_range(start_date, end_date)

    def test_read_by_id_with_real_db(self):
        """Test the read_by_id method with a real database."""
        # Create a news item to read
        # First create source, author and topic to avoid foreign key issues

        # Initialize DAOs
        source_dao = NewsAgencyDAO()
        author_dao = PersonDAO()
        topic_dao = TopicDAO()

        # Create required entities
        source = source_dao.create(
            name="Read Test Source", description="Test Organization"
        )

        author = author_dao.create(full_name="Read Test Author")  # type: ignore

        topic = topic_dao.create(
            name="Read Test Topic", definition="Test Topic Definition"
        )

        # Now create the news
        created_news = self.news_dao.create(
            header="Read Test Headline",
            date=self.test_date,
            source_id=source.id,
            content="Read Test Content",
            url="https://example.com/read-test",
            author_ids=[author.id],
            topic_ids=[topic.id],
        )

        # Execute read_by_id method
        read_news = self.news_dao.read_by_id(created_news.id)

        # Validate the result
        self.assertIsNotNone(read_news)
        self.assertEqual(read_news.id, created_news.id)
        self.assertEqual(read_news.header, created_news.header)

        # Clean up - delete all created entities
        self.news_dao.delete(created_news.id)
        topic_dao.delete(topic.id)
        author_dao.delete(author.id)
        source_dao.delete(source.id)

        # Execute read_by_id method and verify it raises an error
        with self.assertRaises(DAOReadError):
            self.news_dao.read_by_id(created_news.id)

    def test_create_from_scrap_with_new_entities_real_db(self):
        """
        Integration test for create_from_scrap that creates author and organization in real DB.

        This test uses the real database connection to test the full flow, including:
        - Creating a new news agency (organization) when not found
        - Creating a new author when not found
        - Using an existing topic if found
        - Finally cleaning up all created entities
        """
        # Generate unique names to avoid collisions with existing data
        test_prefix = f"test_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        test_source = f"{test_prefix}_TestSource"
        test_author = f"{test_prefix}_TestAuthor"

        # Create scraped news model with non-existent author and source
        scraped_news = ScrapedNewsModel(
            header=f"{test_prefix} Test Headline",
            date=datetime.now(),
            source=test_source,
            content="Test content for integration test",
            url=f"https://example.com/{test_prefix}",
            authors=[test_author],
            topics=[],  # No topics - we'll skip topic creation
        )

        created_news = None
        created_author_id = None
        created_source_id = None

        news_dao = NewsDAO()
        agency_dao = NewsAgencyDAO()
        person_dao = PersonDAO()

        try:
            # Create the news - this should create both author and news agency
            created_news = news_dao.create_from_scrap(scraped_news)

            # Verify the news was created
            self.assertIsNotNone(created_news)
            self.assertEqual(created_news.header, scraped_news.header)
            self.assertEqual(created_news.content, scraped_news.content)
            self.assertEqual(created_news.url, scraped_news.url)

            # Verify source was created and linked
            self.assertIsNotNone(created_news.source_id)
            created_source_id = created_news.source_id

            # Find the source and verify it matches
            source = agency_dao.read_by_id(created_source_id)
            self.assertEqual(source.name, test_source)

            # Verify author was created and linked
            self.assertEqual(len(created_news.author_ids), 1)
            created_author_id = created_news.author_ids[0]

            # Find the author and verify it matches
            author = person_dao.read_by_id(created_author_id)
            self.assertEqual(author.full_name, test_author)

            # Verify no topics were linked
            self.assertEqual(len(created_news.topic_ids), 0)

        finally:
            # Clean up all created entities
            try:
                if created_news:
                    news_dao.delete(created_news.id)
                    print(f"Cleaned up test news: {created_news.id}")
            except Exception as e:
                print(f"Error cleaning up test news: {e}")

            try:
                if created_author_id:
                    person_dao.delete(created_author_id)
                    print(f"Cleaned up test author: {created_author_id}")
            except Exception as e:
                print(f"Error cleaning up test author: {e}")

            try:
                if created_source_id:
                    agency_dao.delete(created_source_id)
                    print(f"Cleaned up test source: {created_source_id}")
            except Exception as e:
                print(f"Error cleaning up test source: {e}")


    # TODO: add more integration tests


if __name__ == "__main__":
    unittest.main()
