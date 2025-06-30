from neomodel import StringProperty, StructuredNode, UniqueIdProperty


class Topic(StructuredNode):
    """Topic node model."""

    uid = UniqueIdProperty()
    name = StringProperty(required=True, unique_index=True)
    definition = StringProperty()

    class Meta:
        app_label = "digiliencia"
