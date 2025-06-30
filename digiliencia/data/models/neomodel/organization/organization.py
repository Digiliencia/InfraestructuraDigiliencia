from neomodel import StringProperty, StructuredNode, UniqueIdProperty


class Organization(StructuredNode):
    """Organization base node model."""

    uid = UniqueIdProperty()
    name = StringProperty(required=True, unique_index=True)
    description = StringProperty()

    class Meta:
        app_label = "digiliencia"
