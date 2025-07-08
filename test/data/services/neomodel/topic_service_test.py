from digiliencia.data.models.neomodel.topic import Topic
from digiliencia.data.services.neomodel.topic.topic_service import TopicService


def test_create_topic(topic_service: TopicService):
    """Test creating a topic."""
    topic = topic_service.create_topic("Test Topic", "Test definition", "https://example.com/test-topic")

    assert isinstance(topic, Topic)
    assert topic.name == "Test Topic"
    assert topic.definition == "Test definition"


def test_create_duplicate_topic(topic_service: TopicService):
    """Test creating a duplicate topic returns existing one."""
    topic1 = topic_service.create_topic("Duplicate Topic", "First definition", "https://example.com/duplicate1")
    topic2 = topic_service.create_topic("Duplicate Topic", "Second definition", "https://example.com/duplicate2")

    # Should return the same topic (first one created)
    assert topic1.uid == topic2.uid
    assert topic1.definition == "First definition"  # Original definition preserved


def test_get_topic_by_name(topic_service: TopicService):
    """Test retrieving topic by name."""
    created_topic = topic_service.create_topic("Searchable Topic", "Definition", "https://example.com/searchable")
    retrieved_topic = topic_service.get_topic_by_name("Searchable Topic")

    assert retrieved_topic is not None
    assert retrieved_topic.uid == created_topic.uid
    assert retrieved_topic.name == created_topic.name


def test_get_nonexistent_topic(topic_service: TopicService):
    """Test retrieving nonexistent topic."""
    topic = topic_service.get_topic_by_name("Nonexistent Topic")
    assert topic is None


def test_get_all_topics(topic_service: TopicService):
    """Test retrieving all topics."""
    initial_count = len(topic_service.get_all_topics())

    topic_service.create_topic("Topic A", "Description A", "https://example.com/topic-a")
    topic_service.create_topic("Topic B", "Description B", "https://example.com/topic-b")

    all_topics = topic_service.get_all_topics()
    assert len(all_topics) >= initial_count + 2

    # Verify our topics are in the results
    topic_names = [topic.name for topic in all_topics]
    assert "Topic A" in topic_names
    assert "Topic B" in topic_names
