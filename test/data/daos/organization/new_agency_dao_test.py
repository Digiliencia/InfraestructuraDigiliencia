import unittest

from digiliencia.data.daos.organization.news_agency_dao import NewsAgencyDAO
from digiliencia.data.models.organization.news_agency_model import NewsAgencyModel
from digiliencia.exc.dao_read_exc import DAOReadError


class TestNewsAgencyDAO(unittest.TestCase):
    def setUp(self):
        self.news_agency_dao = NewsAgencyDAO()

    def test_build_model_with_valid_data(self):
        raw_data = {
            "id": "12345",
            "name": "Test News Agency",
            "description": "A test description for the news agency.",
        }

        model = self.news_agency_dao._build_model(raw_data)

        self.assertIsInstance(model, NewsAgencyModel)
        self.assertEqual(model.id, raw_data["id"])
        self.assertEqual(model.name, raw_data["name"])
        self.assertEqual(model.description, raw_data["description"])

    def test_build_model_with_missing_fields(self):
        raw_data = {
            "id": "12345",
            "name": "Test News Agency",
            # 'description' is missing
        }

        model = self.news_agency_dao._build_model(raw_data)

        self.assertIsInstance(model, NewsAgencyModel)
        self.assertEqual(model.id, raw_data["id"])
        self.assertEqual(model.name, raw_data["name"])
        self.assertIsNone(model.description)

    def test_build_model_with_empty_data(self):
        raw_data = {}

        model = self.news_agency_dao._build_model(raw_data)

        self.assertIsInstance(model, NewsAgencyModel)
        self.assertIsNone(model.id)
        self.assertIsNone(model.name)
        self.assertIsNone(model.description)
        
    def test_integration_create_read_and_list(self):
        # Create new news agency
        created_agency = self.news_agency_dao.create(
            name="Integration Test News Agency",
            description="Integration test description for news agency",
        )

        self.assertIsInstance(created_agency, NewsAgencyModel)

        # Read the news agency back
        read_agency = self.news_agency_dao.read_by_id(created_agency.id)

        # Verify the read news agency matches created news agency
        self.assertEqual(created_agency.id, read_agency.id)
        self.assertEqual(created_agency.name, read_agency.name)
        self.assertEqual(created_agency.description, read_agency.description)

        # Get all news agencies and verify our test agency is in the list
        all_agencies = self.news_agency_dao.read_all()
        self.assertTrue(any(a.id == created_agency.id for a in all_agencies))

        # Update news agency
        updated_agency = self.news_agency_dao.update(
            created_agency.id, name="Updated Integration Test News Agency"
        )

        # Verify update was successful
        self.assertEqual(updated_agency.name, "Updated Integration Test News Agency")
        self.assertEqual(updated_agency.id, created_agency.id)
        self.assertEqual(updated_agency.description, created_agency.description)

        # Read again to confirm persistence
        read_updated = self.news_agency_dao.read_by_id(created_agency.id)
        self.assertIsInstance(read_updated, NewsAgencyModel)
        self.assertEqual(read_updated.name, "Updated Integration Test News Agency")

        # Clean up the created news agency
        self.news_agency_dao.delete(created_agency.id)

        # Test to verify deletion worked correctly
        with self.assertRaises(DAOReadError):
            self.news_agency_dao.read_by_id(created_agency.id)

        # Verify news agency no longer appears in all agencies list
        all_agencies_after = self.news_agency_dao.read_all()
        self.assertFalse(any(a.id == created_agency.id for a in all_agencies_after))


if __name__ == "__main__":
    unittest.main()
