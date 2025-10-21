import pytest
import os
import psycopg2
from dotenv import load_dotenv
from pathlib import Path
import sys
from faker import Faker

# --- Initialization & Environment Loading ---
fake = Faker()
dotenv_path = Path(__file__).resolve().parent.parent / "../.env"
load_dotenv(dotenv_path)

# --- Database Configuration Variables ---
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
APP_DB_NAME = os.getenv("APP_DB_NAME")
DB_OWNER_USER = os.getenv("DB_OWNER_USER")
DB_OWNER_PASSWORD = os.getenv("DB_OWNER_PASSWORD")
APP_USER = os.getenv("APP_USER")
APP_USER_PASSWORD = os.getenv("APP_USER_PASSWORD")
APP_USER_LOGIN = os.getenv("APP_USER_LOGIN")
APP_USER_LOGIN_PASSWORD = os.getenv("APP_USER_LOGIN_PASSWORD")

# Verify that all necessary variables are present
for var_name in [
    "POSTGRES_USER",
    "POSTGRES_PASSWORD",
    "APP_DB_NAME",
    "DB_OWNER_USER",
    "DB_OWNER_PASSWORD",
    "APP_USER",
    "APP_USER_PASSWORD",
    "APP_USER_LOGIN",
    "APP_USER_LOGIN_PASSWORD",
]:
    if not os.getenv(var_name):
        raise EnvironmentError(f"Missing environment variable for tests: {var_name}")


# --- Connection Factory Fixture ---
@pytest.fixture(scope="function")
def get_db_connection_for_role():
    """Factory to get a DB connection for a specific role."""
    open_connections = []

    def _connect_as_role(role_name: str):
        user_creds_map = {
            "superuser": (POSTGRES_USER, POSTGRES_PASSWORD),
            "db_owner": (DB_OWNER_USER, DB_OWNER_PASSWORD),
            "app_user": (APP_USER, APP_USER_PASSWORD),
            "app_user_login": (APP_USER_LOGIN, APP_USER_LOGIN_PASSWORD),
        }
        user, password = user_creds_map.get(role_name, (None, None))
        if not user:
            pytest.fail(
                f"Unknown or improperly configured database role: '{role_name}'"
            )

        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                port=DB_PORT,
                user=user,
                password=password,
                dbname=APP_DB_NAME,
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


# --- Database Population and Cleanup Fixture ---
@pytest.fixture(scope="function")
def populated_db(get_db_connection_for_role):
    """
    Populates tables with test data and yields the connection used.
    Ensures cleanup after the test.
    """
    conn = get_db_connection_for_role("db_owner")
    cursor = conn.cursor()

    print(f"\n--- Populating '{APP_DB_NAME}' with test data ---")
    try:
        # Cleanup any existing data
        cursor.execute(
            "TRUNCATE TABLE MESSAGES, CHATS, USERS, IA_PROMPTS, MODELS RESTART IDENTITY CASCADE;"
        )
        conn.commit()

        # 1. Populate tables without dependencies
        cursor.execute(
            "INSERT INTO MODELS (IA_name) VALUES (%s), (%s) RETURNING ID;",
            (fake.unique.word(), fake.unique.word()),  # Avoid duplicates
        )
        model_ids = [row[0] for row in cursor.fetchall()]

        cursor.execute(
            "INSERT INTO IA_PROMPTS (prompt, IA_name) VALUES ('You are a helpful assistant.', 'GeneralAssistant') RETURNING ID;"
        )
        prompt_ids = [row[0] for row in cursor.fetchall()]

        # 2. Populate USERS
        user_ids = []
        for _ in range(5):
            cursor.execute(
                "INSERT INTO USERS (email, hashed_password) VALUES (%s, %s) RETURNING ID;",
                (fake.unique.email(), "fakepass"),
            )
            user_ids.append(cursor.fetchone()[0])

        # 3. Populate CHATS (depends on USERS)
        chat_ids = []
        for user_id in user_ids:
            cursor.execute(
                "INSERT INTO CHATS (tittle, user_id) VALUES (%s, %s) RETURNING ID;",
                (f"Chat for {user_id}", user_id),
            )
            chat_ids.append(cursor.fetchone()[0])

        # 4. Populate MESSAGES (depends on CHATS, MODELS, IA_PROMPTS)
        for i, chat_id in enumerate(chat_ids):
            cursor.execute(
                """INSERT INTO MESSAGES (order_number, content, chat_id, model_id, ia_prompt_id)
                   VALUES (%s, %s, %s, %s, %s);""",
                (
                    i + 1,
                    "This is a test message.",
                    chat_id,
                    fake.random_element(model_ids),
                    fake.random_element(prompt_ids),
                ),
            )
        conn.commit()
        print("--- Population complete ---")

        yield conn  # Yield the connection to the test function

    finally:
        print(f"\n--- Cleaning up data from '{APP_DB_NAME}' ---")
        try:
            # Use a new cursor in case the test closed the old one
            if not conn.closed:
                cleanup_cursor = conn.cursor()
                cleanup_cursor.execute(
                    "TRUNCATE TABLE MESSAGES, CHATS, USERS, IA_PROMPTS, MODELS RESTART IDENTITY CASCADE;"
                )
                conn.commit()
                print("--- Cleanup complete ---")
                cleanup_cursor.close()
        except Exception as e:
            print(f"Error during database cleanup: {e}", file=sys.stderr)
            conn.rollback()
        # The connection itself will be closed by the get_db_connection_for_role fixture's own teardown
