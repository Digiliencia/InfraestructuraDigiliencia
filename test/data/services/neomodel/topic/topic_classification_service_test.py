import json
from unittest.mock import Mock, patch

import pytest
import requests

from digiliencia.data.models.neomodel.topic import Topic
from digiliencia.data.services.neomodel.topic.topic_classification_service import TopicClassificationService


@pytest.fixture
def mock_topics():
    """Create mock Topic objects for testing."""
    topics = []
    topic_names = ["Cybersecurity", "Artificial Intelligence", "Data Privacy", "Cloud Computing"]
    
    for i, name in enumerate(topic_names):
        topic = Mock(spec=Topic)
        topic.uid = f"uid_{i}"
        topic.name = name
        topic.definition = f"Definition for {name}"
        topic.url = f"https://example.com/{name.lower().replace(' ', '-')}"
        topics.append(topic)
    
    return topics


@pytest.fixture
def mock_topic_service(mock_topics):
    """Create a mock TopicService."""
    service = Mock()
    service.get_all_topics.return_value = mock_topics
    return service


@pytest.fixture
def topic_classification_service(mock_topic_service):
    """Create TopicClassificationService with mocked dependencies."""
    with patch('digiliencia.data.services.neomodel.topic.topic_classification_service.TopicService') as mock_service_class:
        mock_service_class.return_value = mock_topic_service
        service = TopicClassificationService()
        return service


@pytest.fixture
def mock_news():
    """Create a mock news object."""
    news = Mock()
    news.content = "This article discusses the latest developments in artificial intelligence and cybersecurity measures for protecting sensitive data."
    return news


class TestTopicClassificationService:
    """Test suite for TopicClassificationService."""

    def test_init(self, mock_topic_service):
        """Test service initialization."""
        with patch('digiliencia.data.services.neomodel.topic.topic_classification_service.TopicService') as mock_service_class:
            mock_service_class.return_value = mock_topic_service
            
            service = TopicClassificationService("http://test-ollama:11434/api/generate")
            
            assert service.ollama_url == "http://test-ollama:11434/api/generate"
            assert service.topic_service == mock_topic_service
            assert len(service.topics) == 4
            assert "Cybersecurity" in service.topics
            assert "Artificial Intelligence" in service.topics

    @patch('requests.post')
    def test_classify_news_topics_success(self, mock_post, topic_classification_service, mock_news):
        """Test successful topic classification."""
        # Mock successful Ollama response
        mock_response = Mock()
        mock_response.json.return_value = {
            "response": '["Artificial Intelligence", "Cybersecurity"]'
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        result = topic_classification_service.classify_news_topics(mock_news, max_topics=3)

        # Verify the request was made correctly
        mock_post.assert_called_once()
        call_args = mock_post.call_args
        assert call_args[1]['json']['model'] is not None
        assert 'prompt' in call_args[1]['json']
        assert call_args[1]['json']['stream'] is False
        assert call_args[1]['json']['options']['temperature'] == 0

        # Verify the result
        assert len(result) == 2
        assert result[0].name == "Artificial Intelligence"
        assert result[1].name == "Cybersecurity"

    @patch('requests.post')
    def test_classify_news_topics_with_max_topics_limit(self, mock_post, topic_classification_service, mock_news):
        """Test that max_topics limit is respected."""
        # Mock response with more topics than max_topics
        mock_response = Mock()
        mock_response.json.return_value = {
            "response": '["Artificial Intelligence", "Cybersecurity", "Data Privacy", "Cloud Computing"]'
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        result = topic_classification_service.classify_news_topics(mock_news, max_topics=2)

        assert len(result) == 2

    @patch('requests.post')
    def test_classify_news_topics_invalid_topic_names(self, mock_post, topic_classification_service, mock_news):
        """Test handling of invalid topic names in response."""
        # Mock response with invalid topic names
        mock_response = Mock()
        mock_response.json.return_value = {
            "response": '["Artificial Intelligence", "Invalid Topic", "Cybersecurity"]'
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        result = topic_classification_service.classify_news_topics(mock_news)

        # Should only return valid topics
        assert len(result) == 2
        assert all(topic.name in ["Artificial Intelligence", "Cybersecurity"] for topic in result)

    @patch('requests.post')
    def test_classify_news_topics_connection_error(self, mock_post, topic_classification_service, mock_news):
        """Test handling of connection errors."""
        mock_post.side_effect = requests.exceptions.ConnectionError("Connection failed")

        result = topic_classification_service.classify_news_topics(mock_news)

        assert result == []

    @patch('requests.post')
    def test_classify_news_topics_timeout_error(self, mock_post, topic_classification_service, mock_news):
        """Test handling of timeout errors."""
        mock_post.side_effect = requests.exceptions.Timeout("Request timed out")

        result = topic_classification_service.classify_news_topics(mock_news)

        assert result == []

    @patch('requests.post')
    def test_classify_news_topics_http_error(self, mock_post, topic_classification_service, mock_news):
        """Test handling of HTTP errors."""
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("500 Server Error")
        mock_post.return_value = mock_response

        result = topic_classification_service.classify_news_topics(mock_news)

        assert result == []

    @patch('requests.post')
    def test_classify_news_topics_missing_response_field(self, mock_post, topic_classification_service, mock_news):
        """Test handling of missing 'response' field in Ollama response."""
        mock_response = Mock()
        mock_response.json.return_value = {"error": "Some error"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        result = topic_classification_service.classify_news_topics(mock_news)

        assert result == []

    @patch('requests.post')
    def test_classify_news_topics_empty_response(self, mock_post, topic_classification_service, mock_news):
        """Test handling of empty response."""
        mock_response = Mock()
        mock_response.json.return_value = {"response": ""}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        result = topic_classification_service.classify_news_topics(mock_news)

        assert result == []

    @patch('requests.post')
    def test_classify_news_topics_invalid_json_response(self, mock_post, topic_classification_service, mock_news):
        """Test handling of invalid JSON in response."""
        mock_response = Mock()
        mock_response.json.return_value = {"response": "invalid json response"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        result = topic_classification_service.classify_news_topics(mock_news)

        assert result == []

    @patch('requests.post')
    def test_classify_news_topics_non_list_response(self, mock_post, topic_classification_service, mock_news):
        """Test handling of non-list JSON response."""
        mock_response = Mock()
        mock_response.json.return_value = {"response": '{"topic": "Cybersecurity"}'}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        result = topic_classification_service.classify_news_topics(mock_news)

        assert result == []

    def test_extract_json_from_response_valid_json(self, topic_classification_service):
        """Test extracting valid JSON from response."""
        response_text = 'Here are the topics: ["Cybersecurity", "AI"] based on the analysis.'
        
        result = topic_classification_service._extract_json_from_response(response_text)
        
        assert result == ["Cybersecurity", "AI"]

    def test_extract_json_from_response_only_json(self, topic_classification_service):
        """Test extracting JSON when response contains only JSON."""
        response_text = '["Cybersecurity", "Data Privacy"]'
        
        result = topic_classification_service._extract_json_from_response(response_text)
        
        assert result == ["Cybersecurity", "Data Privacy"]

    def test_extract_json_from_response_no_brackets(self, topic_classification_service):
        """Test handling response without brackets."""
        response_text = 'Cybersecurity, Data Privacy'
        
        result = topic_classification_service._extract_json_from_response(response_text)
        
        assert result == []

    def test_extract_json_from_response_malformed_json(self, topic_classification_service):
        """Test handling malformed JSON."""
        response_text = '["Cybersecurity", "Data Privacy"'  # Missing closing bracket
        
        result = topic_classification_service._extract_json_from_response(response_text)
        
        assert result == []

    def test_extract_json_from_response_nested_brackets(self, topic_classification_service):
        """Test extracting JSON with nested content - should fail due to extra content."""
        response_text = 'Analysis shows ["Cybersecurity", "AI"] and ["Data"] are relevant.'
        
        result = topic_classification_service._extract_json_from_response(response_text)
        
        # Should return empty list because there's extra content after the JSON
        assert result == []

    def test_extract_json_from_response_clean_json_with_text(self, topic_classification_service):
        """Test extracting clean JSON surrounded by text."""
        response_text = 'Based on the analysis, the topics are: ["Cybersecurity", "AI"]. These are the most relevant.'
        
        result = topic_classification_service._extract_json_from_response(response_text)
        
        assert result == ["Cybersecurity", "AI"]

    @patch('requests.post')
    def test_classify_news_topics_json_decode_error(self, mock_post, topic_classification_service, mock_news):
        """Test handling of JSON decode error from requests."""
        mock_response = Mock()
        mock_response.json.side_effect = json.JSONDecodeError("Invalid JSON", "", 0)
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        result = topic_classification_service.classify_news_topics(mock_news)

        assert result == []

    @patch('requests.post')
    def test_classify_news_topics_unexpected_error(self, mock_post, topic_classification_service, mock_news):
        """Test handling of unexpected errors."""
        mock_post.side_effect = Exception("Unexpected error")

        result = topic_classification_service.classify_news_topics(mock_news)

        assert result == []

    @patch('requests.post')
    def test_classify_news_topics_with_whitespace_in_response(self, mock_post, topic_classification_service, mock_news):
        """Test handling response with extra whitespace."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "response": '  \n  ["Cybersecurity", "Artificial Intelligence"]  \n  '
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        result = topic_classification_service.classify_news_topics(mock_news)

        assert len(result) == 2
        assert result[0].name == "Cybersecurity"
        assert result[1].name == "Artificial Intelligence"

    def test_topics_conversion_to_string(self, mock_topic_service):
        """Test that topic names are properly converted to strings."""
        with patch('digiliencia.data.services.neomodel.topic.topic_classification_service.TopicService') as mock_service_class:
            mock_service_class.return_value = mock_topic_service
            
            service = TopicClassificationService()
            
            # Verify all topics are strings
            assert all(isinstance(topic, str) for topic in service.topics)
