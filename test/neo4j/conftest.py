import os
from pathlib import Path
from typing import Dict, Generator
import subprocess
import time
import requests

import pytest
from neo4j import GraphDatabase

from test.conftest import TEST_DB_CONFIG


@pytest.fixture(autouse=True, scope="session")
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


@pytest.fixture(autouse=True, scope="function")
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
