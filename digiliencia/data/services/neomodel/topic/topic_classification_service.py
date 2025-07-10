"""Topic classification service using LLM for cybersecurity news."""

import json
from typing import List

import requests
from loguru import logger

from digiliencia.configs.env import Env
from digiliencia.data.models.neomodel.news import News
from digiliencia.data.models.neomodel.topic import Topic
from digiliencia.data.services.neomodel.config import configure_neomodel
from digiliencia.data.services.neomodel.topic.topic_service import TopicService


class TopicClassificationService:
    """Service for classifying news into cybersecurity topics using LLM."""

    def __init__(self) -> None:
        """Initialize the topic classification service."""
        configure_neomodel()
        self.env = Env()
        self.topic_service = TopicService()

    def classify_news_topics(self, news: News, max_topics: int = 5) -> List[Topic]:
        """
        Classify a news article into cybersecurity topics using LLM.

        Args:
            news: The news article to classify
            max_topics: Maximum number of topics to assign (default: 5)

        Returns:
            List[Topic]: List of topics the news belongs to
        """
        try:
            # Get all available topics from database
            all_topics = self.topic_service.get_all_topics()

            if not all_topics:
                logger.warning("No topics found in database")
                return []

            # Prepare topics information for LLM
            topics_info = []
            for topic in all_topics:
                topics_info.append({"name": topic.name, "definition": topic.definition})

            # Prepare the prompt for LLM
            prompt = self._build_classification_prompt(
                str(news.header), str(news.content), topics_info, max_topics
            )

            # Call LLM API
            classified_topics = self._call_llm_api(prompt)

            # Filter and return valid topics
            return self._filter_valid_topics(classified_topics, all_topics)

        except Exception as e:
            logger.error(f"Error classifying news topics: {e}")
            return []

    def _build_classification_prompt(
        self, headline: str, content: str, topics_info: List[dict], max_topics: int
    ) -> str:
        """
        Build the classification prompt for the LLM.

        Args:
            headline: News headline
            content: News content
            topics_info: List of available topics with their definitions
            max_topics: Maximum number of topics to assign

        Returns:
            str: The formatted prompt
        """
        topics_text = "\n".join([f"- {topic['name']}" for topic in topics_info])

        prompt = f"""
You are a cybersecurity expert. Analyze the following news article and classify it into the most relevant cybersecurity topics from the provided list.

AVAILABLE TOPICS:
{topics_text}

INSTRUCTIONS:
1. Analyze the news content carefully
2. Select the most relevant topics (maximum {max_topics}) that best describe the article
3. Return ONLY a JSON array with the topic names
4. If no topics are clearly relevant, return an empty array
5. Do not include any explanations or additional text - ONLY the JSON array

RESPONSE FORMAT:
["topic1", "topic2", "topic3"]

NEWS ARTICLE:
Headline: {headline}
Content: {content}

JSON ARRAY:
"""
        print(prompt)  # Debugging: print the prompt to console
        return prompt

    def _call_llm_api(self, prompt: str) -> List[str]:
        """
        Call the LLM API to classify the news.

        Args:
            prompt: The classification prompt

        Returns:
            List[str]: List of classified topic names
        """
        try:
            # Prepare the request payload for Ollama API
            payload = {
                "model": "qwen3:14b",
                "prompt": prompt,
                "stream": False,
                "options": {"temperature": 0.1, "top_p": 0.9, "max_tokens": 2000},
            }

            # Make API call
            response = requests.post(
                f"{self.env.llm_url}/api/generate",
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=60000,
            )

            if response.status_code != 200:
                logger.error(f"LLM API error: {response.status_code} - {response.text}")
                return []

            # Parse response
            response_data = response.json()
            llm_response = response_data.get("response", "").strip()

            # Try to parse as JSON
            try:
                topics = json.loads(llm_response)
                if isinstance(topics, list):
                    return topics
                else:
                    logger.warning(f"LLM response is not a list: {llm_response}")
                    return []
            except json.JSONDecodeError:
                # Try to extract JSON array from the response
                try:
                    # Look for JSON array pattern in the response
                    import re

                    json_pattern = r"\[.*?\]"
                    matches = re.findall(json_pattern, llm_response, re.DOTALL)

                    if matches:
                        # Try to parse the last JSON-like match (most likely the final result)
                        for match in reversed(matches):
                            try:
                                topics = json.loads(match)
                                if isinstance(topics, list):
                                    logger.info(
                                        f"Extracted JSON from LLM response: {match}"
                                    )
                                    return topics
                            except json.JSONDecodeError:
                                continue

                    logger.error(
                        f"Failed to extract JSON array from LLM response: {llm_response}"
                    )
                    return []
                except Exception as e:
                    logger.error(f"Error extracting JSON from LLM response: {e}")
                    return []

        except requests.exceptions.RequestException as e:
            logger.error(f"Request error calling LLM API: {e}")
            return []
        except Exception as e:
            logger.error(f"Unexpected error calling LLM API: {e}")
            return []

    def _filter_valid_topics(
        self, classified_topics: List[str], all_topics: List[Topic]
    ) -> List[Topic]:
        """
        Filter and return only valid topics that exist in the database.

        Args:
            classified_topics: List of topic names returned by LLM
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
