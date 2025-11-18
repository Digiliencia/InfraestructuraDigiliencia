# /tests/db_test/conftest.py
import pytest
import psycopg2
from digiliencia.configs.fastAPI.core.config import settings as fastapi_settings


# =============================================================================
# PostgreSQL DB Test Data Fixtures
# =============================================================================


@pytest.fixture(scope="session", autouse=True)
def setup_databaseSQL(setup_database):
    yield


# --- Connection Factory Fixture ---
@pytest.fixture(scope="function")
def get_db_connection_for_role():
    """Factory to get a DB connection for a specific role."""
    open_connections = []

    def _connect_as_role(role_name: str) -> psycopg2.extensions.connection:
        user_creds_map = {
            "superuser": (
                fastapi_settings.POSTGRES_USER,
                fastapi_settings.POSTGRES_PASSWORD,
            ),
            "db_owner": (
                fastapi_settings.DB_OWNER_USER,
                fastapi_settings.DB_OWNER_PASSWORD,
            ),
            "app_user": (fastapi_settings.APP_USER, fastapi_settings.APP_USER_PASSWORD),
            "app_user_login": (
                fastapi_settings.APP_USER_LOGIN,
                fastapi_settings.APP_USER_LOGIN_PASSWORD,
            ),
        }
        user, password = user_creds_map.get(role_name, (None, None))
        if not user:
            pytest.fail(
                f"Unknown or improperly configured database role: '{role_name}'"
            )

        try:
            conn = psycopg2.connect(
                host=fastapi_settings.DB_HOST_TEST,
                port=fastapi_settings.DB_PORT,
                user=user,
                password=password,
                dbname=fastapi_settings.APP_DB_NAME,
                connect_timeout=5,
            )
            open_connections.append(conn)
            return conn
        except Exception as e:
            pytest.fail(f"Could not establish connection for role '{role_name}': {e}")

    yield _connect_as_role

    for conn in open_connections:
        if not conn.closed:
            conn.close()
