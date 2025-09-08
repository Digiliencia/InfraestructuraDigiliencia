import logging

from neomodel import (
    One,
    RelationshipTo,
    StringProperty,
    StructuredNode,
    UniqueIdProperty,
)
import logging

from digiliencia.enums.topics import TOPIC_VALUES, is_valid_topic
from digiliencia.data.models.neomodel.organization.organization import Organization  # noqa: F401
from digiliencia.enums.topics import is_valid_topic
import logging
logger = logging.getLogger(__name__)
from digiliencia.enums.topics import is_valid_topic, TOPIC_VALUES

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

    def save(self, *args, **kwargs):  # type: ignore[override]
        if self.name and not is_valid_topic(self.name):
            logger.warning("Topic name fuera de enum, se guarda igualmente: %s", self.name)
        return super().save(*args, **kwargs)

    @classmethod
    def valid_names(cls):
        return list(TOPIC_VALUES)
