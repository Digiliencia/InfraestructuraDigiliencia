"""Text classification service using RoBERTa-large-mnli model."""

import time
from typing import List, Tuple
from loguru import logger
from transformers import pipeline, Pipeline
import torch

from models import TopicCandidate, TopicResult


class TextClassificationService:
    """Service for classifying text using RoBERTa-large-mnli model."""

    def __init__(self):
        """Initialize the classification service."""
        self.classifier: Pipeline = None
        self.model_name = "roberta-large-mnli"
        self._load_model()

    def _load_model(self) -> None:
        """Load the RoBERTa-large-mnli model."""
        try:
            logger.info(f"Loading {self.model_name} model...")

            # Check if CUDA is available
            device = 0 if torch.cuda.is_available() else -1
            if device == 0:
                logger.info("Using GPU acceleration")
            else:
                logger.info("Using CPU")

            self.classifier = pipeline(
                "zero-shot-classification",
                model=self.model_name,
                device=device,
                return_all_scores=True,
            )

            logger.info(f"Successfully loaded {self.model_name} model")

        except Exception as e:
            logger.error(f"Failed to load model: {e}")
            raise RuntimeError(f"Failed to load classification model: {e}")

    def is_model_loaded(self) -> bool:
        """Check if the model is loaded."""
        return self.classifier is not None

    def classify_text(
        self,
        text: str,
        headline: str,
        topic_candidates: List[TopicCandidate],
        max_topics: int = 5,
        confidence_threshold: float = 0.1,
    ) -> Tuple[List[TopicResult], float]:
        """
        Classify text into topics using zero-shot classification.

        Args:
            text: The main text to classify
            headline: Optional headline text
            topic_candidates: List of possible topics
            max_topics: Maximum number of topics to return
            confidence_threshold: Minimum confidence for topic inclusion

        Returns:
            Tuple of (classified topics, processing time in ms)
        """
        if not self.is_model_loaded():
            raise RuntimeError("Classification model not loaded")

        start_time = time.time()

        try:
            # Combine headline and text if headline is provided
            full_text = f"{headline}\n\n{text}" if headline else text

            # Prepare candidate labels using topic names and definitions
            candidate_labels = []
            label_to_topic = {}

            for topic in topic_candidates:
                # Use topic name as label, but we could also combine with definition
                label = topic.name
                candidate_labels.append(label)
                label_to_topic[label] = topic

            logger.info(f"Classifying text with {len(candidate_labels)} candidate topics")

            # Perform zero-shot classification
            result = self.classifier(full_text, candidate_labels)

            # Process results
            classified_topics: List[TopicResult] = []

            for label, score in zip(result["labels"], result["scores"]):
                if score >= confidence_threshold and len(classified_topics) < max_topics:
                    topic_result = TopicResult(name=label, confidence=float(score))
                    classified_topics.append(topic_result)

            # Sort by confidence (highest first)
            classified_topics.sort(key=lambda x: x.confidence, reverse=True)

            processing_time = (time.time() - start_time) * 1000

            logger.info(
                f"Classification completed in {processing_time:.2f}ms. "
                f"Found {len(classified_topics)} topics above threshold."
            )

            return classified_topics, processing_time

        except Exception as e:
            processing_time = (time.time() - start_time) * 1000
            logger.error(f"Error during classification: {e}")
            raise RuntimeError(f"Classification failed: {e}")

    def get_model_info(self) -> dict:
        """Get information about the loaded model."""
        return {
            "model_name": self.model_name,
            "model_loaded": self.is_model_loaded(),
            "device": "GPU" if torch.cuda.is_available() else "CPU",
            "torch_version": torch.__version__,
        }
