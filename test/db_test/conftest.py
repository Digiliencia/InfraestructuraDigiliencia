# /tests/db_test/conftest.py
"""
Pytest configuration and fixtures for Direct SQL Database Testing.

This module provides a connection factory using 'psycopg2' to test database
permissions and direct SQL execution.

Updates:
- Adapted to the new single-user architecture.
- All legacy roles (app_user, db_owner) now map to the main POSTGRES_USER.
"""

import pytest
import psycopg2
from digiliencia.configs.fastAPI.core.config import settings as fastapi_settings


# =============================================================================
# PostgreSQL DB Test Data Fixtures
# =============================================================================


@pytest.fixture(scope="session", autouse=True)
def setup_databaseSQL(setup_database):
    """
    Ensures the database is seeded via the main root conftest fixture
    before running any SQL-specific tests.
    """
    yield


# --- Connection Factory Fixture ---
@pytest.fixture(scope="function")
def get_db_connection_for_role():
    """
    Factory fixture to obtain a raw 'psycopg2' connection for a specific role.

    NOTE: In the new simplified architecture, we use a single Database User
    (POSTGRES_USER) which owns the DB. Therefore, 'app_user', 'db_owner',
    and 'superuser' request keys will all return a connection using the
    same master credentials.
    """
    open_connections = []

    def _connect_as_role(role_name: str = fastapi_settings.POSTGRES_USER) -> psycopg2.extensions.connection:
        """
        Creates a connection based on the requested logical role.
        """
        master_user = fastapi_settings.POSTGRES_USER
        master_pass = fastapi_settings.POSTGRES_PASSWORD

        user_creds_map = {
            "diligenciauser": (master_user, master_pass),
        }

        user, password = user_creds_map.get(role_name, (None, None))

        if not user:
            pytest.fail(f"Unknown database role requested: '{role_name}'")

        try:
            # Connect to the Test Database
            conn = psycopg2.connect(
                host=fastapi_settings.POSTGRES_SERVER,
                port=fastapi_settings.POSTGRES_PORT,
                user=user,
                password=password,
                dbname=fastapi_settings.POSTGRES_DB,
                connect_timeout=5,
            )
            open_connections.append(conn)
            return conn
        except Exception as e:
            pytest.fail(f"Could not establish connection for role '{role_name}': {e}")

    yield _connect_as_role

    # Cleanup: Close all connections opened during the test
    for conn in open_connections:
        if not conn.closed:
            conn.close()
