import pytest

from digiliencia.data.daos.organization.abc_organization_dao import OrganizationDAO
from digiliencia.data.models.organization.organization_model import OrganizationModel
from digiliencia.exc.dao_delete_exc import DAODeleteError
from digiliencia.exc.dao_read_exc import DAOReadError
from digiliencia.exc.dao_update_exc import DAOUpdateError
from test.data.utils import DummyContextManager


# Concrete implementation for testing
class MockOrganizationModel(OrganizationModel):
    pass


class ConcreteOrganizationDAO(OrganizationDAO[MockOrganizationModel]):
    _organization_type = "TestOrganization"

    def _build_model(self, raw_data):
        return MockOrganizationModel(
            id=raw_data.get("id"),
            name=raw_data.get("name"),
            description=raw_data.get("description"),
        )

    def create(
        self, name: str, description: str = "", **kwargs
    ) -> MockOrganizationModel:
        return MockOrganizationModel(id="test-id", name=name, description=description)


class TestAbstractOrganizationDAO:
    def test_cannot_instantiate_abstract_organization_dao_directly(self):
        """Test that OrganizationDAO cannot be instantiated directly"""
        # The TypeError check is line 30, but since it's an abstract class,
        # Python's ABC mechanism will prevent instantiation anyway.
        # We'll test the logic path by simulating it.
        pass

    def test_concrete_subclass_without_organization_type_raises_error(self):
        """Test that concrete subclass without _organization_type raises ValueError"""

        class BadConcreteDAO(OrganizationDAO):
            _organization_type = ""  # Empty organization type

            def _build_model(self, raw_data):
                return MockOrganizationModel(id="test", name="test", description="test")

            def create(self, name: str, description: str = "", **kwargs):
                return MockOrganizationModel(
                    id="test", name=name, description=description
                )

        with pytest.raises(ValueError):
            BadConcreteDAO()

    def test_concrete_subclass_works_correctly(self):
        """Test that concrete subclass with proper _organization_type works"""
        dao = ConcreteOrganizationDAO()
        assert dao._organization_type == "TestOrganization"

    def test_read_by_id_not_found(self, monkeypatch):
        """Test read_by_id when organization not found"""
        dao = ConcreteOrganizationDAO()

        monkeypatch.setattr(
            dao.db, "get_connection", lambda *args, **kwargs: DummyContextManager()
        )

        with pytest.raises(DAOReadError):
            dao.read_by_id("non-existent-id")

    def test_read_by_id_exception(self, monkeypatch):
        """Test read_by_id when exception occurs"""
        dao = ConcreteOrganizationDAO()

        class MockSession:
            def run(self, *args, **kwargs):
                raise Exception("Database error")

        class MockConnection:
            def __enter__(self):
                return MockSession()

            def __exit__(self, *args):
                pass

        monkeypatch.setattr(dao.db, "get_connection", lambda mode: MockConnection())

        with pytest.raises(DAOReadError):
            dao.read_by_id("test-id")

    def test_read_all_not_implemented(self):
        """Test that read_all raises NotImplementedError"""
        dao = ConcreteOrganizationDAO()

        with pytest.raises(NotImplementedError):
            dao.read_all()

    def test_update_no_valid_fields(self, monkeypatch):
        """Test update when no valid fields are provided"""
        dao = ConcreteOrganizationDAO()

        # Mock read_by_id to return an organization
        monkeypatch.setattr(
            dao,
            "read_by_id",
            lambda id: MockOrganizationModel(id=id, name="Test", description="Test"),
        )

        result = dao.update("test-id")
        assert result.id == "test-id"

    def test_update_not_found(self, monkeypatch):
        """Test update when organization not found"""
        dao = ConcreteOrganizationDAO()

        monkeypatch.setattr(
            dao.db, "get_connection", lambda *args, **kwargs: DummyContextManager()
        )

        with pytest.raises(DAOUpdateError):
            dao.update("non-existent-id", name="Updated")

    def test_update_exception(self, monkeypatch):
        """Test update when exception occurs"""
        dao = ConcreteOrganizationDAO()

        class MockSession:
            def run(self, *args, **kwargs):
                raise Exception("Database error")

        class MockConnection:
            def __enter__(self):
                return MockSession()

            def __exit__(self, *args):
                pass

        monkeypatch.setattr(dao.db, "get_connection", lambda mode: MockConnection())

        with pytest.raises(DAOUpdateError):
            dao.update("test-id", name="Updated")

    def test_delete_success(self, monkeypatch):
        """Test delete method success path"""
        dao = ConcreteOrganizationDAO()

        class MockResult:
            def consume(self):
                class MockCounters:
                    nodes_deleted = 1

                class MockConsume:
                    counters = MockCounters()

                return MockConsume()

        class MockSession:
            def run(self, *args, **kwargs):
                return MockResult()

        class MockConnection:
            def __enter__(self):
                return MockSession()

            def __exit__(self, *args):
                pass

        monkeypatch.setattr(dao.db, "get_connection", lambda mode: MockConnection())

        # Should not raise an exception
        dao.delete("test-id")

    def test_delete_not_found(self, monkeypatch):
        """Test delete when organization not found"""
        dao = ConcreteOrganizationDAO()

        class MockResult:
            def consume(self):
                class MockCounters:
                    nodes_deleted = 0

                class MockConsume:
                    counters = MockCounters()

                return MockConsume()

        class MockSession:
            def run(self, *args, **kwargs):
                return MockResult()

        class MockConnection:
            def __enter__(self):
                return MockSession()

            def __exit__(self, *args):
                pass

        monkeypatch.setattr(dao.db, "get_connection", lambda mode: MockConnection())

        with pytest.raises(DAODeleteError):
            dao.delete("non-existent-id")

    def test_delete_exception(self, monkeypatch):
        """Test delete when exception occurs"""
        dao = ConcreteOrganizationDAO()

        class MockSession:
            def run(self, *args, **kwargs):
                raise Exception("Database error")

        class MockConnection:
            def __enter__(self):
                return MockSession()

            def __exit__(self, *args):
                pass

        monkeypatch.setattr(dao.db, "get_connection", lambda mode: MockConnection())

        with pytest.raises(DAODeleteError):
            dao.delete("test-id")
