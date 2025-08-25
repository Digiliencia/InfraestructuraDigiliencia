"""Complex neomodel models."""

from datetime import datetime

from neomodel import (
    DateTimeProperty,
    One,
    RelationshipTo,
    StringProperty,
    StructuredNode,
    UniqueIdProperty,
    ZeroOrMore,
)

from digiliencia.data.models.neomodel.field import Field
from digiliencia.data.models.neomodel.organization.news_agency import NewsAgency
from digiliencia.data.models.neomodel.person.author import Author
from digiliencia.data.models.neomodel.topic import Topic


class News(StructuredNode):
    """News node model."""

    uid = UniqueIdProperty()
    header = StringProperty(required=True)
    date = DateTimeProperty(required=True)
    content = StringProperty(required=True)
    url = StringProperty(required=True)

    # Relationships
    published_by = RelationshipTo("NewsAgency", "PUBLISHED_BY", cardinality=One)
    written_by = RelationshipTo("Author", "WRITTEN_BY", cardinality=ZeroOrMore)
    topics = RelationshipTo("Topic", "COVERS", cardinality=ZeroOrMore)
    fields = RelationshipTo("Field", "RELATED_TO", cardinality=ZeroOrMore)

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

        # Connect to topics
        if topic_names:
            for topic_name in topic_names:
                try:
                    topic = Topic.nodes.get(name=topic_name)
                    news.topics.connect(topic)
                except Topic.DoesNotExist:
                    pass

        # Connect to fields if provided
        if field_names:
            for field_name in field_names:
                try:
                    field = Field.nodes.get(name=field_name)
                    news.fields.connect(field)
                except Field.DoesNotExist:
                    pass

        return news
