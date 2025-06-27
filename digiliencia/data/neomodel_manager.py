"""Unified neomodel models and services."""

from datetime import datetime
from typing import List, Optional

from loguru import logger
from neomodel import (
    DateTimeProperty,
    One,
    RelationshipFrom,
    RelationshipTo,
    StringProperty,
    StructuredNode,
    UniqueIdProperty,
    ZeroOrMore,
    config,
)
from pydantic import BaseModel, ConfigDict, HttpUrl

from digiliencia.configs.env import Env


def configure_neomodel() -> None:
    """Configure neomodel with database settings."""
    env = Env()

    # Get database configuration directly from environment
    uri = env.ddbb_uri
    config.DATABASE_URL = uri


# Pydantic models for validation
class ScrapedNewsData(BaseModel):
    """Pydantic model for scraped news data validation."""

    header: str
    date: datetime
    source: str
    content: str
    url: HttpUrl
    authors: List[str]
    topics: Optional[List[str]] = None

    model_config = ConfigDict(str_strip_whitespace=True, validate_assignment=True)


# Neomodel node classes
class Person(StructuredNode):
    """Person node model."""

    uid = UniqueIdProperty()
    name = StringProperty(required=True, unique_index=True)
    email = StringProperty()
    description = StringProperty()


class Topic(StructuredNode):
    """Topic node model."""

    uid = UniqueIdProperty()
    name = StringProperty(required=True, unique_index=True)
    definition = StringProperty()


class Organization(StructuredNode):
    """Organization base node model."""

    uid = UniqueIdProperty()
    name = StringProperty(required=True, unique_index=True)
    description = StringProperty()


class NewsAgency(Organization):
    """News agency node model that inherits from Organization."""

    pass


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
        try:
            existing_news = cls.nodes.filter(header=header, date=date).first()
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
                # Only connect to existing topics, don't create new ones
                try:
                    topic = Topic.nodes.get(name=topic_name)
                    news.covers.connect(topic)
                except Topic.DoesNotExist:
                    pass  # Skip if topic doesn't exist

        return news


class Author(Person):
    """Author node model that extends Person."""

    # Relationships
    wrote = RelationshipFrom("News", "WRITTEN_BY", cardinality=ZeroOrMore)


# Service classes
class NewsService:
    """Service for managing news using neomodel."""

    def __init__(self) -> None:
        """Initialize the news service."""
        configure_neomodel()

    def create_from_scraped_data(self, scraped_data: ScrapedNewsData) -> News:
        """
        Create a news item from scraped data.

        Args:
            scraped_data: Validated scraped news data

        Returns:
            News: The created news instance
        """
        try:
            return News.get_or_create_with_relationships(
                header=scraped_data.header,
                date=scraped_data.date,
                content=scraped_data.content,
                url=str(scraped_data.url),
                source_name=scraped_data.source,
                author_names=scraped_data.authors,
                topic_names=scraped_data.topics,
            )
        except Exception as e:
            logger.error(f"Error creating news from scraped data: {e}")
            raise

    def create_news(
        self,
        header: str,
        date: datetime,
        content: str,
        url: str,
        source_name: str,
        author_names: Optional[List[str]] = None,
        topic_names: Optional[List[str]] = None,
    ) -> News:
        """
        Create a news item.

        Args:
            header: News headline
            date: Publication date
            content: News content
            url: News URL
            source_name: Name of the news agency
            author_names: List of author names
            topic_names: List of topic names

        Returns:
            News: The created news instance
        """
        return News.get_or_create_with_relationships(
            header=header,
            date=date,
            content=content,
            url=url,
            source_name=source_name,
            author_names=author_names or [],
            topic_names=topic_names or [],
        )

    def get_news_by_id(self, uid: str) -> Optional[News]:
        """
        Get a news item by its UID.

        Args:
            uid: The unique identifier

        Returns:
            News: The news instance or None if not found
        """
        try:
            return News.nodes.get(uid=uid)
        except News.DoesNotExist:
            return None

    def get_all_news(self) -> List[News]:
        """
        Get all news items.

        Returns:
            List[News]: List of all news items
        """
        return list(News.nodes.all())

    def update_news(
        self,
        uid: str,
        header: Optional[str] = None,
        content: Optional[str] = None,
        url: Optional[str] = None,
    ) -> Optional[News]:
        """
        Update a news item.

        Args:
            uid: The unique identifier
            header: New header (optional)
            content: New content (optional)
            url: New URL (optional)

        Returns:
            News: The updated news instance or None if not found
        """
        try:
            news = News.nodes.get(uid=uid)
            if header is not None:
                news.header = header
            if content is not None:
                news.content = content
            if url is not None:
                news.url = url
            news.save()
            return news
        except News.DoesNotExist:
            return None

    def delete_news(self, uid: str) -> bool:
        """
        Delete a news item.

        Args:
            uid: The unique identifier

        Returns:
            bool: True if deleted, False if not found
        """
        try:
            news = News.nodes.get(uid=uid)
            news.delete()
            return True
        except News.DoesNotExist:
            return False


class TopicService:
    """Service for managing topics using neomodel."""

    def __init__(self) -> None:
        """Initialize the topic service."""
        configure_neomodel()

    def create_topic(self, name: str, definition: str = "") -> Topic:
        """
        Create a topic.

        Args:
            name: Topic name
            definition: Topic definition

        Returns:
            Topic: The created topic instance
        """
        try:
            return Topic.nodes.get(name=name)
        except Topic.DoesNotExist:
            return Topic(name=name, definition=definition).save()

    def get_topic_by_name(self, name: str) -> Optional[Topic]:
        """
        Get a topic by name.

        Args:
            name: Topic name

        Returns:
            Topic: The topic instance or None if not found
        """
        try:
            return Topic.nodes.get(name=name)
        except Topic.DoesNotExist:
            return None

    def get_all_topics(self) -> List[Topic]:
        """
        Get all topics.

        Returns:
            List[Topic]: List of all topics
        """
        return list(Topic.nodes.all())


class AuthorService:
    """Service for managing authors using neomodel."""

    def __init__(self) -> None:
        """Initialize the author service."""
        configure_neomodel()

    def create_author(
        self, name: str, email: str = "", description: str = ""
    ) -> Author:
        """
        Create an author.

        Args:
            name: Author name
            email: Author email
            description: Author description

        Returns:
            Author: The created author instance
        """
        try:
            return Author.nodes.get(name=name)
        except Author.DoesNotExist:
            return Author(name=name, email=email, description=description).save()

    def get_author_by_name(self, name: str) -> Optional[Author]:
        """
        Get an author by name.

        Args:
            name: Author name

        Returns:
            Author: The author instance or None if not found
        """
        try:
            return Author.nodes.get(name=name)
        except Author.DoesNotExist:
            return None

    def get_all_authors(self) -> List[Author]:
        """
        Get all authors.

        Returns:
            List[Author]: List of all authors
        """
        return list(Author.nodes.all())
