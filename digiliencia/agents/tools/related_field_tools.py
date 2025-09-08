import os
from neo4j import GraphDatabase
from digiliencia.enums.related_fields import ALL_RELATED_FIELDS_ENUMS


def list_related_field_categories() -> list[str]:
    return [enum.__name__ for enum in ALL_RELATED_FIELDS_ENUMS]


def list_all_related_fields() -> list[str]:
    return [item.value for enum in ALL_RELATED_FIELDS_ENUMS for item in enum]


def _get_driver():
    uri = os.getenv("NEO4J_URI")
    user = os.getenv("NEO4J_USER")
    pwd = os.getenv("NEO4J_PASSWORD")
    if not all([uri, user, pwd]):
        raise RuntimeError("Faltan variables NEO4J_URI / NEO4J_USER / NEO4J_PASSWORD")
    return GraphDatabase.driver(uri, auth=(user, pwd))


def check_related_field_exists(name: str) -> bool:
    driver = _get_driver()
    try:
        with driver.session() as s:
            r = s.run("MATCH (n {name: $name}) RETURN 1 LIMIT 1", name=name)
            return r.single() is not None
    finally:
        driver.close()


def missing_related_fields() -> list[str]:
    all_vals = set(list_all_related_fields())
    driver = _get_driver()
    try:
        with driver.session() as s:
            r = s.run("MATCH (n) WHERE exists(n.name) RETURN DISTINCT n.name AS name")
            existing = {row["name"] for row in r}
    finally:
        driver.close()
    return sorted(all_vals - existing)


TOOLS = [
    {
        "name": "list_related_field_categories",
        "callable": list_related_field_categories,
        "description": "Lista nombres de categorías.",
    },
    {
        "name": "list_all_related_fields",
        "callable": list_all_related_fields,
        "description": "Lista todos los valores de related fields.",
    },
    {
        "name": "check_related_field_exists",
        "callable": check_related_field_exists,
        "description": "Verifica si un valor existe como nodo (name).",
    },
    {
        "name": "missing_related_fields",
        "callable": missing_related_fields,
        "description": "Devuelve los valores que faltan en Neo4j.",
    },
]


# faltaría el verctor de poder recorrer el related field enums
