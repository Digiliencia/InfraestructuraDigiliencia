import json
from typing import List

import requests
from loguru import logger

from digiliencia.data.models.neomodel.topic import Topic
from digiliencia.data.services.neomodel.topic.topic_service import TopicService


class TopicClassificationService:
    def __init__(self, ollama_url="http://localhost:11434/api/generate"):
        self.topic_service = TopicService()
        self.db_topics = self.topic_service.get_all_topics()
        self.topics = [str(t.name) for t in self.db_topics]  # Convert to string explicitly
        self.ollama_url = ollama_url

    def classify_news_topics(self, news, max_topics: int = 5) -> List[Topic]:
        text = str(news.content)
        prompt = f"""Classify the following news article into these categories: {', '.join(self.topics)}.
Text: "{text}"

Return ONLY a JSON list with the most relevant category names (maximum {max_topics}).
Expected format: ["category1", "category2", "category3"]
Do not include additional explanations, only valid JSON.
"""
        payload = {
            "model": "gemma3:12b",
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0,
            }
        }
        try:
            response = requests.post(self.ollama_url, json=payload, timeout=30)
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
            name_to_obj = {str(t.name): t for t in self.db_topics}  # Convert to string explicitly
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
        """Extracts a JSON list from Ollama's response, handling additional text."""
        response_text = response_text.strip()
        
        # Find the first [ and the last ]
        start_idx = response_text.find('[')
        end_idx = response_text.rfind(']')
        
        if start_idx == -1 or end_idx == -1 or start_idx >= end_idx:
            logger.error(f"No valid JSON found in response: {response_text}")
            return []
        
        json_str = response_text[start_idx:end_idx + 1]
        
        try:
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing extracted JSON '{json_str}': {e}")
            return []
