import os
from pathlib import Path
from typing import Dict, Generator
import subprocess
import time
import requests

import pytest
from neo4j import GraphDatabase

import psycopg2
from dotenv import load_dotenv
import sys
from faker import Faker

import pytest_asyncio
import httpx
import multiprocessing
import asyncio
from typing import AsyncGenerator, Any
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert, text
import json
from httpx import AsyncClient

from starlette import status
from digiliencia.configs.fastAPI.core.config import settings
from digiliencia.configs.fastAPI.db.models import User, Chat, Message, IAPrompt, Model, Base
from digiliencia.configs.fastAPI.core.endpoints import TEMPLATE_LIST, MODEL_LIST, REGISTER, LOGIN, USERS_ME



# Configuration constants
TEST_DB_CONFIG = {
    "DDBB_URI": "bolt://neo4j:testpassword@neo4j-test:7687",
    "TESTING": "true",
    "WEFORUM_EMAIL": "test@example.com",
    "WEFORUM_PASSWD": "testpassword",
    "WEBDRIVERWAIT_TIMEOUT": "5",
    "IMPLICIT_WAIT": "2",
    "LLM_URL": "http://localhost:11434",
    "CLASSIFICATION_MODEL": "test_model",
    "EMBEDDINGS_SERVICE": "http://localhost:8000",
    "COMPOSE_PROJECT_DIR": "../.devcontainer",
    "SERVICE_NAME": "embedding-api-service",
}


@pytest.fixture(#autouse=True,
        scope="session")
def setup_test_environment() -> Generator[None, None, None]:
    """
    Configure the test environment before any tests run.

    This fixture:
    1. Sets up test environment variables
    2. Configures testing mode
    3. Resets singletons to use test configuration
    4. Cleans up after all tests complete
    """
    # Store original environment variables
    original_env: Dict[str, str | None] = {
        key: os.environ.get(key) for key in TEST_DB_CONFIG.keys()
    }

    # Set test environment variables
    for key, value in TEST_DB_CONFIG.items():
        os.environ[key] = value

    # Reset singletons to pick up new environment variables
    _reset_singletons()

    yield  # Run tests

    # Cleanup: restore original environment
    _restore_environment(original_env)
    _reset_singletons()


def _reset_singletons() -> None:
    """Reset singleton instances for testing."""
    from digiliencia.configs.env import Env

    Env.reset_instance()
    # Note: Database singleton is no longer used with neomodel


def _restore_environment(original_env: Dict[str, str | None]) -> None:
    """Restore original environment variables."""
    for key, original_value in original_env.items():
        if original_value is None:
            os.environ.pop(key, None)
        else:
            os.environ[key] = original_value


@pytest.fixture(#autouse=True,
        scope="function")
def reset_neo4j_db():
    """Reset the Neo4j database before each test function."""
    from urllib.parse import urlparse

    from digiliencia.configs.env import Env

    env = Env()
    _validate_db_config(env)

    # Parse URI to extract credentials if present
    parsed_uri = urlparse(env.ddbb_uri)

    if parsed_uri.username and parsed_uri.password:
        # URI contains credentials, extract them
        clean_uri = (
            f"{parsed_uri.scheme}://{parsed_uri.hostname}:{parsed_uri.port or 7687}"
        )
        driver = GraphDatabase.driver(
            clean_uri, auth=(parsed_uri.username, parsed_uri.password)
        )
    else:
        # URI doesn't contain credentials
        driver = GraphDatabase.driver(env.ddbb_uri)

    try:
        _clear_database(driver)
        _initialize_database(driver)
    finally:
        driver.close()


def _validate_db_config(env) -> None:
    """Validate that required database configuration is present."""
    assert env.ddbb_uri, "DDBB_URI must be set in the environment variables."


def _clear_database(driver) -> None:
    """Clear all data and constraints from the database."""
    with driver.session() as session:
        # Drop all constraints
        constraints = session.run("SHOW CONSTRAINTS")
        for record in constraints:
            name = record["name"]
            session.run(f"DROP CONSTRAINT {name}")

        # Detach and delete all nodes
        session.run("MATCH (n) DETACH DELETE n")


def _initialize_database(driver) -> None:
    """Initialize the database with schema from initialization.cypher."""
    cypher_path = Path(__file__).parent / "../digiliencia/data/db/initialization.cypher"

    if not cypher_path.exists():
        print(f"[WARNING] initialization.cypher not found at {cypher_path}")
        return

    cypher_content = cypher_path.read_text()

    with driver.session() as session:
        try:
            for query in cypher_content.split(";"):
                query = query.strip()
                if query:
                    session.run(query)
        except Exception as e:
            print(f"[WARNING] Error executing initialization.cypher:\n{e}")


@pytest.fixture(scope="session", autouse=False)
def run_container():
    # Build and start the service
    subprocess.run(
        [
            "docker",
            "compose",
            "-f",
            f"{TEST_DB_CONFIG['COMPOSE_PROJECT_DIR']}/docker-compose.yml",
            "build",
            TEST_DB_CONFIG["SERVICE_NAME"],
        ],
        check=True,
    )
    subprocess.Popen(
        [
            "docker",
            "compose",
            "-f",
            f"{TEST_DB_CONFIG['COMPOSE_PROJECT_DIR']}/docker-compose.yml",
            "up",
            TEST_DB_CONFIG["SERVICE_NAME"],
        ],
        cwd=TEST_DB_CONFIG["COMPOSE_PROJECT_DIR"],
    )

    # Wait for the service to be ready
    for _ in range(30):
        try:
            r = requests.get("http://localhost:8000/docs")
            if r.status_code == 200:
                break
        except Exception:
            pass
        time.sleep(2)
    else:
        # If the API does not start in time, shut down the container and raise an error
        subprocess.run(
            [
                "docker",
                "compose",
                "-f",
                f"{TEST_DB_CONFIG['COMPOSE_PROJECT_DIR']}/docker-compose.yml",
                "logs",
                TEST_DB_CONFIG["SERVICE_NAME"],
            ],
            cwd=TEST_DB_CONFIG["COMPOSE_PROJECT_DIR"],
        )
        subprocess.run(
            [
                "docker",
                "compose",
                "-f",
                f"{TEST_DB_CONFIG['COMPOSE_PROJECT_DIR']}/docker-compose.yml",
                "down",
            ],
            cwd=TEST_DB_CONFIG["COMPOSE_PROJECT_DIR"],
        )
        raise RuntimeError("API did not start in time")

    yield  # Provide the fixture to the test functions

    # Teardown: stop the service
    subprocess.run(
        [
            "docker",
            "compose",
            "-f",
            f"{TEST_DB_CONFIG['COMPOSE_PROJECT_DIR']}/docker-compose.yml",
            "down",
        ],
        cwd=TEST_DB_CONFIG["COMPOSE_PROJECT_DIR"],
    )


# =============================================================================
# Common Test Data Fixtures
# =============================================================================


@pytest.fixture
def sample_scraped_data():
    """Sample scraped news data for testing."""
    from datetime import datetime

    from pydantic import HttpUrl

    from digiliencia.data.models.news_model import ScrapedNews

    return ScrapedNews(
        header="Test Cybersecurity News",
        date=datetime(2023, 1, 1, 12, 0),
        source="Test News Agency",
        content="This is test cybersecurity news content.",
        url=HttpUrl("https://example.com/test-news"),
        authors=["John Doe", "Jane Smith"],
        topics=["Cybersecurity", "AI Security"],
    )


@pytest.fixture
def minimal_scraped_data():
    """Minimal scraped news data for testing edge cases."""
    from datetime import datetime

    from pydantic import HttpUrl

    from digiliencia.data.models.news_model import ScrapedNews

    return ScrapedNews(
        header="Minimal News",
        date=datetime(2023, 1, 1),
        source="Minimal Source",
        content="Minimal content",
        url=HttpUrl("https://example.com/minimal"),
        authors=[],
        topics=[],
    )


@pytest.fixture
def sample_topic_data():
    """Sample topic data for testing."""
    return {
        "name": "Test Topic",
        "definition": "Definition for Test Topic",
        "url": "https://example.com/test-topic",
    }


@pytest.fixture
def multiple_topics_data():
    """Multiple topic data objects for testing."""
    topic_names = [
        "Cybersecurity",
        "Artificial Intelligence",
        "Data Privacy",
        "Cloud Computing",
    ]
    return [
        {
            "name": name,
            "definition": f"Definition for {name}",
            "url": f"https://example.com/{name.lower().replace(' ', '-')}",
        }
        for name in topic_names
    ]


@pytest.fixture
def sample_author_data():
    """Sample author data for testing."""
    return {
        "name": "Test Author",
        "email": "test@example.com",
        "description": "Test author description",
    }


# =============================================================================
# PostgreSQL DB Test Data Fixtures
# =============================================================================

# --- Initialization & Environment Loading ---
fake = Faker()
dotenv_path = Path(__file__).resolve().parent.parent / ".env"
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

# =============================================================================
# FastAPI Async SQLAlchemy Test Data Fixture
# =============================================================================

# /tests/conftest.py
"""
This module serves as the central configuration file for pytest.

It defines shared fixtures that are used across multiple test files to provide
dependencies like a running API server, database sessions, and HTTP clients.
This approach promotes code reuse and ensures a consistent testing environment.
"""


# Load environment variables from the project's .env file
dotenv_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path)

# --- Database Setup ---
TEST_DATABASE_URL = settings.DATABASE_TEST_URL
engine = create_async_engine(TEST_DATABASE_URL, echo=False)
TestingSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

faker = Faker()

# --- HTTP Client Fixtures ---
API_URL = "http://127.0.0.1:8080/api"
HEALTH_CHECK_URL = "http://127.0.0.1:8080/api/health"


def run_server():
    """Target function to run the Uvicorn server in a separate process."""
    # uvicorn.run(app, host="127.0.0.1", port=8080)
    pass


async def wait_for_server(url: str, timeout: int = 10):
    """Polls the health check endpoint until the server is responsive."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            async with httpx.AsyncClient() as client:
                await client.get(url)
                return
        except httpx.ConnectError:
            await asyncio.sleep(0.1)
    raise TimeoutError("Test server did not start within the timeout period.")


@pytest.fixture(scope="session", autouse=True)
def app_server():
    """
    Session-scoped fixture to manage the lifecycle of the FastAPI test server.

    It starts the server in a separate process before any tests run and
    terminates it after all tests in the session are complete.
    """
    proc = multiprocessing.Process(target=run_server, daemon=True)
    proc.start()
    try:
        asyncio.run(wait_for_server(HEALTH_CHECK_URL))
    except TimeoutError as e:
        proc.terminate()
        proc.join()
        pytest.fail(f"Server failed to start: {e}")

    yield

    proc.terminate()
    proc.join()


@pytest_asyncio.fixture(scope="session", autouse=True)
async def setup_database():
    """
    Session-scoped fixture to initialize and tear down the test database.

    It runs once per test session, dropping and recreating all tables to ensure
    a clean state, then seeds the database with initial data. After all tests
    are finished, it drops all tables again.
    """
    sql_drop_tables = text(
        """
        DO $$
        BEGIN
           DROP TABLE IF EXISTS MESSAGES CASCADE;
           DROP TABLE IF EXISTS CHATS CASCADE;
           DROP TABLE IF EXISTS USERS CASCADE;
           DROP TABLE IF EXISTS IA_PROMPTS CASCADE;
           DROP TABLE IF EXISTS MODELS CASCADE;
        END $$;
        """
    )

    async with engine.begin() as conn:
        await conn.execute(sql_drop_tables)
        await conn.run_sync(Base.metadata.create_all)

    # Seed data in a separate session
    async with TestingSessionLocal() as session:
        async with session.begin():
            users = [
                {
                    "email": faker.unique.email(),
                    "hashed_password": faker.password(length=12),
                }
                for _ in range(5)
            ]
            result_users = await session.execute(insert(User).returning(User.id), users)
            user_ids = [row.id for row in result_users]

            prompts = [
                {
                    "prompt_name": faker.text(max_nb_chars=100),
                    "prompt": faker.text(max_nb_chars=100),
                    "prompt_description": faker.sentence(),
                }
                for _ in range(3)
            ]
            result_prompts = await session.execute(
                insert(IAPrompt).returning(IAPrompt.id), prompts
            )
            prompt_ids = [row.id for row in result_prompts]

            chats = [
                {
                    "tittle": faker.sentence(nb_words=3),
                    "user_id": faker.random_element(user_ids),
                    "ia_prompt_id": faker.random_element(prompt_ids),
                }
                for _ in range(10)
            ]
            result_chats = await session.execute(insert(Chat).returning(Chat.id), chats)
            chat_ids = [row.id for row in result_chats]

            models_data = [{"ia_name": faker.unique.word()} for _ in range(3)]
            result_models = await session.execute(
                insert(Model).returning(Model.id), models_data
            )
            model_ids = [row.id for row in result_models]

            messages = []
            for chat_id in chat_ids:
                for order in range(1, 4):
                    messages.append(
                        {
                            "order_number": order,
                            "content": faker.paragraph(),
                            "statistics": json.dumps(
                                {"tokens": faker.random_int(1, 100)}
                            ),
                            "chat_id": chat_id,
                            "model_id": faker.random_element(model_ids),
                        }
                    )
            await session.execute(insert(Message), messages)

        await session.commit()

    yield

    async with engine.begin() as conn:
        await conn.execute(sql_drop_tables)


@pytest_asyncio.fixture(scope="function")
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Function-scoped fixture providing an isolated database session for each test.

    It begins a transaction before yielding the session to the test and rolls
    back the transaction after the test completes, ensuring test isolation.
    """
    async with TestingSessionLocal() as session:
        trans = await session.begin()
        try:
            yield session
        finally:
            await trans.rollback()


@pytest_asyncio.fixture(scope="function")
async def api_client() -> AsyncGenerator[httpx.AsyncClient, Any]:
    """
    Function-scoped fixture providing an unauthenticated HTTP client.
    """
    async with httpx.AsyncClient(base_url=API_URL) as client:
        yield client


@pytest.fixture(scope="function")
def fake_user() -> dict:
    """
    Function-scoped fixture that generates a dictionary with fake user data.
    """
    return {"email": faker.email(), "password": "ValidPassword123"}


@pytest_asyncio.fixture(scope="function")
async def authenticated_client(
    fake_user: dict,
) -> AsyncGenerator[httpx.AsyncClient, Any]:
    """
    Function-scoped fixture that provides an authenticated HTTP client.

    It performs the complete authentication flow:
    1. Registers a new user with fake data.
    2. Logs the new user in to obtain a JWT.
    3. Yields an HTTP client with the `Authorization` header pre-set.
    4. Deletes the user after the test is complete for cleanup.
    """
    async with httpx.AsyncClient(base_url=API_URL) as auth_client:
        response = await auth_client.post(REGISTER, json=fake_user)
        if response.status_code != 201:
            raise Exception(f"User registration failed in fixture: {response.text}")

        response = await auth_client.post(
            LOGIN,
            json={"email": fake_user["email"], "password": fake_user["password"]},
        )
        if response.status_code != 200:
            raise Exception(f"User login failed in fixture: {response.text}")

        token = response.json()["access_token"]
        auth_client.headers.update({"Authorization": f"Bearer {token}"})

        yield auth_client

        response = await auth_client.delete(USERS_ME)
        if response.status_code != 204:
            print(f"Warning: Failed to cleanup user {fake_user['email']}")


@pytest_asyncio.fixture(scope="function")
async def templates(authenticated_client: AsyncClient) -> list:
    """
    Function-scoped fixture that fetches the list of available prompt templates.
    """
    response = await authenticated_client.get(TEMPLATE_LIST)
    if response.status_code != status.HTTP_202_ACCEPTED:
        raise Exception(f"Error getting templates: {response.status_code}")

    templates_list = response.json()
    if not templates_list:
        raise Exception("No templates found in database to use in tests.")

    return templates_list


@pytest_asyncio.fixture(scope="function")
async def models(authenticated_client: AsyncClient) -> list:
    """
    Function-scoped fixture that fetches the list of available AI models.
    """
    response = await authenticated_client.get(MODEL_LIST)
    if response.status_code != status.HTTP_202_ACCEPTED:
        raise Exception(f"Error getting models: {response.status_code}")

    models_list = response.json()
    if not models_list:
        raise Exception("No models found in database to use in tests.")

    return models_list


# =============================================================================
# Common Mock Fixtures
# =============================================================================


@pytest.fixture
def mock_topics():
    """Create mock Topic objects for testing."""
    topic_names = [
        "Cybersecurity",
        "Artificial Intelligence",
        "Data Privacy",
        "Cloud Computing",
    ]

    topics = []
    for i, name in enumerate(topic_names):
        # Create a simple object with the required attributes
        topic = type(
            "MockTopic",
            (),
            {
                "uid": f"uid_{i}",
                "name": name,
                "definition": f"Definition for {name}",
                "url": f"https://example.com/{name.lower().replace(' ', '-')}",
            },
        )()
        topics.append(topic)

    return topics


@pytest.fixture
def mock_topic_service(mock_topics):
    """Create a mock TopicService."""

    class MockTopicService:
        def get_all_topics(self):
            return mock_topics

    return MockTopicService()


@pytest.fixture
def mock_news():
    """Create a mock news object."""

    class MockNews:
        def __init__(self):
            self.content = (
                "This article discusses the latest developments in artificial "
                "intelligence and cybersecurity measures for protecting sensitive data."
            )

    return MockNews()


@pytest.fixture
def mock_response_factory():
    """Factory for creating mock HTTP responses."""

    def _create_response(json_data=None, status_code=200, raise_for_status_effect=None):
        class MockResponse:
            def __init__(self):
                self._json_data = json_data
                self.status_code = status_code
                self._raise_for_status_effect = raise_for_status_effect

            def json(self):
                return self._json_data

            def raise_for_status(self):
                if self._raise_for_status_effect:
                    raise self._raise_for_status_effect

        return MockResponse()

    return _create_response
