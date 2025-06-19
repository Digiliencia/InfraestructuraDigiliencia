from digiliencia.data.daos.abc_dao import AbstractDAO
from digiliencia.data.models.interface_model import IModel


# Concrete implementation for testing
class MockModel(IModel):
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name


class ConcreteDAO(AbstractDAO):
    def _build_model(self, raw_data):
        return MockModel(id=raw_data.get("id"), name=raw_data.get("name"))

    def create(self, **kwargs):
        # Create doesn't return anything in the abstract base
        pass

    def read_by_id(self, id: str):
        return MockModel(id=id, name="test")

    def read_all(self):
        return [MockModel(id="1", name="test1"), MockModel(id="2", name="test2")]

    def update(self, id: str, **kwargs):
        # Update doesn't return anything in the abstract base
        pass

    def delete(self, id: str):
        pass


class TestAbstractDAO:
    def test_concrete_dao_can_be_instantiated(self):
        """Test that concrete DAO implementation can be instantiated"""
        dao = ConcreteDAO()
        assert dao is not None
        assert hasattr(dao, "db")

    def test_concrete_dao_methods_work(self):
        """Test that concrete DAO methods work correctly"""
        dao = ConcreteDAO()

        # Test _build_model
        raw_data = {"id": "test-id", "name": "test-name"}
        result = dao._build_model(raw_data)
        assert isinstance(result, MockModel)
        assert result.id == "test-id"
        assert result.name == "test-name"

        # Test read_by_id
        result = dao.read_by_id("123")
        assert isinstance(result, MockModel)
        assert result.id == "123"

        # Test read_all
        results = dao.read_all()
        assert isinstance(results, list)
        assert len(results) == 2

        # Test create (should not raise exception)
        dao.create()

        # Test update (should not raise exception)
        dao.update("123", name="updated")

        # Test delete (should not raise exception)
        dao.delete("123")
