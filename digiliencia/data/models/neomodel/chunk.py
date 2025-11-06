"""Chunk node for storing embedded fragments of News content."""

from neomodel import (
    ArrayProperty,
    FloatProperty,
    IntegerProperty,
    StringProperty,
    StructuredNode,
    UniqueIdProperty,
)


class Chunk(StructuredNode):
    """Represents a chunk of text belonging to a News item."""

    uid = UniqueIdProperty()
    index = IntegerProperty(required=True)  # Order of the chunk within the news
    text = StringProperty(required=True)
    embedding = ArrayProperty(FloatProperty(), default=None)
    kind = StringProperty(
        default="content"
    )  # 'content' (default) or other kinds if extended
    model = StringProperty(required=True)  # Embedding model used for this chunk

    # Relationship to News is defined on News side as HAS_CHUNK
