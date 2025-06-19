import pytest

from digiliencia.data.daos.organization.public_organization_dao import (
    PublicOrganizationDAO,
)
from digiliencia.data.models.organization.public_organization_model import (
    PublicOrganizationModel,
)
from digiliencia.exc.dao_create_exc import DAOCreateError
from digiliencia.exc.dao_read_exc import DAOReadError
from test.data.utils import DummyContextManager


class TestPublicOrganizationDAO:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.public_org_dao = PublicOrganizationDAO()

    def test_build_model(self):
        """Test the _build_model method creates a valid PublicOrganizationModel"""
        raw_data = {
            "id": "test-uuid",
            "name": "Test Public Org",
            "description": "Test Description",
        }

        public_org = self.public_org_dao._build_model(raw_data)

        assert isinstance(public_org, PublicOrganizationModel)
        assert public_org.id == "test-uuid"
        assert public_org.name == "Test Public Org"
        assert public_org.description == "Test Description"

    def test_create_public_organization_empty_name(self):
        """Test that creating a public organization with an empty name raises DAOCreateError."""
        with pytest.raises(
            DAOCreateError, match="Name is required to create a public organization"
        ):
            self.public_org_dao.create(name="", description="Should fail")

    def test_create_public_organization_no_record(self, monkeypatch):
        """Test create method when database fails to return a record"""
        monkeypatch.setattr(
            self.public_org_dao.db,
            "get_connection",
            lambda *args, **kwargs: DummyContextManager(),
        )
        with pytest.raises(DAOCreateError):
            self.public_org_dao.create(
                name="Test Public Org", description="Test description"
            )

    def test_create_public_organization_exception(self, monkeypatch):
        """Test create method when exception occurs"""

        class DummySession:
            def run(self, *args, **kwargs):
                raise Exception("Database error")

        monkeypatch.setattr(
            self.public_org_dao.db, "get_connection", lambda: DummyContextManager()
        )
        with pytest.raises(DAOCreateError):
            self.public_org_dao.create(
                name="Test Public Org", description="Test description"
            )

    def test_read_all_success(self):
        """Test read_all method success path"""
        public_orgs = self.public_org_dao.read_all()
        assert isinstance(public_orgs, list)

    def test_read_all_exception(self, monkeypatch):
        """Test read_all method when exception occurs"""

        class DummySession:
            def run(self, *args, **kwargs):
                raise Exception("Database error")

        monkeypatch.setattr(
            self.public_org_dao.db, "get_connection", lambda: DummyContextManager()
        )
        with pytest.raises(DAOReadError):
            self.public_org_dao.read_all()

    def test_integration_create_read_and_list(self):
        """Integration test for complete CRUD operations on PublicOrganization."""
        created_org = self.public_org_dao.create(
            name="Integration Test Public Org",
            description="Integration test description",
        )

        assert isinstance(created_org, PublicOrganizationModel)
        assert created_org.id is not None
        assert created_org.name == "Integration Test Public Org"
        assert created_org.description == "Integration test description"

        read_org = self.public_org_dao.read_by_id(created_org.id)
        assert created_org.id == read_org.id
        assert created_org.name == read_org.name
        assert created_org.description == read_org.description

        all_orgs = self.public_org_dao.read_all()
        assert any(o.id == created_org.id for o in all_orgs)

        updated_org = self.public_org_dao.update(
            created_org.id, name="Updated Integration Test Public Org"
        )

        assert updated_org.name == "Updated Integration Test Public Org"
        assert updated_org.id == created_org.id
        assert updated_org.description == created_org.description

        self.public_org_dao.delete(created_org.id)

        with pytest.raises(DAOReadError):
            self.public_org_dao.read_by_id(created_org.id)

        all_orgs_after = self.public_org_dao.read_all()
        assert not any(o.id == created_org.id for o in all_orgs_after)
