import os
from pathlib import Path
from typing import Dict, Generator

import pytest
from neo4j import GraphDatabase

# Configuration constants
TEST_DB_CONFIG = {
    "DDBB_URI": "bolt://neo4j:testpassword@neo4j-test:7687",
    "TESTING": "true",
    "WEFORUM_EMAIL": "test@example.com",
    "WEFORUM_PASSWD": "testpassword",
    "WEBDRIVERWAIT_TIMEOUT": "5",
    "IMPLICIT_WAIT": "2",
    "LLM_URL": "http://localhost:11434",
}


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
