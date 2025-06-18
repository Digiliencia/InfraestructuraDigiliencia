import pytest

from digiliencia.data.daos.person.person_dao import PersonDAO
from digiliencia.data.models.person_model import PersonModel
from digiliencia.exc.dao_create_exc import DAOCreateError
from digiliencia.exc.dao_delete_exc import DAODeleteError
from digiliencia.exc.dao_read_exc import DAOReadError
from digiliencia.exc.dao_update_exc import DAOUpdateError
from test.data.utils import DummyContextManager


def test_create_person_constraint_error():
    person_dao = PersonDAO()
    # Create a person with a unique name
    person_dao.create(
        name="John Doe",
        email="john1@example.com",
        description="Test description",
    )
    # Try to create another person with the same name (should violate constraint)
    with pytest.raises(DAOCreateError):
        person_dao.create(
            name="John Doe",
            email="john2@example.com",
            description="Another description",
        )


def test_create_person_no_name():
    person_dao = PersonDAO()
    with pytest.raises(DAOCreateError, match="Name is required"):
        person_dao.create(name="")


def test_create_person_no_record(monkeypatch):
    person_dao = PersonDAO()
    monkeypatch.setattr(
        person_dao.db,
        "get_connection",
        lambda *args, **kwargs: DummyContextManager(),
    )
    with pytest.raises(DAOCreateError):
        person_dao.create(name="Jane Doe")


def test_read_by_id_not_found():
    person_dao = PersonDAO()
    # Search for an id that does not exist
    with pytest.raises(DAOReadError):
        person_dao.read_by_id("non-existent-uuid")


def test_read_by_id_not_found_db(monkeypatch):
    person_dao = PersonDAO()
    monkeypatch.setattr(
        person_dao.db,
        "get_connection",
        lambda *args, **kwargs: DummyContextManager(),
    )
    with pytest.raises(DAOReadError):
        person_dao.read_by_id("non-existent-uuid")


def test_read_all_exception(monkeypatch):
    person_dao = PersonDAO()
    monkeypatch.setattr(person_dao.db, "get_connection", lambda: DummyContextManager())
    with pytest.raises(DAOReadError):
        person_dao.read_all()


def test_integration_create_read_and_list():
    person_dao = PersonDAO()
    # Create person
    created_person = person_dao.create(
        name="Integration Test Person",
        email="integration@test.com",
        description="Integration test description",
    )
    assert isinstance(created_person, PersonModel)
    # Read person
    read_person = person_dao.read_by_id(created_person.id)
    assert created_person.id == read_person.id
    assert created_person.name == read_person.name
    assert created_person.email == read_person.email
    assert created_person.description == read_person.description
    # List persons
    all_persons = person_dao.read_all()
    assert any(p.id == created_person.id for p in all_persons)
    # Update person
    updated_person = person_dao.update(
        created_person.id, name="Updated Integration Test Person"
    )
    assert updated_person.name == "Updated Integration Test Person"
    assert updated_person.id == created_person.id
    assert updated_person.email == created_person.email
    assert updated_person.description == created_person.description
    # Read again
    read_updated = person_dao.read_by_id(created_person.id)
    assert isinstance(read_updated, PersonModel)
    assert read_updated.name == "Updated Integration Test Person"
    # Delete person
    person_dao.delete(created_person.id)
    # Verify it no longer exists
    with pytest.raises(DAOReadError):
        person_dao.read_by_id(created_person.id)
    # Verify it does not appear in the list
    all_persons_after = person_dao.read_all()
    assert not any(p.id == created_person.id for p in all_persons_after)


def test_update_person_not_found(monkeypatch):
    person_dao = PersonDAO()
    monkeypatch.setattr(
        person_dao.db,
        "get_connection",
        lambda *args, **kwargs: DummyContextManager(),
    )
    with pytest.raises(DAOUpdateError):
        person_dao.update("non-existent-uuid", name="Updated Name")


def test_update_person_exception(monkeypatch):
    person_dao = PersonDAO()
    monkeypatch.setattr(person_dao.db, "get_connection", lambda: DummyContextManager())
    with pytest.raises(DAOUpdateError):
        person_dao.update("some-uuid", name="Updated Name")


def test_update_no_valid_fields(monkeypatch):
    person_dao = PersonDAO()
    person = person_dao.create(name="No Update Person")
    called = {}

    def fake_read_by_id(id):
        called["called"] = True
        return original_read_by_id(id)

    original_read_by_id = person_dao.read_by_id
    monkeypatch.setattr(person_dao, "read_by_id", fake_read_by_id)
    result = person_dao.update(person.id)
    assert result.id == person.id
    assert called.get("called")
    called.clear()
    result2 = person_dao.update(person.id, name=None, email=None, description=None)
    assert result2.id == person.id
    assert called.get("called")
    person_dao.delete(person.id)


def test_delete_person_not_found(monkeypatch):
    person_dao = PersonDAO()
    monkeypatch.setattr(person_dao.db, "get_connection", lambda: DummyContextManager())
    with pytest.raises(DAODeleteError):
        person_dao.delete("non-existent-uuid")


def test_delete_person_exception(monkeypatch):
    person_dao = PersonDAO()
    monkeypatch.setattr(person_dao.db, "get_connection", lambda: DummyContextManager())
    with pytest.raises(DAODeleteError):
        person_dao.delete("some-uuid")


def test_delete_person_not_found_integration():
    person_dao = PersonDAO()
    # Delete an id that does not really exist in the DB
    with pytest.raises(DAODeleteError):
        person_dao.delete("non-existent-uuid-9999")


def test_build_model():
    person_dao = PersonDAO()
    raw_data = {
        "id": "person-uuid",
        "name": "Jane Doe",
        "email": "jane@example.com",
        "description": "A person desc",
    }
    person = person_dao._build_model(raw_data)
    assert isinstance(person, PersonModel)
    assert person.id == "person-uuid"
    assert person.name == "Jane Doe"
    assert person.email == "jane@example.com"
    assert person.description == "A person desc"
