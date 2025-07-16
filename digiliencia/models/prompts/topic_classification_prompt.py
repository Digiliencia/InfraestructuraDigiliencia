"""
Prompt for topic classification using LLM models.
"""
from typing import List


class TopicClassificationPrompt:
    """Handles prompt generation for topic classification tasks."""
    
    @staticmethod
    def generate_news_classification_prompt(topics: List[str], text: str, max_topics: int = 5) -> str:
        """
        Generates a prompt for classifying news articles into topics.
        
        Args:
            topics: List of available topic names
            text: The news article content to classify
            max_topics: Maximum number of topics to return
            
        Returns:
            Formatted prompt string for the LLM
        """
        prompt = f"""Classify the following news article into these categories: {', '.join(topics)}.
Text: "{text}"

Return ONLY a JSON list with the most relevant category names (maximum {max_topics}).
Expected format: ["category1", "category2", "category3"]
Do not include additional explanations, only valid JSON.
"""
        return prompt
