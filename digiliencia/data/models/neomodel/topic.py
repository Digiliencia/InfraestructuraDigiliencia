from neomodel import (
    One,
    RelationshipTo,
    StringProperty,
    StructuredNode,
    UniqueIdProperty,
)

from digiliencia.data.models.neomodel.organization.organization import Organization  # noqa: F401


class Topic(StructuredNode):
    """Topic node model."""

    uid = UniqueIdProperty()
    name = StringProperty(required=True, unique_index=True)
    definition = StringProperty()
    url = StringProperty(required=True, unique_index=True)

    source_organization = RelationshipTo("Organization", "SOURCE", cardinality=One)
