from typing import Dict, List

from digiliencia.agents.prompts.topic_classification_prompt import \
    TopicClassificationPrompt
from digiliencia.data.models.neomodel.topic import Topic
from digiliencia.data.services.neomodel.base_classification_service import \
    BaseClassificationService
from digiliencia.data.services.neomodel.topic.topic_service import TopicService


class TopicClassificationService(BaseClassificationService[Topic]):
    def _initialize_data(self) -> None:
        """Initialize topic-specific data."""
        self.topic_service = TopicService()
        self.db_topics = self.topic_service.get_all_topics()
        self.topics = [str(t.name) for t in self.db_topics]

    def _generate_prompt(self, text: str, max_items: int) -> str:
        """Generate topic classification prompt."""
        return TopicClassificationPrompt.generate_news_classification_prompt(
            topics=self.topics, text=text, max_topics=max_items
        )

    def _get_name_to_object_mapping(self) -> Dict[str, Topic]:
        """Get mapping from topic names to Topic objects."""
        return {str(t.name): t for t in self.db_topics}

    def _get_entity_type_name(self) -> str:
        """Get entity type name for logging."""
        return "topic"

    def classify_news_topics(self, news, max_topics: int = 5) -> List[Topic]:
        """
        Classify news content into topics.

        Args:
            news: News object containing content to classify
            max_topics: Maximum number of topics to return

        Returns:
            List of classified Topic objects
        """
        return self.classify_news(news, max_topics)
