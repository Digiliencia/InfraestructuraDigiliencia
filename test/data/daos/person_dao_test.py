import unittest
from unittest.mock import MagicMock, Mock

from neo4j.exceptions import ConstraintError

from digiliencia.data.daos.person_dao import PersonDAO
from digiliencia.data.models.person_model import PersonModel
from digiliencia.exc.dao_create_exc import DAOCreateError
from digiliencia.exc.dao_read_exc import DAOReadError


class TestPersonDAO(unittest.TestCase):
    _is_parallel = False  # Forzar ejecución secuencial

    def setUp(self):
        self.person_dao = PersonDAO()

    def test_create_person_constraint_error(self):
        # Setup mock
        mock_session = Mock()
        mock_session.run.side_effect = ConstraintError("Duplicate constraint")

        # Usar MagicMock para el context manager
        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = mock_session
        mock_cm.__exit__.return_value = None

        self.person_dao.db.get_connection = Mock(return_value=mock_cm)

        # Test exception is raised
        with self.assertRaises(DAOCreateError):
            self.person_dao.create(
                full_name="John Doe",
                email="john@example.com",
                description="Test description",
            )

    def test_create_person_no_record(self):
        # Setup mock with null record
        mock_result = Mock()
        mock_result.single.return_value = None

        mock_session = Mock()
        mock_session.run.return_value = mock_result

        # Usar MagicMock para el context manager
        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = mock_session
        mock_cm.__exit__.return_value = None

        self.person_dao.db.get_connection = Mock(return_value=mock_cm)

        # Test exception is raised
        with self.assertRaises(DAOCreateError):
            self.person_dao.create(
                full_name="John Doe",
                email="john@example.com",
                description="Test description",
            )

    def test_read_by_id_not_found(self):
        # Setup mock with null record
        mock_result = Mock()
        mock_result.single.return_value = None

        mock_session = Mock()
        mock_session.run.return_value = mock_result

        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = mock_session
        mock_cm.__exit__.return_value = None

        self.person_dao.db.get_connection = Mock(return_value=mock_cm)

        # Test exception is raised
        with self.assertRaises(DAOReadError):
            self.person_dao.read_by_id("non-existent-uuid")

    def test_integration_create_read_and_list(self):
        # Create new person
        created_person = self.person_dao.create(
            full_name="Integration Test Person",
            email="integration@test.com",
            description="Integration test description",
        )

        self.assertIsInstance(created_person, PersonModel)

        # Read the person back
        read_person = self.person_dao.read_by_id(created_person.id)

        # Verify the read person matches created person
        self.assertEqual(created_person.id, read_person.id)
        self.assertEqual(created_person.full_name, read_person.full_name)
        self.assertEqual(created_person.email, read_person.email)
        self.assertEqual(created_person.description, read_person.description)

        # Get all persons and verify our test person is in the list
        all_persons = self.person_dao.read_all()
        self.assertTrue(any(p.id == created_person.id for p in all_persons))

        # Update person
        updated_person = self.person_dao.update(
            created_person.id, full_name="Updated Integration Test Person"
        )

        # Verify update was successful
        self.assertEqual(updated_person.full_name, "Updated Integration Test Person")
        self.assertEqual(updated_person.id, created_person.id)
        self.assertEqual(updated_person.email, created_person.email)
        self.assertEqual(updated_person.description, created_person.description)

        # Read again to confirm persistence
        read_updated = self.person_dao.read_by_id(created_person.id)
        self.assertIsInstance(read_updated, PersonModel)
        self.assertEqual(read_updated.full_name, "Updated Integration Test Person")

        # Clean up the created person
        self.person_dao.delete(created_person.id)

        # Test to verify deletion worked correctly
        with self.assertRaises(DAOReadError):
            self.person_dao.read_by_id(created_person.id)

        # Verify person no longer appears in all persons list
        all_persons_after = self.person_dao.read_all()
        self.assertFalse(any(p.id == created_person.id for p in all_persons_after))
