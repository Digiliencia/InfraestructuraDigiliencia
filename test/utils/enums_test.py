"""Tests básicos para validación de enums de Topics y RelatedFields."""

from digiliencia.enums.topics import is_valid_topic, Topics
from digiliencia.enums.related_fields import (
    is_valid_related_field,
    get_all_related_field_values,
)


def test_is_valid_topic_true():
    assert is_valid_topic(Topics.PHISHING.value)


def test_is_valid_topic_false():
    assert not is_valid_topic("Phishing ")  # espacio extra


def test_related_field_collections_non_empty():
    values = get_all_related_field_values()
    assert len(values) > 10  # sanity check


def test_is_valid_related_field():
    # Tomamos un valor conocido
    assert is_valid_related_field("Online Surveillance")
    assert not is_valid_related_field("Online  Surveillance")  # doble espacio
