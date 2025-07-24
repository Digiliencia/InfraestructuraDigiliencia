import json
from typing import List

import requests
from loguru import logger

from data.models.neomodel.field import Field
from data.services.neomodel.field.field_service import FieldService
from digiliencia.configs.env import Env
from models.prompts.field_classification_prompt import FieldClassificationPrompt
from digiliencia.utils.llm import LLMUtils


class FieldClassificationService:
    def __init__(self, ollama_url="http://localhost:11434/api/generate"):
        self.field_service = FieldService()
        self.fields = self.field_service.get_all()
        self.fields_hierarchy = self.field_service.get_fields_hierarchy()
        self.ollama_url = ollama_url

    def classify_news_fields(self, news, max_fields: int = 10) -> List[Field]:
        text = str(news.content)
        prompt = FieldClassificationPrompt.generate_news_classification_prompt(
            fields=self.fields_hierarchy, text=text, max_fields=max_fields
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
            selected = LLMUtils.extract_json_from_response(answer)
            if not selected:
                return []

            # Validate that it's a list
            if not isinstance(selected, list):
                logger.error(f"Response is not a list: {type(selected)}")
                return []

            # Map names to Topic objects
            name_to_obj = {
                str(t.name): t for t in self.fields
            }  # Convert to string explicitly
            valid_fields = []
            for field_name in selected:
                if isinstance(field_name, str) and field_name in name_to_obj:
                    valid_fields.append(name_to_obj[field_name])
                else:
                    logger.warning(f"Invalid or not found field: {field_name}")

            return valid_fields[:max_fields]  # Ensure it doesn't exceed the maximum

        except requests.exceptions.RequestException as e:
            logger.error(f"Connection error with Ollama: {e}")
            return []
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON from Ollama: {e}")
            return []
        except Exception as e:
            logger.error(f"Unexpected error classifying topics: {e}")
            return []
