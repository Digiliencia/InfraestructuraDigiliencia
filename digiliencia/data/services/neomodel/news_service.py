"""News service for managing news using neomodel."""

from datetime import datetime
from typing import List, Optional

from loguru import logger

from digiliencia.data.models.neomodel.news import News
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
