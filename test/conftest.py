import os

import pytest
from neo4j import GraphDatabase

from digiliencia.configs.env import Env


@pytest.fixture(autouse=True, scope="session")
def override_env_vars():
    os.environ["DDBB_URI"] = "bolt://neo4j-test:7687"
    os.environ["DDBB_USERNAME"] = "neo4j"
    os.environ["DDBB_PASSWD"] = "testpassword"
    # Clear any cached Env instance if it exists


@pytest.fixture(autouse=True, scope="function")
def reset_neo4j_db():
    """
    Reset the Neo4j database before each test function.
    """
    env = Env()
    uri = env.ddbb_uri
    user = env.ddbb_username
    passwd = env.ddbb_passwd

    assert uri and user and passwd, (
        "DDBB_URI, DDBB_USERNAME, and DDBB_PASSWD must be set in the environment variables."
    )

    driver = GraphDatabase.driver(uri, auth=(user, passwd))
    with driver.session() as session:
        # Drop all constraints
        constraints = session.run("SHOW CONSTRAINTS")
        for record in constraints:
            name = record["name"]
            session.run("DROP CONSTRAINT " + name)
        # Detach and delete all nodes
        session.run("MATCH (n) DETACH DELETE n")
        # Run the initialization.cypher script
        cypher_path = os.path.join(
            os.path.dirname(__file__), "../digiliencia/data/db/initialization.cypher"
        )
        cypher_path = os.path.abspath(cypher_path)
        with open(cypher_path, "r") as f:
            cypher = f.read()
        try:
            for query in cypher.split(";"):
                query = query.strip()
                if query:
                    session.run(query)  # type: ignore
        except Exception as e:
            print(
                f"[ADVERTENCIA] Error ejecutando initialization.cypher completo:\n{e}"
            )
            pass
    driver.close()
