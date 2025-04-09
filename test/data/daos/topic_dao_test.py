import unittest
from unittest.mock import MagicMock, Mock

from neo4j.exceptions import ConstraintError

from digiliencia.data.daos.topic_dao import TopicDAO
from digiliencia.data.models.topic_model import TopicModel
from digiliencia.exc.dao_create_exc import DAOCreateError
from digiliencia.exc.dao_read_exc import DAOReadError
from digiliencia.exc.dao_update_exc import DAOUpdateError
from digiliencia.exc.dao_delete_exc import DAODeleteError


class TestTopicDAO(unittest.TestCase):
    _is_parallel = False  # Forzar ejecución secuencial

    def setUp(self):
        self.topic_dao = TopicDAO()

    def test_build_model(self):
        """Test the _build_model method creates a valid TopicModel"""
        raw_data = {
            "id": "test-uuid",
            "name": "Test Topic",
            "definition": "Test Definition"
        }
        
        topic = self.topic_dao._build_model(raw_data)
        
        self.assertIsInstance(topic, TopicModel)
        self.assertEqual(topic.id, "test-uuid")
        self.assertEqual(topic.name, "Test Topic")
        self.assertEqual(topic.definition, "Test Definition")

    def test_create_topic_constraint_error(self):
        """Test that creating a topic with a constraint violation raises correct exception"""
        # Setup mock
        mock_session = Mock()
        mock_session.run.side_effect = ConstraintError("Duplicate constraint")

        # Usar MagicMock para el context manager
        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = mock_session
        mock_cm.__exit__.return_value = None

        self.topic_dao.db.get_connection = Mock(return_value=mock_cm)

        # Test exception is raised
        with self.assertRaises(DAOCreateError):
            self.topic_dao.create(
                name="Test Topic",
                definition="Test definition"
            )

    def test_create_topic_no_record(self):
        """Test create method when no record is returned"""
        # Setup mock with null record
        mock_result = Mock()
        mock_result.single.return_value = None

        mock_session = Mock()
        mock_session.run.return_value = mock_result

        # Usar MagicMock para el context manager
        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = mock_session
        mock_cm.__exit__.return_value = None

        self.topic_dao.db.get_connection = Mock(return_value=mock_cm)

        # Test exception is raised
        with self.assertRaises(DAOCreateError):
            self.topic_dao.create(
                name="Test Topic",
                definition="Test definition"
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

        self.topic_dao.db.get_connection = Mock(return_value=mock_cm)

        # Test exception is raised
        with self.assertRaises(DAOReadError):
            self.topic_dao.read_by_id("non-existent-uuid")

    def test_read_by_name_not_found(self):
        """Test read_by_name method when no record is found"""
        # Setup mock with null record
        mock_result = Mock()
        mock_result.single.return_value = None

        mock_session = Mock()
        mock_session.run.return_value = mock_result

        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = mock_session
        mock_cm.__exit__.return_value = None

        self.topic_dao.db.get_connection = Mock(return_value=mock_cm)

        # Test exception is raised
        with self.assertRaises(DAOReadError):
            self.topic_dao.read_by_name("non-existent-topic")

    def test_read_all_exception(self):
        """Test read_all method when exception occurs"""
        # Setup mock to raise exception
        mock_session = Mock()
        mock_session.run.side_effect = Exception("Database error")

        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = mock_session
        mock_cm.__exit__.return_value = None

        self.topic_dao.db.get_connection = Mock(return_value=mock_cm)

        # Test exception is raised
        with self.assertRaises(DAOReadError):
            self.topic_dao.read_all()

    def test_update_topic_not_found(self):
        """Test update method when no topic is found"""
        # Setup mock with null record
        mock_result = Mock()
        mock_result.single.return_value = None

        mock_session = Mock()
        mock_session.run.return_value = mock_result

        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = mock_session
        mock_cm.__exit__.return_value = None

        self.topic_dao.db.get_connection = Mock(return_value=mock_cm)

        # Test exception is raised
        with self.assertRaises(DAOUpdateError):
            self.topic_dao.update("non-existent-uuid", name="Updated Topic")

    def test_update_topic_exception(self):
        """Test update method when exception occurs"""
        # Setup mock to raise exception
        mock_session = Mock()
        mock_session.run.side_effect = Exception("Database error")

        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = mock_session
        mock_cm.__exit__.return_value = None

        self.topic_dao.db.get_connection = Mock(return_value=mock_cm)

        # Test exception is raised
        with self.assertRaises(DAOUpdateError):
            self.topic_dao.update("some-uuid", name="Updated Topic")

    def test_delete_topic_not_found(self):
        """Test delete method when no topic is found"""
        # Setup mock
        mock_result = Mock()
        mock_consume = Mock()
        mock_consume.counters.nodes_deleted = 0
        mock_result.consume.return_value = mock_consume

        mock_session = Mock()
        mock_session.run.return_value = mock_result

        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = mock_session
        mock_cm.__exit__.return_value = None

        self.topic_dao.db.get_connection = Mock(return_value=mock_cm)

        # Test exception is raised
        with self.assertRaises(DAODeleteError):
            self.topic_dao.delete("non-existent-uuid")

    def test_delete_topic_exception(self):
        """Test delete method when exception occurs"""
        # Setup mock to raise exception
        mock_session = Mock()
        mock_session.run.side_effect = Exception("Database error")

        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = mock_session
        mock_cm.__exit__.return_value = None

        self.topic_dao.db.get_connection = Mock(return_value=mock_cm)

        # Test exception is raised
        with self.assertRaises(DAODeleteError):
            self.topic_dao.delete("some-uuid")

    def test_integration_create_read_and_list(self):
        """
        Integration test for complete CRUD operations on Topic.
        This test creates, reads, updates, and deletes a topic in the actual database.
        """
        # Create new topic
        created_topic = self.topic_dao.create(
            name="Integration Test Topic",
            definition="Integration test definition"
        )

        self.assertIsInstance(created_topic, TopicModel)
        self.assertIsNotNone(created_topic.id)
        self.assertEqual(created_topic.name, "Integration Test Topic")
        self.assertEqual(created_topic.definition, "Integration test definition")

        # Read the topic back by ID
        read_topic = self.topic_dao.read_by_id(created_topic.id)

        # Verify the read topic matches created topic
        self.assertEqual(created_topic.id, read_topic.id)
        self.assertEqual(created_topic.name, read_topic.name)
        self.assertEqual(created_topic.definition, read_topic.definition)

        # Read the topic back by name
        read_topic_by_name = self.topic_dao.read_by_name("Integration Test Topic")
        self.assertEqual(created_topic.id, read_topic_by_name.id)

        # Get all topics and verify our test topic is in the list
        all_topics = self.topic_dao.read_all()
        self.assertTrue(any(t.id == created_topic.id for t in all_topics))

        # Update topic
        updated_topic = self.topic_dao.update(
            created_topic.id, name="Updated Integration Test Topic"
        )

        # Verify update was successful
        self.assertEqual(updated_topic.name, "Updated Integration Test Topic")
        self.assertEqual(updated_topic.id, created_topic.id)
        self.assertEqual(updated_topic.definition, created_topic.definition)

        # Assert that the topic can no longer be found by the old name
        with self.assertRaises(DAOReadError):
            self.topic_dao.read_by_name("Integration Test Topic")

        # Update another field
        updated_topic2 = self.topic_dao.update(
            created_topic.id, definition="Updated integration test definition"
        )

        # Verify second update was successful
        self.assertEqual(updated_topic2.name, "Updated Integration Test Topic")
        self.assertEqual(updated_topic2.definition, "Updated integration test definition")

        # Read again to confirm persistence
        read_updated = self.topic_dao.read_by_id(created_topic.id)
        self.assertIsInstance(read_updated, TopicModel)
        self.assertEqual(read_updated.name, "Updated Integration Test Topic")
        self.assertEqual(read_updated.definition, "Updated integration test definition")

        # Clean up the created topic
        self.topic_dao.delete(created_topic.id)
        
        # Assert the topic cannot be deleted again
        with self.assertRaises(DAODeleteError):
            self.topic_dao.delete(created_topic.id)

        # Test to verify deletion worked correctly
        with self.assertRaises(DAOReadError):
            self.topic_dao.read_by_id(created_topic.id)

        # Verify topic no longer appears in all topics list
        all_topics_after = self.topic_dao.read_all()
        self.assertFalse(any(t.id == created_topic.id for t in all_topics_after))

    def test_integration_multiple_topics(self):
        """
        Integration test for multiple topics.
        Tests creating multiple topics and reading them all back.
        """
        # Create multiple topics
        topic1 = self.topic_dao.create(
            name="Multiple Topic Test 1",
            definition="First test topic for multiple topics test"
        )
        
        topic2 = self.topic_dao.create(
            name="Multiple Topic Test 2",
            definition="Second test topic for multiple topics test"
        )
        
        topic3 = self.topic_dao.create(
            name="Multiple Topic Test 3",
            definition="Third test topic for multiple topics test"
        )
        
        # Get all topics
        all_topics = self.topic_dao.read_all()
        
        # Verify all created topics are in the list
        topic_ids = [t.id for t in all_topics]
        self.assertIn(topic1.id, topic_ids)
        self.assertIn(topic2.id, topic_ids)
        self.assertIn(topic3.id, topic_ids)
        
        # Clean up
        self.topic_dao.delete(topic1.id)
        self.topic_dao.delete(topic2.id)
        self.topic_dao.delete(topic3.id)
        
        # Verify topics were deleted
        all_topics_after = self.topic_dao.read_all()
        topic_ids_after = [t.id for t in all_topics_after]
        self.assertNotIn(topic1.id, topic_ids_after)
        self.assertNotIn(topic2.id, topic_ids_after)
        self.assertNotIn(topic3.id, topic_ids_after)