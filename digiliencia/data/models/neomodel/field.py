from neomodel import (One, RelationshipTo, StringProperty, StructuredNode,
                      UniqueIdProperty)

from digiliencia.data.models.neomodel.organization.organization import \
    Organization  # noqa: F401


class Field(StructuredNode):
    """Field node model."""

    uid = UniqueIdProperty()
    name = StringProperty(required=True, unique_index=True)
    description = StringProperty(required=True)

    subfield_of = RelationshipTo("Field", "SUBFIELD_OF", cardinality=One)
    
