import logging

from neomodel import (
    One,
    RelationshipTo,
    StringProperty,
    StructuredNode,
    UniqueIdProperty,
)

from digiliencia.enums.topics import TOPIC_VALUES, is_valid_topic
from digiliencia.data.models.neomodel.organization.organization import Organization  # noqa: F401

logger = logging.getLogger(__name__)

logger = logging.getLogger(__name__)


class Topic(StructuredNode):
    """Topic node model."""

    uid = UniqueIdProperty()
    name = StringProperty(required=True, unique_index=True)
    definition = StringProperty()
    url = StringProperty(required=True, unique_index=True)

    source_organization = RelationshipTo("Organization", "SOURCE", cardinality=One)

    def save(self, *args, **kwargs):  # type: ignore[override]
        name_val = getattr(self, "name", None)
        if name_val and not is_valid_topic(name_val):
            logger.warning(
                "Intento de guardar Topic con nombre no reconocido '%s' (se guarda igual para no romper datos históricos)",
                name_val,
            )
        return super().save(*args, **kwargs)

    @classmethod
    def get_or_none(cls, name: str):
        try:
            return cls.nodes.get(name=name)
        except cls.DoesNotExist:
            return None

    @classmethod
    def valid_names(cls):
        return list(TOPIC_VALUES)
