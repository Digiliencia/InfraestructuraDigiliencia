import json
from typing import List
from loguru import logger

class LLMUtils:
    """Has utilities for handling LLM responses."""
    
    @staticmethod
    def extract_json_from_response(response_text: str) -> List[str]:
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
