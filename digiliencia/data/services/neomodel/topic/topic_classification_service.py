"""Topic classification service using microservice with RoBERTa-large-mnli for cybersecurity news."""

import os
from typing import List

import torch
from loguru import logger
from transformers import pipeline

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
        self.classifier = pipeline(
            "zero-shot-classification",
            model="facebook/bart-large-mnli",
            device=0 if torch.cuda.is_available() else -1,
        )

        pipe = self.classifier
        print(pipe.model.device)

        self.db_topics = self.topic_service.get_all_topics()
        if not self.db_topics:
            logger.error("No topics found in database, classification will not work")
        self.topics = [topic.name for topic in self.db_topics]

    def classify_news_topics(
        self, news: News, max_topics: int = 5, confidence_threshold: float = 0.1
    ) -> List[Topic]:
        """
        Classify a news article into cybersecurity topics using RoBERTa-large-mnli.
        Args:
            news: The news article to classify
            max_topics: Maximum number of topics to assign (default: 5)
            confidence_threshold: Minimum confidence score for topic inclusion (default: 0.1)

        Returns:
            List[Topic]: List of topics the news belongs to
        """
        try:
            # Convert news content to string (handle neomodel properties)
            text = str(news.content)

            # Classify the news content
            result = self.classifier(
                text,
                self.topics,
                hypothesis_template="This text is about {}",
                multi_label=True,
            )

            # Tomar sólo los top‑N con score > umbral (por ejemplo > 0.2)
            selected = [
                lbl for lbl, sc in zip(result["labels"], result["scores"]) if sc > 0.2
            ][:max_topics]
            # Filtrar los Topic objetos existentes
            name_to_obj = {t.name: t for t in self.db_topics}
            return [name_to_obj[n] for n in selected if n in name_to_obj]

        except Exception as e:
            logger.error(f"Error classifying topics for news '{news.header}': {e}")
            return []
