import os

import pytest
from neo4j import GraphDatabase


@pytest.fixture(autouse=True, scope="function")
def reset_neo4j_db():
    """
    Resetea la base de datos Neo4j de testing antes de cada test usando el script de inicialización.
    """
    uri = os.getenv("DDBB_URI")
    user = os.getenv("DDBB_USERNAME")
    passwd = os.getenv("DDBB_PASSWD")
    assert uri and user and passwd, (
        "Variables de entorno de conexión a Neo4j no definidas."
    )

    driver = GraphDatabase.driver(uri, auth=(user, passwd))
    with driver.session() as session:
        # Eliminar todos los constraints existentes
        constraints = session.run("SHOW CONSTRAINTS")
        for record in constraints:
            name = record["name"]
            # Usar consulta parametrizada para evitar problemas de tipado
            session.run("DROP CONSTRAINT " + name)
        # Eliminar todos los nodos y relaciones
        session.run("MATCH (n) DETACH DELETE n")
        # Ejecutar el script de constraints
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
            pass  # ignorar errores de constraints ya existentes
    driver.close()
