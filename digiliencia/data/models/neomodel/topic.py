from neomodel import (
    One,
    RelationshipTo,
    StringProperty,
    StructuredNode,
    UniqueIdProperty,
)


class Topic(StructuredNode):
    """Topic node model."""

    uid = UniqueIdProperty()
    name = StringProperty(required=True, unique_index=True)
    definition = StringProperty()
    url = StringProperty(required=True, unique_index=True)

    source = RelationshipTo("Organization", "SOURCE", cardinality=One)
