"""Neomodel base models."""

from neomodel import StringProperty, StructuredNode, UniqueIdProperty


class Person(StructuredNode):
    """Person node model."""

    uid = UniqueIdProperty()
    name = StringProperty(required=True, unique_index=True)
    email = StringProperty()
    description = StringProperty()

    class Meta:
        app_label = "digiliencia"


class Topic(StructuredNode):
    """Topic node model."""

    uid = UniqueIdProperty()
    name = StringProperty(required=True, unique_index=True)
    definition = StringProperty()

    class Meta:
        app_label = "digiliencia"


class Organization(StructuredNode):
    """Organization base node model."""

    uid = UniqueIdProperty()
    name = StringProperty(required=True, unique_index=True)
    description = StringProperty()

    class Meta:
        app_label = "digiliencia"


class NewsAgency(Organization):
    """News agency node model that inherits from Organization."""

    pass
