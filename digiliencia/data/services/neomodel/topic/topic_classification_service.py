import json
from typing import List

import requests
from loguru import logger

from digiliencia.configs.env import Env
from digiliencia.data.models.neomodel.topic import Topic
from digiliencia.data.services.neomodel.topic.topic_service import TopicService
from digiliencia.models.prompts.topic_classification_prompt import (
    TopicClassificationPrompt,
)


class TopicClassificationService:
    def __init__(self, ollama_url="http://localhost:11434/api/generate"):
        self.topic_service = TopicService()
        self.db_topics = self.topic_service.get_all_topics()
        self.topics = [
            str(t.name) for t in self.db_topics
        ]  # Convert to string explicitly
        self.ollama_url = ollama_url

    def classify_news_topics(self, news, max_topics: int = 5) -> List[Topic]:
        text = str(news.content)
        prompt = TopicClassificationPrompt.generate_news_classification_prompt(
            topics=self.topics, text=text, max_topics=max_topics
        )
        payload = {
            "model": Env().classification_model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0,
            },
        }
        try:
            response = requests.post(self.ollama_url, json=payload, timeout=60000)
            response.raise_for_status()

            response_data = response.json()
            if "response" not in response_data:
                logger.error("Ollama response does not contain 'response' field")
                return []

            answer = response_data["response"].strip()
            if not answer:
                logger.error("Ollama response is empty")
                return []

            logger.debug(f"Ollama response: {answer}")

            # Try to extract JSON from the response
            selected = self._extract_json_from_response(answer)
            if not selected:
                return []

            # Validate that it's a list
            if not isinstance(selected, list):
                logger.error(f"Response is not a list: {type(selected)}")
                return []

            # Map names to Topic objects
            name_to_obj = {
                str(t.name): t for t in self.db_topics
            }  # Convert to string explicitly
            valid_topics = []
            for topic_name in selected:
                if isinstance(topic_name, str) and topic_name in name_to_obj:
                    valid_topics.append(name_to_obj[topic_name])
                else:
                    logger.warning(f"Invalid or not found topic: {topic_name}")

            return valid_topics[:max_topics]  # Ensure it doesn't exceed the maximum

        except requests.exceptions.RequestException as e:
            logger.error(f"Connection error with Ollama: {e}")
            return []
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON from Ollama: {e}")
            return []
        except Exception as e:
            logger.error(f"Unexpected error classifying topics: {e}")
            return []

    def _extract_json_from_response(self, response_text: str) -> List[str]:
        """Extracts the last valid JSON list from Ollama's response, handling reasoning text with multiple JSONs."""
        response_text = response_text.strip()

        # Find all potential JSON arrays by looking for [ and ] pairs
        potential_jsons = []

        # Find all occurrences of [ and ]
        bracket_positions = []
        for i, char in enumerate(response_text):
            if char in ["[", "]"]:
                bracket_positions.append((i, char))

        # Find all valid JSON array candidates (matching [ and ] pairs)
        stack = []
        for pos, bracket in bracket_positions:
            if bracket == "[":
                stack.append(pos)
            elif bracket == "]" and stack:
                start_pos = stack.pop()
                potential_jsons.append((start_pos, pos))

        if not potential_jsons:
            logger.error(f"No JSON arrays found in response: {response_text}")
            return []

        # Try to parse JSONs from the last to the first until we find a valid one
        potential_jsons.sort(
            key=lambda x: x[1], reverse=True
        )  # Sort by end position, descending

        for start_idx, end_idx in potential_jsons:
            json_str = response_text[start_idx : end_idx + 1]
            try:
                parsed = json.loads(json_str)
                if isinstance(parsed, list):
                    logger.debug(f"Successfully parsed last JSON: {json_str}")
                    return parsed
                else:
                    logger.debug(f"JSON is not a list, trying previous: {json_str}")
                    continue
            except json.JSONDecodeError:
                logger.debug(f"Failed to parse JSON, trying previous: {json_str}")
                continue

        logger.error(f"No valid JSON list found in response: {response_text}")
        return []
