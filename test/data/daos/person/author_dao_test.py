import pytest

from digiliencia.data.daos.person.author_dao import AuthorDAO
from digiliencia.data.models.author_model import RawAuthorModel
from digiliencia.exc.dao_create_exc import DAOCreateError
from digiliencia.exc.dao_delete_exc import DAODeleteError
from digiliencia.exc.dao_read_exc import DAOReadError
from digiliencia.exc.dao_update_exc import DAOUpdateError
from test.data.utils import DummyContextManager


class TestAuthorDAO:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.author_dao = AuthorDAO()

    def test_build_model(self):
        raw_data = {
            "id": "author-uuid",
            "name": "John Doe",
            "email": "john@example.com",
            "description": "Author description",
            "news": ["news1", "news2"],
        }
        author = self.author_dao._build_model(raw_data)
        assert isinstance(author, RawAuthorModel)
        assert author.id == "author-uuid"
        assert author.name == "John Doe"
        assert author.email == "john@example.com"
        assert author.description == "Author description"
        assert author.news_ids == ["news1", "news2"]

    def test_create_author_constraint_error(self):
        self.author_dao.create(
            name="John Doe", email="john@example.com", description="desc"
        )
        with pytest.raises(DAOCreateError):
            self.author_dao.create(
                name="John Doe", email="john@example.com", description="desc"
            )
        author = self.author_dao.read_all()[0]
        self.author_dao.delete(author.id)

    def test_create_author_no_name(self):
        with pytest.raises(DAOCreateError, match="Name is required"):
            self.author_dao.create(name="")

    def test_create_author_no_record(self, monkeypatch):
        monkeypatch.setattr(
            self.author_dao.db,
            "get_connection",
            lambda *args, **kwargs: DummyContextManager(),
        )
        with pytest.raises(DAOCreateError):
            self.author_dao.create(name="Jane Doe")

    def test_read_by_id_not_found(self, monkeypatch):
        monkeypatch.setattr(
            self.author_dao.db,
            "get_connection",
            lambda *args, **kwargs: DummyContextManager(),
        )
        with pytest.raises(DAOReadError):
            self.author_dao.read_by_id("non-existent-uuid")

    def test_read_all_exception(self, monkeypatch):
        class DummySession:
            def run(self, *args, **kwargs):
                raise Exception("Database error")

        monkeypatch.setattr(
            self.author_dao.db, "get_connection", lambda: DummyContextManager()
        )
        with pytest.raises(DAOReadError):
            self.author_dao.read_all()

    def test_update_author_not_found(self, monkeypatch):
        monkeypatch.setattr(
            self.author_dao.db,
            "get_connection",
            lambda *args, **kwargs: DummyContextManager(),
        )
        with pytest.raises(DAOUpdateError):
            self.author_dao.update("non-existent-uuid", name="Updated Name")

    def test_update_author_exception(self, monkeypatch):
        class DummySession:
            def run(self, *args, **kwargs):
                raise Exception("Database error")

        monkeypatch.setattr(
            self.author_dao.db, "get_connection", lambda: DummyContextManager()
        )
        with pytest.raises(DAOUpdateError):
            self.author_dao.update("some-uuid", name="Updated Name")

    def test_update_no_valid_fields(self, monkeypatch):
        author = self.author_dao.create(name="No Update Author")
        called = {}
        original_read_by_id = self.author_dao.read_by_id

        def fake_read_by_id(id):
            called["called"] = True
            return original_read_by_id(id)

        monkeypatch.setattr(self.author_dao, "read_by_id", fake_read_by_id)
        result = self.author_dao.update(author.id)
        assert result.id == author.id
        assert called.get("called")
        called.clear()
        result2 = self.author_dao.update(
            author.id, name=None, email=None, description=None
        )
        assert result2.id == author.id
        assert called.get("called")
        self.author_dao.delete(author.id)

    def test_delete_author_not_found(self, monkeypatch):
        class DummyResult:
            def consume(self):
                class DummyConsume:
                    counters = type("counters", (), {"nodes_deleted": 0})()

                return DummyConsume()

        monkeypatch.setattr(
            self.author_dao.db, "get_connection", lambda: DummyContextManager()
        )
        with pytest.raises(DAODeleteError):
            self.author_dao.delete("non-existent-uuid")

    def test_delete_author_exception(self, monkeypatch):
        class DummySession:
            def run(self, *args, **kwargs):
                raise Exception("Database error")

        monkeypatch.setattr(
            self.author_dao.db, "get_connection", lambda: DummyContextManager()
        )
        with pytest.raises(DAODeleteError):
            self.author_dao.delete("some-uuid")

    def test_integration_create_read_and_list(self):
        created_author = self.author_dao.create(
            name="Integration Test Author",
            email="integration@example.com",
            description="desc",
        )
        assert isinstance(created_author, RawAuthorModel)
        assert created_author.id is not None
        assert created_author.name == "Integration Test Author"
        assert created_author.email == "integration@example.com"
        assert created_author.description == "desc"
        assert created_author.news_ids == []
        read_author = self.author_dao.read_by_id(created_author.id)
        assert created_author.id == read_author.id
        assert created_author.name == read_author.name
        assert created_author.email == read_author.email
        assert created_author.description == read_author.description
        all_authors = self.author_dao.read_all()
        assert any(a.id == created_author.id for a in all_authors)
        updated_author = self.author_dao.update(
            created_author.id, name="Updated Integration Test Author"
        )
        assert updated_author.name == "Updated Integration Test Author"
        assert updated_author.id == created_author.id
        assert updated_author.email == created_author.email
        assert updated_author.description == created_author.description
        updated_author2 = self.author_dao.update(
            created_author.id, email="updated@example.com", description="updated desc"
        )
        assert updated_author2.email == "updated@example.com"
        assert updated_author2.description == "updated desc"
        read_updated = self.author_dao.read_by_id(created_author.id)
        assert isinstance(read_updated, RawAuthorModel)
        assert read_updated.name == "Updated Integration Test Author"
        assert read_updated.email == "updated@example.com"
        assert read_updated.description == "updated desc"
        self.author_dao.delete(created_author.id)
        with pytest.raises(DAODeleteError):
            self.author_dao.delete(created_author.id)
        with pytest.raises(DAOReadError):
            self.author_dao.read_by_id(created_author.id)
        all_authors_after = self.author_dao.read_all()
        assert not any(a.id == created_author.id for a in all_authors_after)

    def test_integration_multiple_authors(self):
        author1 = self.author_dao.create(
            name="Multiple Author Test 1", email="a1@example.com", description="desc1"
        )
        author2 = self.author_dao.create(
            name="Multiple Author Test 2", email="a2@example.com", description="desc2"
        )
        author3 = self.author_dao.create(
            name="Multiple Author Test 3", email="a3@example.com", description="desc3"
        )
        all_authors = self.author_dao.read_all()
        author_ids = [a.id for a in all_authors]
        assert author1.id in author_ids
        assert author2.id in author_ids
        assert author3.id in author_ids
        self.author_dao.delete(author1.id)
        self.author_dao.delete(author2.id)
        self.author_dao.delete(author3.id)
        all_authors_after = self.author_dao.read_all()
        author_ids_after = [a.id for a in all_authors_after]
        assert author1.id not in author_ids_after
        assert author2.id not in author_ids_after
        assert author3.id not in author_ids_after
