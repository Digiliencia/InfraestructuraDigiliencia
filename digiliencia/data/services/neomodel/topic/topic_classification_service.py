"""Topic classification service using microservice with RoBERTa-large-mnli for cybersecurity news."""

from typing import List

import requests
from loguru import logger

from digiliencia.configs.env import Env
from digiliencia.data.models.neomodel.news import News
from digiliencia.data.models.neomodel.topic import Topic
from digiliencia.data.services.neomodel.config import configure_neomodel
from digiliencia.data.services.neomodel.topic.topic_service import TopicService


class TopicClassificationService:
    """Service for classifying news into cybersecurity topics using RoBERTa-large-mnli microservice."""

    def __init__(self) -> None:
        """Initialize the topic classification service."""
        configure_neomodel()
        self.env = Env()
        self.topic_service = TopicService()
        self._request_timeout = 120  # 2 minutes timeout for classification requests

    def classify_news_topics(
        self, news: News, max_topics: int = 5, confidence_threshold: float = 0.1
    ) -> List[Topic]:
        """
        Classify a news article into cybersecurity topics using RoBERTa-large-mnli microservice.

        Args:
            news: The news article to classify
            max_topics: Maximum number of topics to assign (default: 5)
            confidence_threshold: Minimum confidence score for topic inclusion (default: 0.1)

        Returns:
            List[Topic]: List of topics the news belongs to
        """
        try:
            # Get all available topics from database
            all_topics = self.topic_service.get_all_topics()

            if not all_topics:
                logger.warning("No topics found in database")
                return []

            # Prepare topics information for the microservice
            topic_candidates = []
            for topic in all_topics:
                topic_candidates.append(
                    {"name": topic.name, "definition": topic.definition or ""}
                )

            # Call the classification microservice
            classified_topic_names = self._call_classification_service(
                headline=str(news.header),
                content=str(news.content),
                topic_candidates=topic_candidates,
                max_topics=max_topics,
                confidence_threshold=confidence_threshold,
            )

            # Filter and return valid topics
            return self._filter_valid_topics(classified_topic_names, all_topics)

        except Exception as e:
            logger.error(f"Error classifying news topics: {e}")
            return []

    def _call_classification_service(
        self,
        headline: str,
        content: str,
        topic_candidates: List[dict],
        max_topics: int = 5,
        confidence_threshold: float = 0.1,
    ) -> List[str]:
        """
        Call the classification microservice to classify the news.

        Args:
            headline: The news headline
            content: The news content
            topic_candidates: List of topic candidates with name and definition
            max_topics: Maximum number of topics to return
            confidence_threshold: Minimum confidence score for topic inclusion

        Returns:
            List[str]: List of classified topic names
        """
        try:
            # Prepare the request payload
            payload = {
                "text": content,
                "headline": headline,
                "topic_candidates": topic_candidates,
                "max_topics": max_topics,
                "confidence_threshold": confidence_threshold,
            }

            # Make API call to the classification microservice
            response = requests.post(
                f"{self.env.classification_service_url}/classify",
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=self._request_timeout,
            )

            if response.status_code != 200:
                logger.error(
                    f"Classification service error: {response.status_code} - {response.text}"
                )
                return []

            # Parse response
            response_data = response.json()

            # Extract topic names from the response
            topics = response_data.get("topics", [])
            topic_names = [topic["name"] for topic in topics]

            processing_time = response_data.get("processing_time_ms", 0)
            logger.info(
                f"Classification completed in {processing_time:.2f}ms. "
                f"Found {len(topic_names)} topics: {topic_names}"
            )

            return topic_names

        except requests.exceptions.Timeout:
            logger.error("Classification service request timed out")
            return []
        except requests.exceptions.ConnectionError:
            logger.error("Failed to connect to classification service")
            return []
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error calling classification service: {e}")
            return []
        except Exception as e:
            logger.error(f"Unexpected error calling classification service: {e}")
            return []

    def check_service_health(self) -> bool:
        """
        Check if the classification microservice is healthy and ready.

        Returns:
            bool: True if service is healthy, False otherwise
        """
        try:
            response = requests.get(
                f"{self.env.classification_service_url}/health", timeout=10
            )

            if response.status_code == 200:
                health_data = response.json()
                is_healthy = health_data.get("status") == "healthy" and health_data.get(
                    "model_loaded", False
                )
                logger.info(f"Classification service health check: {health_data}")
                return is_healthy
            else:
                logger.warning(
                    f"Classification service health check failed: {response.status_code}"
                )
                return False

        except Exception as e:
            logger.error(f"Failed to check classification service health: {e}")
            return False

    def _filter_valid_topics(
        self, classified_topics: List[str], all_topics: List[Topic]
    ) -> List[Topic]:
        """
        Filter and return only valid topics that exist in the database.

        Args:
            classified_topics: List of topic names returned by classification service
            all_topics: List of all available topics from database

        Returns:
            List[Topic]: List of valid topic objects
        """
        valid_topics = []
        topic_name_to_object = {topic.name: topic for topic in all_topics}

        for topic_name in classified_topics:
            if topic_name in topic_name_to_object:
                valid_topics.append(topic_name_to_object[topic_name])
            else:
                logger.warning(f"Topic '{topic_name}' not found in database")

        return valid_topics

    def get_news_topics(self, news: News) -> List[Topic]:
        """
        Get all topics that a news article covers.

        Args:
            news: The news article

        Returns:
            List[Topic]: List of topics the news covers
        """
        return list(news.covers.all())  # type: ignore
