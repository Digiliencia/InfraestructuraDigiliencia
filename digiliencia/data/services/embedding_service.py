"""Service for making embedding generation requests (DRY principle)."""

import os
from typing import List, Optional

import requests
from loguru import logger


class EmbeddingService:
    """
    Service for making requests to the embedding generation API.
    Centralizes logic for DRY and OOP best practices.
    Supports both custom API and Ollama providers.
    """

    def __init__(
        self,
        service_url: Optional[str] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None,
    ):
        """
        Initialize the embedding service.

        Args:
            service_url: URL of the embedding service (defaults to EMBEDDINGS_SERVICE env var)
            provider: Provider type ('custom' or 'ollama', defaults to EMBEDDINGS_PROVIDER env var)
            model: Model name for Ollama (defaults to EMBEDDINGS_MODEL env var)
        """
        self.service_url: str = (
            service_url if service_url is not None else os.getenv("EMBEDDINGS_SERVICE", "")
        )
        self.provider: str = (
            provider if provider is not None else os.getenv("EMBEDDINGS_PROVIDER", "custom")
        )
        self.model: str = (
            model if model is not None else os.getenv("EMBEDDINGS_MODEL", "")
        )

        if not self.service_url:
            logger.error("EMBEDDINGS_SERVICE environment variable not set")
            raise ValueError("EMBEDDINGS_SERVICE environment variable not set")

        if self.provider == "ollama" and not self.model:
            logger.error("EMBEDDINGS_MODEL environment variable not set for Ollama provider")
            raise ValueError("EMBEDDINGS_MODEL environment variable not set for Ollama provider")

        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

        logger.info(f"EmbeddingService initialized with provider: {self.provider}, model: {self.model}")

    def generate_embeddings(self, texts: List[str]) -> Optional[List]:
        """
        Request embeddings for a list of texts.

        Args:
            texts (List[str]): List of texts to embed.
        Returns:
            Optional[List]: List of embeddings or None if failed.
        """
        if self.provider == "ollama":
            return self._generate_embeddings_ollama(texts)
        else:
            return self._generate_embeddings_custom(texts)

    def _generate_embeddings_custom(self, texts: List[str]) -> Optional[List]:
        """
        Request embeddings from custom API.

        Args:
            texts (List[str]): List of texts to embed.
        Returns:
            Optional[List]: List of embeddings or None if failed.
        """
        try:
            logger.debug(f"Requesting embeddings from custom API for {len(texts)} texts")
            response = self.session.post(self.service_url, json={"texts": texts})
            response.raise_for_status()
            embeddings = response.json().get("embeddings")
            if embeddings is None:
                logger.error("No embeddings returned from custom service")
            return embeddings
        except requests.RequestException as e:
            logger.error(f"Custom embedding service request failed: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error in custom embedding service: {e}")
            return None

    def _generate_embeddings_ollama(self, texts: List[str]) -> Optional[List]:
        """
        Request embeddings from Ollama API.

        Args:
            texts (List[str]): List of texts to embed.
        Returns:
            Optional[List]: List of embeddings or None if failed.
        """
        try:
            logger.debug(f"Requesting embeddings from Ollama for {len(texts)} texts")
            
            embeddings = []
            # Ollama API requires one text at a time for embeddings
            for text in texts:
                response = self.session.post(
                    f"{self.service_url}/api/embed",
                    json={"model": self.model, "input": text}
                )
                response.raise_for_status()
                result = response.json()
                embedding = result.get("embeddings")
                
                # Ollama returns embeddings as a list with one element
                if embedding and len(embedding) > 0:
                    embeddings.append(embedding[0])
                else:
                    logger.error(f"No embedding returned from Ollama for text: {text[:50]}...")
                    return None
            
            logger.debug(f"Successfully received {len(embeddings)} embeddings from Ollama")
            return embeddings
            
        except requests.RequestException as e:
            logger.error(f"Ollama embedding service request failed: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error in Ollama embedding service: {e}")
            return None

    def close(self):
        """Close the HTTP session."""
        self.session.close()
