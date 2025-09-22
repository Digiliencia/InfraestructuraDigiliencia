"""Complex neomodel models."""

import logging
from datetime import datetime

from neomodel import (
    ArrayProperty,
    DateTimeProperty,
    FloatProperty,
    One,
    RelationshipTo,
    StringProperty,
    StructuredNode,
    UniqueIdProperty,
    ZeroOrMore,
)

from digiliencia.data.models.neomodel.chunk import Chunk
from digiliencia.data.models.neomodel.field import Field
from digiliencia.data.models.neomodel.organization.news_agency import NewsAgency
from digiliencia.data.models.neomodel.person.author import Author
from digiliencia.data.models.neomodel.topic import Topic
from digiliencia.enums.related_fields import (
    all_related_field_values,
    is_valid_related_field,
)
from digiliencia.enums.topics import is_valid_topic

logger = logging.getLogger(__name__)

_VALID_FIELD_VALUES = all_related_field_values()


class News(StructuredNode):
    """News node model."""

    uid = UniqueIdProperty()
    header = StringProperty(required=True)
    date = DateTimeProperty(required=True)
    content = StringProperty(required=True)
    url = StringProperty(required=True)

    # Embedding properties
    header_embedding = ArrayProperty(
        FloatProperty(), default=None
    )  # Track which model was used

    # Relationships
    published_by = RelationshipTo("NewsAgency", "PUBLISHED_BY", cardinality=One)
    written_by = RelationshipTo("Author", "WRITTEN_BY", cardinality=ZeroOrMore)
    topics = RelationshipTo("Topic", "COVERS", cardinality=ZeroOrMore)
    fields = RelationshipTo("Field", "RELATED_TO", cardinality=ZeroOrMore)
    chunks = RelationshipTo("Chunk", "HAS_CHUNK", cardinality=ZeroOrMore)

    @classmethod
    def get_or_create_with_relationships(
        cls,
        header: str,
        date: datetime,
        content: str,
        url: str,
        source_name: str,
        author_names: list[str] | None = None,
        topic_names: list[str] | None = None,
        field_names: list[str] | None = None,
        generate_embeddings: bool = False,
        embedding_service=None,
    ) -> "News":
        """
        Create or get a news item with all its relationships.

        Args:
            header: News headline
            date: Publication date (must be a datetime object)
            content: News content
            url: News URL
            source_name: Name of the news agency
            author_names: List of author names
            topic_names: List of topic names
            field_names: List of field names
            generate_embeddings: Whether to generate embeddings immediately (default: False)
            embedding_service: Optional embedding service to use

        Returns:
            News: The created or existing news instance
        """
        # Ensure 'date' is a datetime object
        if isinstance(date, str):
            try:
                date = datetime.fromisoformat(date)
            except ValueError as e:
                raise ValueError(
                    f"'date' must be a datetime object or a valid ISO 8601 string. Error: {e}"
                )
        elif not isinstance(date, datetime):
            raise TypeError(f"'date' must be a datetime object, got {type(date)}")

        # Check if news already exists
        try:
            existing_news = cls.nodes.get(header=header, date=date)
            return existing_news
        except cls.DoesNotExist:
            pass  # Continue with creation

        # Create or get the news agency
        try:
            news_agency = NewsAgency.nodes.get(name=source_name)
        except NewsAgency.DoesNotExist:
            news_agency = NewsAgency(name=source_name).save()

        # Create the news
        news = cls(header=header, date=date, content=content, url=url).save()

        # Connect to news agency
        news.published_by.connect(news_agency)

        # Connect to authors
        if author_names:
            for author_name in author_names:
                try:
                    author = Author.nodes.get(name=author_name)
                except Author.DoesNotExist:
                    author = Author(name=author_name).save()
                news.written_by.connect(author)

        # Connect to topics: si existen en BD, se conectan independientemente del enum
        # Si no existen, se deja constancia por log para depuración
        if topic_names:
            for topic_name in topic_names:
                try:
                    topic = Topic.nodes.get(name=topic_name)
                    news.topics.connect(topic)
                except Topic.DoesNotExist:
                    if is_valid_topic(topic_name):
                        logger.warning(
                            "Topic válido según enum pero no existente en BD: %s",
                            topic_name,
                        )
                    else:
                        logger.warning(
                            "Topic no reconocido y no existente en BD, omitido: %s",
                            topic_name,
                        )

        # Connect to fields (validación silenciosa con logging)
        if field_names:
            for field_name in field_names:
                if not is_valid_related_field(field_name):
                    logger.warning("Field inválido ignorado: %s", field_name)
                    continue
                try:
                    field = Field.nodes.get(name=field_name)
                    news.fields.connect(field)
                except Field.DoesNotExist:
                    logger.warning(
                        "Field válido según enum pero no existente en BD: %s",
                        field_name,
                    )

        # Generate embeddings if requested
        if generate_embeddings:
            try:
                news.generate_embeddings(embedding_service)
            except Exception as e:
                # Log error but don't fail the entire operation
                logger.warning(
                    f"Failed to generate embeddings for news {news.uid}: {e}"
                )

        return news

    def generate_embeddings(self, embedding_service=None) -> "News":
        """
        Generate and store embeddings for header and content.

        Args:
            embedding_service: Optional EmbeddingService instance. If None, creates a new one.

        Returns:
            News: Self instance with updated embeddings
        """
        if embedding_service is None:
            from digiliencia.models.embedding_manager import EmbeddingManager

            embedding_manager = EmbeddingManager()

            # Generate embeddings - access properties as strings
            header_text = str(self.header) if self.header else ""
            content_text = str(self.content) if self.content else ""

            self.header_embedding = embedding_manager.generate_embedding(header_text)
            self.content_embedding = embedding_manager.generate_embedding(content_text)
        else:
            # Use the provided embedding service
            header_text = str(self.header) if self.header else ""
            content_text = str(self.content) if self.content else ""

            self.header_embedding = embedding_service.embed_one(header_text)
            self.content_embedding = embedding_service.embed_one(content_text)

        self.save()
        return self

    def has_embeddings(self) -> bool:
        """Check if both header and content embeddings exist."""
        return bool(self.header_embedding and self.content_embedding)

    @classmethod
    def get_news_without_embeddings(cls, limit: int = 100):
        """Get news items that don't have embeddings generated."""
        # This is a simplified query - in practice you might want more sophisticated filtering
        return cls.nodes.filter(header_embedding__isnull=True).limit(limit)
