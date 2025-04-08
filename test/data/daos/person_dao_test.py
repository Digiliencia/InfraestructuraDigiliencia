import unittest
from unittest.mock import Mock

from neo4j.exceptions import ConstraintError

from digiliencia.data.daos.person_dao import PersonDAO
from digiliencia.data.models.person_model import PersonModel
from digiliencia.exc.dao_create_exc import DAOCreateError


class TestPersonDAO(unittest.TestCase):
    def setUp(self):
        self.person_dao = PersonDAO()

    def test_build_model_with_complete_data(self):
        mock_node = Mock()
        mock_node.id = "test-uuid"
        node_data = {
            "full_name": "John Doe",
            "email": "john@example.com",
            "description": "Test description",
        }
        mock_node.get = lambda key, default=None: node_data.get(key, default)

        result = self.person_dao._build_model(mock_node)

        self.assertIsInstance(result, PersonModel)
        self.assertEqual(result.id, "test-uuid")
        self.assertEqual(result.full_name, "John Doe")
        self.assertEqual(result.email, "john@example.com")
        self.assertEqual(result.description, "Test description")

    def test_build_model_with_missing_optional_fields(self):
        mock_node = Mock()
        mock_node.id = "test-uuid"
        mock_node.get = lambda key: {"full_name": "Jane Doe"}.get(key)

        result = self.person_dao._build_model(mock_node)

        self.assertIsInstance(result, PersonModel)
        self.assertEqual(result.id, "test-uuid")
        self.assertEqual(result.full_name, "Jane Doe")
        self.assertIsNone(result.email)
        self.assertIsNone(result.description)