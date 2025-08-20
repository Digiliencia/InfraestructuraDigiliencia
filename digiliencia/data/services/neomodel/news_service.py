"""News service for managing news using neomodel."""

import os
from datetime import datetime
from typing import List, Optional

import requests
from loguru import logger

from digiliencia.data.models.neomodel.field import Field
from digiliencia.data.models.neomodel.news import News
from digiliencia.data.models.neomodel.topic import Topic
from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.data.services.neomodel.config import configure_neomodel


class NewsService:
    """Service for managing news using neomodel."""

    def __init__(self) -> None:
        """Initialize the news service."""
        configure_neomodel()

    def create_from_scraped_data(self, scraped_data: ScrapedNews) -> News:
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

    def get_all_news_without_topics(self) -> List[News]:
        """
        Get all news items without topics.

        Returns:
            List[News]: List of news items without topics
        """
        return [news for news in News.nodes.all() if not news.topics]

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

    def set_topics_relations(self, news: News, topics: List[Topic]):
        """
        Set topics relationships for the given news.

        Args:
            topics: List of Topic instances to relate to news
        """
        for topic in topics:
            news.topics.connect(topic)  # type: ignore
            logger.info(f"Connected topic {topic.name} to news {news.header}")

    def set_fields_relations(self, news: News, fields: List[Field]):
        """
        Set fields relationships for the given news.

        Args:
            fields: List of Field instances to relate to news
        """
        for field in fields:
            news.fields.connect(field)
            logger.info(f"Connected field {field.name} to news {news.header}")

    def get_all_news_without_fields(self) -> List[News]:
        """
        Get all news items without fields.

        Returns:
            List[News]: List of news items without fields
        """
        return [news for news in News.nodes.all() if not news.fields]

    def generate_embeddings_for_all_news(self):
        """
        Generate embeddings for all news items.

        Args:
            embedding_service: Optional EmbeddingService instance. If None, creates a new one.
        """
        news_items = self.get_all_news()
        for news in news_items:
            # Get the embeddings service URL from environment
            embeddings_service_url = os.getenv("EMBEDDINGS_SERVICE")
            if not embeddings_service_url:
                logger.error("EMBEDDINGS_SERVICE_URL environment variable not set")
                continue

            try:
                # CONTENT
                # Prepare the request payload
                payload = {"texts": [news.header, news.content]}

                # Make POST request to embeddings service
                response = requests.post(
                    embeddings_service_url,
                    json=payload,
                    headers={"Content-Type": "application/json"},
                )
                response.raise_for_status()

                # Extract embedding from response
                embeddings = response.json().get("embeddings")

                if embeddings:
                    news.header_embedding = embeddings[0]
                    news.content_embedding = embeddings[1]
                    news.save()
                    logger.info(f"Generated embeddings for news: {news.header}")
                else:
                    logger.error(f"No embeddings returned for news: {news.header}")

            except requests.RequestException as e:
                logger.error(f"Error generating embeddings for news {news.header}: {e}")
            except Exception as e:
                logger.error(
                    f"Unexpected error generating embeddings for news {news.header}: {e}"
                )
