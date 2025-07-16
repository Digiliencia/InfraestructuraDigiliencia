import json

import pytest
import requests

from digiliencia.data.services.neomodel.topic.topic_classification_service import (
    TopicClassificationService,
)


@pytest.fixture
def mock_topics():
    """Create mock Topic objects for testing."""
    topics = []
    topic_names = [
        "Cybersecurity",
        "Artificial Intelligence",
        "Data Privacy",
        "Cloud Computing",
    ]

    for i, name in enumerate(topic_names):
        # Create a simple object with the required attributes
        topic = type(
            "MockTopic",
            (),
            {
                "uid": f"uid_{i}",
                "name": name,
                "definition": f"Definition for {name}",
                "url": f"https://example.com/{name.lower().replace(' ', '-')}",
            },
        )()
        topics.append(topic)

    return topics


@pytest.fixture
def mock_topic_service(mock_topics):
    """Create a mock TopicService."""

    class MockTopicService:
        def get_all_topics(self):
            return mock_topics

    return MockTopicService()


@pytest.fixture
def topic_classification_service(mock_topic_service, monkeypatch):
    """Create TopicClassificationService with mocked dependencies."""

    def mock_topic_service_init(*args, **kwargs):
        return mock_topic_service

    monkeypatch.setattr(
        "digiliencia.data.services.neomodel.topic.topic_classification_service.TopicService",
        mock_topic_service_init,
    )
    service = TopicClassificationService()
    return service


@pytest.fixture
def mock_news():
    """Create a mock news object."""

    class MockNews:
        def __init__(self):
            self.content = "This article discusses the latest developments in artificial intelligence and cybersecurity measures for protecting sensitive data."

    return MockNews()


def test_init(mock_topic_service, monkeypatch):
    """Test service initialization."""

    def mock_topic_service_init(*args, **kwargs):
        return mock_topic_service

    monkeypatch.setattr(
        "digiliencia.data.services.neomodel.topic.topic_classification_service.TopicService",
        mock_topic_service_init,
    )

    service = TopicClassificationService("http://test-ollama:11434/api/generate")

    assert service.ollama_url == "http://test-ollama:11434/api/generate"
    assert service.topic_service == mock_topic_service
    assert len(service.topics) == 4
    assert "Cybersecurity" in service.topics
    assert "Artificial Intelligence" in service.topics


def create_mock_response(
    json_return_value=None, raise_for_status_effect=None, json_side_effect=None
):
    """Helper function to create mock response objects."""

    class MockResponse:
        def __init__(self):
            self._json_return_value = json_return_value
            self._raise_for_status_effect = raise_for_status_effect
            self._json_side_effect = json_side_effect

        def json(self):
            if self._json_side_effect:
                raise self._json_side_effect
            return self._json_return_value

        def raise_for_status(self):
            if self._raise_for_status_effect:
                raise self._raise_for_status_effect

    return MockResponse()


def test_classify_news_topics_success(
    topic_classification_service, mock_news, monkeypatch
):
    """Test successful topic classification."""
    # Mock successful Ollama response
    mock_response = create_mock_response(
        json_return_value={"response": '["Artificial Intelligence", "Cybersecurity"]'}
    )

    called_args = []

    def mock_post(*args, **kwargs):
        called_args.append((args, kwargs))
        return mock_response

    monkeypatch.setattr("requests.post", mock_post)

    result = topic_classification_service.classify_news_topics(mock_news, max_topics=3)

    # Verify the request was made correctly
    assert len(called_args) == 1
    call_args = called_args[0]
    assert call_args[1]["json"]["model"] is not None
    assert "prompt" in call_args[1]["json"]
    assert call_args[1]["json"]["stream"] is False
    assert call_args[1]["json"]["options"]["temperature"] == 0

    # Verify the result
    assert len(result) == 2
    assert result[0].name == "Artificial Intelligence"
    assert result[1].name == "Cybersecurity"


def test_classify_news_topics_with_max_topics_limit(
    topic_classification_service, mock_news, monkeypatch
):
    """Test that max_topics limit is respected."""
    # Mock response with more topics than max_topics
    mock_response = create_mock_response(
        json_return_value={
            "response": '["Artificial Intelligence", "Cybersecurity", "Data Privacy", "Cloud Computing"]'
        }
    )

    def mock_post(*args, **kwargs):
        return mock_response

    monkeypatch.setattr("requests.post", mock_post)

    result = topic_classification_service.classify_news_topics(mock_news, max_topics=2)

    assert len(result) == 2


def test_classify_news_topics_invalid_topic_names(
    topic_classification_service, mock_news, monkeypatch
):
    """Test handling of invalid topic names in response."""
    # Mock response with invalid topic names
    mock_response = create_mock_response(
        json_return_value={
            "response": '["Artificial Intelligence", "Invalid Topic", "Cybersecurity"]'
        }
    )

    def mock_post(*args, **kwargs):
        return mock_response

    monkeypatch.setattr("requests.post", mock_post)

    result = topic_classification_service.classify_news_topics(mock_news)

    # Should only return valid topics
    assert len(result) == 2
    assert all(
        topic.name in ["Artificial Intelligence", "Cybersecurity"] for topic in result
    )


def test_classify_news_topics_connection_error(
    topic_classification_service, mock_news, monkeypatch
):
    """Test handling of connection errors."""

    def mock_post(*args, **kwargs):
        raise requests.exceptions.ConnectionError("Connection failed")

    monkeypatch.setattr("requests.post", mock_post)

    result = topic_classification_service.classify_news_topics(mock_news)

    assert result == []


def test_classify_news_topics_timeout_error(
    topic_classification_service, mock_news, monkeypatch
):
    """Test handling of timeout errors."""

    def mock_post(*args, **kwargs):
        raise requests.exceptions.Timeout("Request timed out")

    monkeypatch.setattr("requests.post", mock_post)

    result = topic_classification_service.classify_news_topics(mock_news)

    assert result == []


def test_classify_news_topics_http_error(
    topic_classification_service, mock_news, monkeypatch
):
    """Test handling of HTTP errors."""
    mock_response = create_mock_response(
        raise_for_status_effect=requests.exceptions.HTTPError("500 Server Error")
    )

    def mock_post(*args, **kwargs):
        return mock_response

    monkeypatch.setattr("requests.post", mock_post)

    result = topic_classification_service.classify_news_topics(mock_news)

    assert result == []


def test_classify_news_topics_missing_response_field(
    topic_classification_service, mock_news, monkeypatch
):
    """Test handling of missing 'response' field in Ollama response."""
    mock_response = create_mock_response(json_return_value={"error": "Some error"})

    def mock_post(*args, **kwargs):
        return mock_response

    monkeypatch.setattr("requests.post", mock_post)

    result = topic_classification_service.classify_news_topics(mock_news)

    assert result == []


def test_classify_news_topics_empty_response(
    topic_classification_service, mock_news, monkeypatch
):
    """Test handling of empty response."""
    mock_response = create_mock_response(json_return_value={"response": ""})

    def mock_post(*args, **kwargs):
        return mock_response

    monkeypatch.setattr("requests.post", mock_post)

    result = topic_classification_service.classify_news_topics(mock_news)

    assert result == []


def test_classify_news_topics_invalid_json_response(
    topic_classification_service, mock_news, monkeypatch
):
    """Test handling of invalid JSON in response."""
    mock_response = create_mock_response(
        json_return_value={"response": "invalid json response"}
    )

    def mock_post(*args, **kwargs):
        return mock_response

    monkeypatch.setattr("requests.post", mock_post)

    result = topic_classification_service.classify_news_topics(mock_news)

    assert result == []


def test_classify_news_topics_non_list_response(
    topic_classification_service, mock_news, monkeypatch
):
    """Test handling of non-list JSON response."""
    mock_response = create_mock_response(
        json_return_value={"response": '{"topic": "Cybersecurity"}'}
    )

    def mock_post(*args, **kwargs):
        return mock_response

    monkeypatch.setattr("requests.post", mock_post)

    result = topic_classification_service.classify_news_topics(mock_news)

    assert result == []


def test_extract_json_from_response_valid_json(topic_classification_service):
    """Test extracting valid JSON from response."""
    response_text = (
        'Here are the topics: ["Cybersecurity", "AI"] based on the analysis.'
    )

    result = topic_classification_service._extract_json_from_response(response_text)

    assert result == ["Cybersecurity", "AI"]


def test_extract_json_from_response_only_json(topic_classification_service):
    """Test extracting JSON when response contains only JSON."""
    response_text = '["Cybersecurity", "Data Privacy"]'

    result = topic_classification_service._extract_json_from_response(response_text)

    assert result == ["Cybersecurity", "Data Privacy"]


def test_extract_json_from_response_no_brackets(topic_classification_service):
    """Test handling response without brackets."""
    response_text = "Cybersecurity, Data Privacy"

    result = topic_classification_service._extract_json_from_response(response_text)

    assert result == []


def test_extract_json_from_response_malformed_json(topic_classification_service):
    """Test handling malformed JSON."""
    response_text = '["Cybersecurity", "Data Privacy"'  # Missing closing bracket

    result = topic_classification_service._extract_json_from_response(response_text)

    assert result == []


def test_extract_json_from_response_nested_brackets(topic_classification_service):
    """Test extracting JSON with nested content - should fail due to extra content."""
    response_text = 'Analysis shows ["Cybersecurity", "AI"] and ["Data"] are relevant.'

    result = topic_classification_service._extract_json_from_response(response_text)

    # Should return empty list because there's extra content after the JSON
    assert result == []


def test_extract_json_from_response_clean_json_with_text(topic_classification_service):
    """Test extracting clean JSON surrounded by text."""
    response_text = 'Based on the analysis, the topics are: ["Cybersecurity", "AI"]. These are the most relevant.'

    result = topic_classification_service._extract_json_from_response(response_text)

    assert result == ["Cybersecurity", "AI"]


def test_classify_news_topics_json_decode_error(
    topic_classification_service, mock_news, monkeypatch
):
    """Test handling of JSON decode error from requests."""
    mock_response = create_mock_response(
        json_side_effect=json.JSONDecodeError("Invalid JSON", "", 0)
    )

    def mock_post(*args, **kwargs):
        return mock_response

    monkeypatch.setattr("requests.post", mock_post)

    result = topic_classification_service.classify_news_topics(mock_news)

    assert result == []


def test_classify_news_topics_unexpected_error(
    topic_classification_service, mock_news, monkeypatch
):
    """Test handling of unexpected errors."""

    def mock_post(*args, **kwargs):
        raise Exception("Unexpected error")

    monkeypatch.setattr("requests.post", mock_post)

    result = topic_classification_service.classify_news_topics(mock_news)

    assert result == []


def test_classify_news_topics_with_whitespace_in_response(
    topic_classification_service, mock_news, monkeypatch
):
    """Test handling response with extra whitespace."""
    mock_response = create_mock_response(
        json_return_value={
            "response": '  \n  ["Cybersecurity", "Artificial Intelligence"]  \n  '
        }
    )

    def mock_post(*args, **kwargs):
        return mock_response

    monkeypatch.setattr("requests.post", mock_post)

    result = topic_classification_service.classify_news_topics(mock_news)

    assert len(result) == 2
    assert result[0].name == "Cybersecurity"
    assert result[1].name == "Artificial Intelligence"


def test_topics_conversion_to_string(mock_topic_service, monkeypatch):
    """Test that topic names are properly converted to strings."""

    def mock_topic_service_init(*args, **kwargs):
        return mock_topic_service

    monkeypatch.setattr(
        "digiliencia.data.services.neomodel.topic.topic_classification_service.TopicService",
        mock_topic_service_init,
    )

    service = TopicClassificationService()

    # Verify all topics are strings
    assert all(isinstance(topic, str) for topic in service.topics)
