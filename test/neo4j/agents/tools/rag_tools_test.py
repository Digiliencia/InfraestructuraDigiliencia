import pytest
import inspect
from neo4j import GraphDatabase

from enum import Enum


from digiliencia.enums.topics import Topics
from digiliencia.enums.related_fields import RelatedFields


class Neo4jEnumChecker:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def check_node_exists(self, name: str) -> bool:
        query = "MATCH (n {name: $name}) RETURN n LIMIT 1"
        with self.driver.session() as session:
            result = session.run(query, name=name)
            return result.single() is not None

    def check_all_enums(self, topics_class):
        for _, enum_class in inspect.getmembers(topics_class, inspect.isclass):
            if issubclass(enum_class, Enum):
                print(f"\n[Checking category: {enum_class.__name__}]")
                for item in list(enum_class):
                    exists = self.check_node_exists(item.value)
                    status = "✅ Found" if exists else "❌ Missing"
                    print(f"- {item.value}: {status}")


@pytest.mark.usefixtures("reset_neo4j_db")
def test_check_all_project_enums(capsys):
    """
    Test que recorre todas las enums del proyecto y verifica su existencia en Neo4j,
    igual que el main de rag_tools.py pero para Topics y RelatedFields.
    """
    from digiliencia.configs.env import Env

    env = Env()
    # Extrae usuario y contraseña si están en la URI
    from urllib.parse import urlparse

    parsed_uri = urlparse(env.ddbb_uri)
    if parsed_uri.username and parsed_uri.password:
        uri = f"{parsed_uri.scheme}://{parsed_uri.hostname}:{parsed_uri.port or 7687}"
        user = parsed_uri.username
        password = parsed_uri.password
    else:
        uri = env.ddbb_uri
        user = "neo4j"
        password = "testpassword"
    checker = Neo4jEnumChecker(uri, user, password)
    try:
        # Primero Topics
        print("\n[Checking category: Topics]")
        for item in Topics:
            exists = checker.check_node_exists(item.value)
            status = "✅ Found" if exists else "❌ Missing"
            print(f"- {item.value}: {status}")

        # Ahora todas las subenums de RelatedFields
        checker.check_all_enums(RelatedFields)

        captured = capsys.readouterr()
        # Debe imprimir el nombre de cada categoría y el estado de cada item
        assert "[Checking category:" in captured.out
        assert ("✅ Found" in captured.out) or ("❌ Missing" in captured.out)
        # Debe mostrar también los Topics
        for item in Topics:
            assert item.value in captured.out
    finally:
        checker.close()
