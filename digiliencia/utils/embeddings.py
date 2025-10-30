"""
Custom embeddings implementation for llama-index using internal embeddings service.

This module provides a custom embedding class that connects to the internal
embeddings microservice API.
"""

from typing import Any, List

import requests
from llama_index.core.bridge.pydantic import PrivateAttr
from llama_index.core.embeddings import BaseEmbedding
from loguru import logger


class CustomAPIEmbedding(BaseEmbedding):
    """
    Custom embedding class that uses the internal embeddings microservice.
    
    This class integrates with the FastAPI embeddings service running at
    EMBEDDINGS_SERVICE endpoint (default: http://localhost:8000/embed).
    
    The service uses sentence-transformers models to generate embeddings.
    """
    
    # Private attributes for API configuration
    _api_url: str = PrivateAttr()
    _timeout: int = PrivateAttr()
    _embedding_dimension: int = PrivateAttr()
    
    def __init__(
        self,
        api_url: str,
        embed_batch_size: int = 16,
        timeout: int = 60,
        embedding_dimension: int = 1024,
        **kwargs: Any,
    ) -> None:
        """
        Initialize the custom API embedding client.
        
        Args:
            api_url: Full URL to the embeddings API endpoint (e.g., "http://localhost:8000/embed")
            embed_batch_size: Number of texts to embed in a single batch
            timeout: Request timeout in seconds
            embedding_dimension: Dimension of the embedding vectors
            **kwargs: Additional arguments passed to BaseEmbedding
        """
        # Ensure model_name is set to avoid OpenAI fallback
        if 'model_name' not in kwargs:
            kwargs['model_name'] = 'custom-api-embedding'
        
        super().__init__(
            embed_batch_size=embed_batch_size,
            **kwargs,
        )
        self._api_url = api_url
        self._timeout = timeout
        self._embedding_dimension = embedding_dimension
        
        logger.info(f"CustomAPIEmbedding initialized with API: {api_url}, dimension: {embedding_dimension}")
    
    @classmethod
    def class_name(cls) -> str:
        """Return the class name for serialization."""
        return "CustomAPIEmbedding"
    
    def _call_api(self, texts: List[str]) -> List[List[float]]:
        """
        Call the embeddings API to get embeddings for texts.
        
        Args:
            texts: List of texts to embed
            
        Returns:
            List of embedding vectors
            
        Raises:
            requests.RequestException: If the API call fails
        """
        try:
            payload = {"texts": texts}
            
            logger.debug(f"Calling embeddings API with {len(texts)} texts")
            
            response = requests.post(
                self._api_url,
                json=payload,
                timeout=self._timeout,
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()
            
            result = response.json()
            embeddings = result.get("embeddings", [])
            
            if not embeddings:
                raise ValueError("API returned empty embeddings")
            
            logger.debug(f"Successfully received {len(embeddings)} embeddings from API")
            
            return embeddings
            
        except requests.RequestException as e:
            logger.error(f"Error calling embeddings API: {e}")
            raise
        except (KeyError, ValueError) as e:
            logger.error(f"Error parsing API response: {e}")
            raise
    
    def _get_query_embedding(self, query: str) -> List[float]:
        """
        Get embedding for a single query.
        
        Args:
            query: Query text to embed
            
        Returns:
            Embedding vector
        """
        return self._call_api([query])[0]
    
    def _get_text_embedding(self, text: str) -> List[float]:
        """
        Get embedding for a single text.
        
        Args:
            text: Text to embed
            
        Returns:
            Embedding vector
        """
        return self._call_api([text])[0]
    
    def _get_text_embeddings(self, texts: List[str]) -> List[List[float]]:
        """
        Get embeddings for multiple texts in batches.
        
        Args:
            texts: List of texts to embed
            
        Returns:
            List of embedding vectors
        """
        # Process in batches according to embed_batch_size
        all_embeddings: List[List[float]] = []
        
        for i in range(0, len(texts), self.embed_batch_size):
            batch = texts[i:i + self.embed_batch_size]
            batch_embeddings = self._call_api(batch)
            all_embeddings.extend(batch_embeddings)
        
        return all_embeddings
    
    async def _aget_query_embedding(self, query: str) -> List[float]:
        """
        Async version of _get_query_embedding.
        
        Note: Currently wraps the synchronous version.
        For true async support, use aiohttp instead of requests.
        
        Args:
            query: Query text to embed
            
        Returns:
            Embedding vector
        """
        # For now, just call the sync version
        # TODO: Implement true async with aiohttp if needed
        return self._get_query_embedding(query)
    
    async def _aget_text_embedding(self, text: str) -> List[float]:
        """
        Async version of _get_text_embedding.
        
        Args:
            text: Text to embed
            
        Returns:
            Embedding vector
        """
        return self._get_text_embedding(text)
