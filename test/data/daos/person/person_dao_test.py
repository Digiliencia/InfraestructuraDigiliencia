import pytest

from digiliencia.data.daos.person.person_dao import PersonDAO
from digiliencia.data.models.person_model import PersonModel
from digiliencia.exc.dao_create_exc import DAOCreateError
from digiliencia.exc.dao_read_exc import DAOReadError


def test_create_person_constraint_error():
    person_dao = PersonDAO()
    # Crear persona con nombre único
    person_dao.create(
        name="John Doe",
        email="john1@example.com",
        description="Test description",
    )
    # Intentar crear otra persona con el mismo nombre (debe violar constraint)
    with pytest.raises(DAOCreateError):
        person_dao.create(
            name="John Doe",
            email="john2@example.com",
            description="Otra descripción",
        )


def test_create_person_no_record():
    person_dao = PersonDAO()
    # La BBDD permite crear persona sin nombre, así que verificamos que se crea sin error
    with pytest.raises(DAOCreateError):
        person_dao.create(
            name=None,  # type: ignore
            email="john@example.com",
            description="Test description",
        )


def test_read_by_id_not_found():
    person_dao = PersonDAO()
    # Buscar un id que no existe
    with pytest.raises(DAOReadError):
        person_dao.read_by_id("non-existent-uuid")


def test_integration_create_read_and_list():
    person_dao = PersonDAO()
    # Crear persona
    created_person = person_dao.create(
        name="Integration Test Person",
        email="integration@test.com",
        description="Integration test description",
    )
    assert isinstance(created_person, PersonModel)
    # Leer persona
    read_person = person_dao.read_by_id(created_person.id)
    assert created_person.id == read_person.id
    assert created_person.name == read_person.name
    assert created_person.email == read_person.email
    assert created_person.description == read_person.description
    # Listar personas
    all_persons = person_dao.read_all()
    assert any(p.id == created_person.id for p in all_persons)
    # Actualizar persona
    updated_person = person_dao.update(
        created_person.id, name="Updated Integration Test Person"
    )
    assert updated_person.name == "Updated Integration Test Person"
    assert updated_person.id == created_person.id
    assert updated_person.email == created_person.email
    assert updated_person.description == created_person.description
    # Leer de nuevo
    read_updated = person_dao.read_by_id(created_person.id)
    assert isinstance(read_updated, PersonModel)
    assert read_updated.name == "Updated Integration Test Person"
    # Eliminar persona
    person_dao.delete(created_person.id)
    # Verificar que ya no existe
    with pytest.raises(DAOReadError):
        person_dao.read_by_id(created_person.id)
    # Verificar que no aparece en la lista
    all_persons_after = person_dao.read_all()
    assert not any(p.id == created_person.id for p in all_persons_after)
