"""Topic service for managing topics using neomodel."""

from typing import List, Optional

from digiliencia.data.models.neomodel.topic import Topic
from digiliencia.data.services.neomodel.config import configure_neomodel


class TopicService:
    """Service for managing topics using neomodel."""

    def __init__(self) -> None:
        """Initialize the topic service."""
        configure_neomodel()

    def create_topic(self, name: str, definition: str = "", url: str = "") -> Topic:
        """
        Create a topic.

        Args:
            name: Topic name
            definition: Topic definition
            url: Topic URL

        Returns:
            Topic: The created topic instance
        """
        try:
            return Topic.nodes.get(name=name)
        except Topic.DoesNotExist:
            return Topic(name=name, definition=definition, url=url).save()

    def get_topic_by_name(self, name: str) -> Optional[Topic]:
        """
        Get a topic by name.

        Args:
            name: Topic name

        Returns:
            Topic: The topic instance or None if not found
        """
        try:
            return Topic.nodes.get(name=name)
        except Topic.DoesNotExist:
            return None

    def get_all_topics(self) -> List[Topic]:
        """
        Get all topics.

        Returns:
            List[Topic]: List of all topics
        """
        return list(Topic.nodes.all())
