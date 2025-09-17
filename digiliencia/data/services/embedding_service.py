"""Service for making embedding generation requests (DRY principle)."""

import os
import requests
from loguru import logger
from typing import List, Optional


class EmbeddingService:
    """
    Service for making requests to the embedding generation API.
    Centralizes logic for DRY and OOP best practices.
    """

    def __init__(self, service_url: Optional[str] = None):
        url = (
            service_url if service_url is not None else os.getenv("EMBEDDINGS_SERVICE")
        )
        if not url:
            logger.error("EMBEDDINGS_SERVICE environment variable not set")
            raise ValueError("EMBEDDINGS_SERVICE environment variable not set")
        self.service_url: str = url
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def generate_embeddings(self, texts: List[str]) -> Optional[List]:
        """
        Request embeddings for a list of texts.

        Args:
            texts (List[str]): List of texts to embed.
        Returns:
            Optional[List]: List of embeddings or None if failed.
        """
        try:
            response = self.session.post(self.service_url, json={"texts": texts})
            response.raise_for_status()
            embeddings = response.json().get("embeddings")
            if embeddings is None:
                logger.error("No embeddings returned from service")
            return embeddings
        except requests.RequestException as e:
            logger.error(f"Embedding service request failed: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error in embedding service: {e}")
            return None

    def close(self):
        self.session.close()
