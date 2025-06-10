import pytest

from digiliencia.data.daos.organization.news_agency_dao import NewsAgencyDAO
from digiliencia.data.models.organization.news_agency_model import NewsAgencyModel
from digiliencia.exc.dao_read_exc import DAOReadError


@pytest.fixture
def news_agency_dao():
    return NewsAgencyDAO()


def test_build_model_with_valid_data(news_agency_dao):
    raw_data = {
        "id": "12345",
        "name": "Test News Agency",
        "description": "A test description for the news agency.",
    }
    model = news_agency_dao._build_model(raw_data)
    assert isinstance(model, NewsAgencyModel)
    assert model.id == raw_data["id"]
    assert model.name == raw_data["name"]
    assert model.description == raw_data["description"]


def test_build_model_with_missing_fields(news_agency_dao):
    raw_data = {
        "id": "12345",
        "name": "Test News Agency",
        # 'description' is missing
    }
    model = news_agency_dao._build_model(raw_data)
    assert isinstance(model, NewsAgencyModel)
    assert model.id == raw_data["id"]
    assert model.name == raw_data["name"]
    assert model.description is None


def test_build_model_with_empty_data(news_agency_dao):
    raw_data = {}
    model = news_agency_dao._build_model(raw_data)
    assert isinstance(model, NewsAgencyModel)
    assert model.id is None
    assert model.name is None
    assert model.description is None


def test_integration_create_read_and_list(news_agency_dao):
    # Crear agencia
    created_agency = news_agency_dao.create(
        name="Integration Test News Agency",
        description="Integration test description for news agency",
    )
    assert isinstance(created_agency, NewsAgencyModel)

    # Leer la agencia
    read_agency = news_agency_dao.read_by_id(created_agency.id)
    assert created_agency.id == read_agency.id
    assert created_agency.name == read_agency.name
    assert created_agency.description == read_agency.description

    # Listar agencias
    all_agencies = news_agency_dao.read_all()
    assert any(a.id == created_agency.id for a in all_agencies)

    # Actualizar agencia
    updated_agency = news_agency_dao.update(
        created_agency.id, name="Updated Integration Test News Agency"
    )
    assert updated_agency.name == "Updated Integration Test News Agency"
    assert updated_agency.id == created_agency.id
    assert updated_agency.description == created_agency.description

    # Leer de nuevo
    read_updated = news_agency_dao.read_by_id(created_agency.id)
    assert isinstance(read_updated, NewsAgencyModel)
    assert read_updated.name == "Updated Integration Test News Agency"

    # Eliminar agencia
    news_agency_dao.delete(created_agency.id)

    with pytest.raises(DAOReadError):
        news_agency_dao.read_by_id(created_agency.id)

    # Comprobar que no aparece en la lista
    all_agencies_after = news_agency_dao.read_all()
    assert not any(a.id == created_agency.id for a in all_agencies_after)
