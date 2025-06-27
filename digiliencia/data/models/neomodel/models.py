"""Complex neomodel models."""

from datetime import datetime

from neomodel import (
    DateTimeProperty,
    One,
    RelationshipFrom,
    RelationshipTo,
    StringProperty,
    StructuredNode,
    UniqueIdProperty,
    ZeroOrMore,
)

from .base_models import NewsAgency, Person, Topic


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
    covers = RelationshipTo("Topic", "COVERS", cardinality=ZeroOrMore)

    class Meta:
        app_label = "digiliencia"

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
    ) -> "News":
        """
        Create or get a news item with all its relationships.

        Args:
            header: News headline
            date: Publication date
            content: News content
            url: News URL
            source_name: Name of the news agency
            author_names: List of author names
            topic_names: List of topic names

        Returns:
            News: The created or existing news instance
        """
        # Check if news already exists (by header and date combination)
        existing_news = cls.nodes.filter(header=header, date=date).first()
        if existing_news:
            return existing_news

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
                # Only connect to existing topics, don't create new ones
                topic = Topic.nodes.filter(name=topic_name).first()
                if topic:
                    news.covers.connect(topic)

        return news


class Author(Person):
    """Author node model that extends Person."""

    # Relationships
    wrote = RelationshipFrom("News", "WRITTEN_BY", cardinality=ZeroOrMore)
