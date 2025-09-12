import json
from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, List, TypeVar

import requests
from loguru import logger

from digiliencia.configs.env import Env
from digiliencia.utils.llm import LLMUtils

T = TypeVar("T")


class BaseClassificationService(ABC, Generic[T]):
    """Abstract base class for classification services that use Ollama LLM."""

    def __init__(self, ollama_url: str = "http://localhost:11434/api/generate"):
        """
        Initialize the base classification service.

        Args:
            ollama_url: URL for the Ollama API endpoint
        """
        self.ollama_url = ollama_url
        self._initialize_data()

    @abstractmethod
    def _initialize_data(self) -> None:
        """Initialize service-specific data. Must be implemented by subclasses."""
        pass

    @abstractmethod
    def _generate_prompt(self, text: str, max_items: int) -> str:
        """
        Generate classification prompt for the given text.

        Args:
            text: Text to classify
            max_items: Maximum number of items to classify

        Returns:
            Generated prompt string
        """
        pass

    @abstractmethod
    def _get_name_to_object_mapping(self) -> Dict[str, T]:
        """
        Get mapping from name strings to objects.

        Returns:
            Dictionary mapping names to objects
        """
        pass

    @abstractmethod
    def _get_entity_type_name(self) -> str:
        """
        Get the name of the entity type for logging purposes.

        Returns:
            Entity type name (e.g., "topic", "field")
        """
        pass

    def _create_ollama_payload(self, prompt: str) -> Dict[str, Any]:
        """
        Create payload for Ollama API request.

        Args:
            prompt: The prompt to send to Ollama

        Returns:
            Dictionary containing the payload
        """
        return {
            "model": Env().classification_model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0,
            },
        }

    def _send_ollama_request(self, payload: Dict[str, Any]) -> str:
        """
        Send request to Ollama API and return the response.

        Args:
            payload: Request payload

        Returns:
            Response text from Ollama

        Raises:
            requests.exceptions.RequestException: If request fails
            ValueError: If response format is invalid
        """
        response = requests.post(self.ollama_url, json=payload, timeout=60000)
        response.raise_for_status()

        response_data = response.json()
        if "response" not in response_data:
            raise ValueError("Ollama response does not contain 'response' field")

        answer = response_data["response"].strip()
        if not answer:
            raise ValueError("Ollama response is empty")

        logger.debug(f"Ollama response: {answer}")
        return answer

    def _extract_and_validate_json(self, response_text: str) -> List[str]:
        """
        Extract and validate JSON from Ollama response.

        Args:
            response_text: Raw response text from Ollama

        Returns:
            List of selected item names

        Raises:
            ValueError: If JSON extraction or validation fails
        """
        selected = LLMUtils.extract_json_from_response(response_text)
        if selected is None:
            raise ValueError("Could not extract JSON from response")

        if not isinstance(selected, list):
            raise ValueError(f"Response is not a list: {type(selected)}")

        return selected

    def _map_names_to_objects(
        self, selected_names: List[str], max_items: int
    ) -> List[T]:
        """
        Map selected names to their corresponding objects.

        Args:
            selected_names: List of selected names
            max_items: Maximum number of items to return

        Returns:
            List of mapped objects
        """
        name_to_obj = self._get_name_to_object_mapping()
        entity_type = self._get_entity_type_name()

        valid_objects = []
        for name in selected_names:
            if isinstance(name, str) and name in name_to_obj:
                valid_objects.append(name_to_obj[name])
            else:
                logger.warning(f"Invalid or not found {entity_type}: {name}")

        return valid_objects[:max_items]

    def classify_news(self, news: Any, max_items: int) -> List[T]:
        """
        Classify news content into categories.

        Args:
            news: News object containing content to classify
            max_items: Maximum number of items to return

        Returns:
            List of classified objects
        """
        try:
            text = str(news.content)
            prompt = self._generate_prompt(text, max_items)
            payload = self._create_ollama_payload(prompt)

            response_text = self._send_ollama_request(payload)
            selected_names = self._extract_and_validate_json(response_text)

            return self._map_names_to_objects(selected_names, max_items)

        except requests.exceptions.RequestException as e:
            logger.error(f"Connection error with Ollama: {e}")
            return []
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON from Ollama: {e}")
            return []
        except ValueError as e:
            logger.error(f"Validation error: {e}")
            return []
        except Exception as e:
            entity_type = self._get_entity_type_name()
            logger.error(f"Unexpected error classifying {entity_type}s: {e}")
            return []
