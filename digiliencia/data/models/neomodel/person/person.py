from neomodel import StringProperty, StructuredNode, UniqueIdProperty


class Person(StructuredNode):
    """Person node model."""

    uid = UniqueIdProperty()
    name = StringProperty(required=True, unique_index=True)
    email = StringProperty()
    description = StringProperty()
