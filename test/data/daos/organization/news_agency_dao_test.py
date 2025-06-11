import pytest

from digiliencia.data.daos.organization.news_agency_dao import NewsAgencyDAO
from digiliencia.data.models.organization.news_agency_model import NewsAgencyModel
from digiliencia.exc.dao_create_exc import DAOCreateError
from digiliencia.exc.dao_read_exc import DAOReadError
from test.data.utils import DummyContextManager


def test_build_model():
    dao = NewsAgencyDAO()
    raw_data = {"id": "agency-uuid", "name": "Test Agency", "description": "desc"}
    model = dao._build_model(raw_data)
    assert isinstance(model, NewsAgencyModel)
    assert model.id == "agency-uuid"
    assert model.name == "Test Agency"
    assert model.description == "desc"


def test_create_news_agency_success():
    dao = NewsAgencyDAO()
    agency = dao.create(name="Agency1", description="desc1")
    assert isinstance(agency, NewsAgencyModel)
    assert agency.name == "Agency1"
    assert agency.description == "desc1"
    # Clean up
    # No delete implemented, so just check creation


def test_create_news_agency_no_record(monkeypatch):
    dao = NewsAgencyDAO()
    monkeypatch.setattr(
        dao.db, "get_connection", lambda *args, **kwargs: DummyContextManager()
    )
    with pytest.raises(DAOCreateError):
        dao.create(name="Agency2", description="desc2")


def test_create_news_agency_exception(monkeypatch):
    dao = NewsAgencyDAO()

    class DummySession:
        def run(self, *args, **kwargs):
            raise Exception("Database error")

    class DummyContext:
        def __enter__(self):
            return DummySession()

        def __exit__(self, exc_type, exc_val, exc_tb):
            return None

    monkeypatch.setattr(
        dao.db, "get_connection", lambda *args, **kwargs: DummyContext()
    )
    with pytest.raises(DAOCreateError):
        dao.create(name="Agency3", description="desc3")


def test_read_all_success():
    dao = NewsAgencyDAO()
    agency = dao.create(name="Agency4", description="desc4")
    agencies = dao.read_all()
    assert any(a.id == agency.id for a in agencies)


def test_read_all_exception(monkeypatch):
    dao = NewsAgencyDAO()

    class DummySession:
        def run(self, *args, **kwargs):
            raise Exception("Database error")

    class DummyContext:
        def __enter__(self):
            return DummySession()

        def __exit__(self, exc_type, exc_val, exc_tb):
            return None

    monkeypatch.setattr(
        dao.db, "get_connection", lambda *args, **kwargs: DummyContext()
    )
    with pytest.raises(DAOReadError):
        dao.read_all()
