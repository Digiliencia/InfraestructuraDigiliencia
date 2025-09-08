from neomodel import (
    One,
    RelationshipTo,
    StringProperty,
    StructuredNode,
    UniqueIdProperty,
)
import logging
from digiliencia.data.models.neomodel.organization.organization import Organization  # noqa: F401
from digiliencia.enums.related_fields import is_valid_related_field, all_related_field_values

logger = logging.getLogger(__name__)


class Field(StructuredNode):
    """Field node model."""

    uid = UniqueIdProperty()
    name = StringProperty(required=True, unique_index=True)
    description = StringProperty(required=True)

    subfield_of = RelationshipTo("Field", "SUBFIELD_OF", cardinality=One)

    def save(self, *args, **kwargs):  # type: ignore[override]
        if self.name and not is_valid_related_field(self.name):
            logger.warning(
                "Intento de guardar Field con nombre no reconocido '%s' (se guarda igual para compatibilidad)",
                self.name,
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
        return list(all_related_field_values())
