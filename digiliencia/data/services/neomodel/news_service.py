"""News service for managing news using neomodel."""

import gc
import os
from datetime import datetime
from typing import Iterable, List, Optional

import requests
from loguru import logger

from digiliencia.data.models.neomodel.field import Field
from digiliencia.data.models.neomodel.news import News
from digiliencia.data.models.neomodel.topic import Topic
from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.data.services.neomodel.chunk_service import ChunkService
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
            news.fields.connect(field)  # type: ignore[attr-defined]
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

    def generate_embeddings_for_unembedded_news(
        self, limit: Optional[int] = None, batch_size: int = 10
    ):
        """
        Generate embeddings for news items that don't have embeddings yet.
        Optimized for local GPU processing with memory management.

        Args:
            limit: Maximum number of news items to process. If None, processes all.
            batch_size: Number of news items to process before forcing garbage collection.
        """
        # Get the embeddings service URL from environment first
        embeddings_service_url = os.getenv("EMBEDDINGS_SERVICE")
        if not embeddings_service_url:
            logger.error("EMBEDDINGS_SERVICE environment variable not set")
            return

        # Use a session for connection reuse
        with requests.Session() as session:
            session.headers.update({"Content-Type": "application/json"})

            processed_count = 0
            failed_count = 0
            batch_count = 0

            # Process news items in a memory-efficient way
            # Instead of loading all at once, iterate and check one by one
            for news in News.nodes.all():
                # Check limit early to avoid unnecessary processing
                if limit and processed_count >= limit:
                    break

                # Skip if already has embeddings (double-check to avoid race conditions)
                if news.has_embeddings():
                    continue

                try:
                    # Prepare the request payload
                    payload = {"texts": [news.header, news.content]}

                    # Make POST request to embeddings service using the session
                    response = session.post(embeddings_service_url, json=payload)
                    response.raise_for_status()

                    # Extract embedding from response
                    embeddings = response.json().get("embeddings")

                    if embeddings and len(embeddings) >= 2:
                        news.header_embedding = embeddings[0]
                        news.content_embedding = embeddings[1]
                        news.save()
                        processed_count += 1

                        # Log progress less frequently to reduce memory overhead
                        if processed_count % 5 == 0 or processed_count == 1:
                            logger.info(
                                f"Generated embeddings for {processed_count} news items (latest: {news.header[:50]}...)"
                            )
                    else:
                        failed_count += 1
                        logger.warning(
                            f"No embeddings returned for news: {news.header[:50]}..."
                        )

                except requests.RequestException as e:
                    failed_count += 1
                    logger.error(
                        f"Network error for news {news.header[:50]}...: {str(e)[:100]}"
                    )
                except Exception as e:
                    failed_count += 1
                    logger.error(
                        f"Unexpected error for news {news.header[:50]}...: {str(e)[:100]}"
                    )

                # Force garbage collection every batch_size items to free GPU/system memory
                batch_count += 1
                if batch_count >= batch_size:
                    gc.collect()
                    batch_count = 0
                    logger.debug(
                        f"Memory cleanup after processing {processed_count + failed_count} items"
                    )

            # Final cleanup
            gc.collect()

            if processed_count > 0:
                logger.info(
                    f"Embedding generation completed. Processed: {processed_count}, Failed: {failed_count}"
                )
            else:
                logger.info("No news items found without embeddings")

    # ---------------------- Chunking and embeddings for chunks ----------------------
    def _split_text_into_chunks(
        self,
        text: str,
        max_chars: int = 800,
        overlap: int = 100,
        preserve_newlines: bool = True,
    ) -> List[str]:
        """Split text into overlapping chunks by characters.

        Args:
            text: Full text to split.
            max_chars: Maximum characters per chunk.
            overlap: Characters to overlap between consecutive chunks.
            preserve_newlines: If True, tries to split on whitespace/newlines close to boundaries.
        """
        if not text:
            return []
        s = text if preserve_newlines else " ".join(text.split())
        chunks: List[str] = []
        start = 0
        n = len(s)
        if max_chars <= 0:
            max_chars = 800
        if overlap < 0:
            overlap = 0
        while start < n:
            end = min(n, start + max_chars)
            # try to cut at a whitespace near the end
            if preserve_newlines and end < n:
                window = s[start:end]
                cut = window.rfind("\n")
                if cut == -1:
                    cut = window.rfind(". ")
                if cut == -1:
                    cut = window.rfind(" ")
                if cut != -1 and cut > max(
                    0, len(window) - 120
                ):  # only if near boundary
                    end = start + cut + 1
            chunks.append(s[start:end].strip())
            if end == n:
                break
            start = max(0, end - overlap)
        return [c for c in chunks if c]

    def _batch(self, items: Iterable[str], size: int) -> Iterable[List[str]]:
        buf: List[str] = []
        for it in items:
            buf.append(it)
            if len(buf) >= size:
                yield buf
                buf = []
        if buf:
            yield buf

    def generate_chunk_embeddings_for_news(
        self,
        news: News,
        *,
        kind: str = "content",
        chunk_size: int = 800,
        overlap: int = 100,
        batch_size: int = 16,
        include_header: bool = True,
        force_regenerate: bool = False,
    ) -> int:
        # Delegate to ChunkService to avoid duplication
        return ChunkService().generate_chunk_embeddings_for_news(
            news,
            kind=kind,
            chunk_size=chunk_size,
            overlap=overlap,
            batch_size=batch_size,
            include_header=include_header,
            force_regenerate=force_regenerate,
        )

    def generate_chunks_for_all_news(
        self,
        limit: Optional[int] = None,
        *,
        only_missing: bool = True,
        chunk_size: int = 800,
        overlap: int = 100,
        include_header: bool = True,
        batch_size: int = 16,
    ) -> int:
        """Generate chunks + embeddings for all (or up to limit) news.

        Returns number of news processed (with at least one chunk created/updated).
        """
        return ChunkService().generate_chunks_for_all_news(
            limit=limit,
            only_missing=only_missing,
            chunk_size=chunk_size,
            overlap=overlap,
            include_header=include_header,
            batch_size=batch_size,
        )

    def generate_embeddings_for_missing_chunks(
        self,
        limit: Optional[int] = None,
        batch_size: int = 32,
    ) -> int:
        """Generate embeddings for all Chunk nodes that don't have embedding yet.

        Returns number of chunks updated.
        """
        return ChunkService().generate_embeddings_for_missing_chunks(
            limit=limit,
            batch_size=batch_size,
        )
