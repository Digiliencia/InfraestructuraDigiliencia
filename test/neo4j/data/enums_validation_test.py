from digiliencia.enums.topics import is_valid_topic, TOPIC_VALUES
from digiliencia.enums.related_fields import (
    is_valid_related_field,
    all_related_field_values,
    related_field_category,
)


def test_topics_enum_validation():
    assert is_valid_topic(next(iter(TOPIC_VALUES)))
    assert not is_valid_topic("__NOPE__")


def test_related_fields_any_value():
    all_values = all_related_field_values()
    assert len(all_values) > 50  # sanity check
    one_value = next(iter(all_values))
    assert is_valid_related_field(one_value)
    assert not is_valid_related_field("__INVALID_FIELD__")


def test_related_field_category():
    all_values = all_related_field_values()
    sample = next(iter(all_values))
    cat = related_field_category(sample)
    assert cat is not None
    assert isinstance(cat, str)
