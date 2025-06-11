import pytest

from digiliencia.data.daos.topic_dao import TopicDAO
from digiliencia.data.models.topic_model import TopicModel
from digiliencia.exc.dao_create_exc import DAOCreateError
from digiliencia.exc.dao_delete_exc import DAODeleteError
from digiliencia.exc.dao_read_exc import DAOReadError
from digiliencia.exc.dao_update_exc import DAOUpdateError


class DummyResult:
    def single(self):
        return None


class DummySession:
    def run(self, *args, **kwargs):
        return DummyResult()


class DummyContextManager:
    def __enter__(self):
        return DummySession()

    def __exit__(self, exc_type, exc_val, exc_tb):
        return None


class TestTopicDAO:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.topic_dao = TopicDAO()

    def test_build_model(self):
        """Test the _build_model method creates a valid TopicModel"""
        raw_data = {
            "id": "test-uuid",
            "name": "Test Topic",
            "definition": "Test Definition",
        }

        topic = self.topic_dao._build_model(raw_data)

        assert isinstance(topic, TopicModel)
        assert topic.id == "test-uuid"
        assert topic.name == "Test Topic"
        assert topic.definition == "Test Definition"

    def test_create_topic_constraint_error(self):
        """Test that creating a topic with a constraint violation raises correct exception"""
        # First create a topic
        self.topic_dao.create(name="Test Topic", definition="Test definition")

        # Attempt to create another topic with the same name
        with pytest.raises(DAOCreateError):
            self.topic_dao.create(name="Test Topic", definition="Different definition")

        # Cleanup
        topic = self.topic_dao.read_by_name("Test Topic")
        self.topic_dao.delete(topic.id)

    def test_create_topic_no_record(self, monkeypatch):
        """Test create method when database fails to return a record"""
        monkeypatch.setattr(
            self.topic_dao.db,
            "get_connection",
            lambda *args, **kwargs: DummyContextManager(),
        )
        with pytest.raises(DAOCreateError):
            self.topic_dao.create(name="Test Topic", definition="Test definition")

    def test_read_by_id_not_found(self, monkeypatch):
        """Test read_by_id method when no record is found"""
        monkeypatch.setattr(
            self.topic_dao.db,
            "get_connection",
            lambda *args, **kwargs: DummyContextManager(),
        )
        with pytest.raises(DAOReadError):
            self.topic_dao.read_by_id("non-existent-uuid")

    def test_read_by_name_not_found(self, monkeypatch):
        """Test read_by_name method when no record is found"""
        monkeypatch.setattr(
            self.topic_dao.db,
            "get_connection",
            lambda *args, **kwargs: DummyContextManager(),
        )
        with pytest.raises(DAOReadError):
            self.topic_dao.read_by_name("non-existent-topic")

    def test_read_all_exception(self, monkeypatch):
        """Test read_all method when exception occurs"""

        class DummySession:
            def run(self, *args, **kwargs):
                raise Exception("Database error")

        monkeypatch.setattr(
            self.topic_dao.db, "get_connection", lambda: DummyContextManager()
        )
        with pytest.raises(DAOReadError):
            self.topic_dao.read_all()

    def test_update_topic_not_found(self, monkeypatch):
        """Test update method when no topic is found"""
        monkeypatch.setattr(
            self.topic_dao.db,
            "get_connection",
            lambda *args, **kwargs: DummyContextManager(),
        )
        with pytest.raises(DAOUpdateError):
            self.topic_dao.update("non-existent-uuid", name="Updated Topic")

    def test_update_topic_exception(self, monkeypatch):
        """Test update method when exception occurs"""

        class DummySession:
            def run(self, *args, **kwargs):
                raise Exception("Database error")

        monkeypatch.setattr(
            self.topic_dao.db, "get_connection", lambda: DummyContextManager()
        )
        with pytest.raises(DAOUpdateError):
            self.topic_dao.update("some-uuid", name="Updated Topic")

    def test_delete_topic_not_found(self, monkeypatch):
        """Test delete method when no topic is found"""

        class DummyResult:
            def consume(self):
                class DummyConsume:
                    counters = type("counters", (), {"nodes_deleted": 0})()

                return DummyConsume()

        monkeypatch.setattr(
            self.topic_dao.db, "get_connection", lambda: DummyContextManager()
        )
        with pytest.raises(DAODeleteError):
            self.topic_dao.delete("non-existent-uuid")

    def test_delete_topic_exception(self, monkeypatch):
        """Test delete method when exception occurs"""

        class DummySession:
            def run(self, *args, **kwargs):
                raise Exception("Database error")

        monkeypatch.setattr(
            self.topic_dao.db, "get_connection", lambda: DummyContextManager()
        )
        with pytest.raises(DAODeleteError):
            self.topic_dao.delete("some-uuid")

    def test_integration_create_read_and_list(self):
        """Integration test for complete CRUD operations on Topic."""
        created_topic = self.topic_dao.create(
            name="Integration Test Topic", definition="Integration test definition"
        )

        assert isinstance(created_topic, TopicModel)
        assert created_topic.id is not None
        assert created_topic.name == "Integration Test Topic"
        assert created_topic.definition == "Integration test definition"

        read_topic = self.topic_dao.read_by_id(created_topic.id)
        assert created_topic.id == read_topic.id
        assert created_topic.name == read_topic.name
        assert created_topic.definition == read_topic.definition

        read_topic_by_name = self.topic_dao.read_by_name("Integration Test Topic")
        assert created_topic.id == read_topic_by_name.id

        all_topics = self.topic_dao.read_all()
        assert any(t.id == created_topic.id for t in all_topics)

        updated_topic = self.topic_dao.update(
            created_topic.id, name="Updated Integration Test Topic"
        )

        assert updated_topic.name == "Updated Integration Test Topic"
        assert updated_topic.id == created_topic.id
        assert updated_topic.definition == created_topic.definition

        with pytest.raises(DAOReadError):
            self.topic_dao.read_by_name("Integration Test Topic")

        updated_topic2 = self.topic_dao.update(
            created_topic.id, definition="Updated integration test definition"
        )

        assert updated_topic2.name == "Updated Integration Test Topic"
        assert updated_topic2.definition == "Updated integration test definition"

        read_updated = self.topic_dao.read_by_id(created_topic.id)
        assert isinstance(read_updated, TopicModel)
        assert read_updated.name == "Updated Integration Test Topic"
        assert read_updated.definition == "Updated integration test definition"

        self.topic_dao.delete(created_topic.id)

        with pytest.raises(DAODeleteError):
            self.topic_dao.delete(created_topic.id)

        with pytest.raises(DAOReadError):
            self.topic_dao.read_by_id(created_topic.id)

        all_topics_after = self.topic_dao.read_all()
        assert not any(t.id == created_topic.id for t in all_topics_after)

    def test_integration_multiple_topics(self):
        """Integration test for multiple topics."""
        topic1 = self.topic_dao.create(
            name="Multiple Topic Test 1",
            definition="First test topic for multiple topics test",
        )

        topic2 = self.topic_dao.create(
            name="Multiple Topic Test 2",
            definition="Second test topic for multiple topics test",
        )

        topic3 = self.topic_dao.create(
            name="Multiple Topic Test 3",
            definition="Third test topic for multiple topics test",
        )

        all_topics = self.topic_dao.read_all()
        topic_ids = [t.id for t in all_topics]

        assert topic1.id in topic_ids
        assert topic2.id in topic_ids
        assert topic3.id in topic_ids

        self.topic_dao.delete(topic1.id)
        self.topic_dao.delete(topic2.id)
        self.topic_dao.delete(topic3.id)

        all_topics_after = self.topic_dao.read_all()
        topic_ids_after = [t.id for t in all_topics_after]

        assert topic1.id not in topic_ids_after
        assert topic2.id not in topic_ids_after
        assert topic3.id not in topic_ids_after
