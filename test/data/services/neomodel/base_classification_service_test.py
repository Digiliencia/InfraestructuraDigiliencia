import pytest

from digiliencia.data.models.neomodel.topic import Topic
from digiliencia.data.services.neomodel.base_classification_service import (
    BaseClassificationService,
)


class MockClassificationService(BaseClassificationService[Topic]):
    """Mock implementation for testing the base class."""

    def __init__(
        self, ollama_url: str = "http://localhost:11434/api/generate", mocker=None
    ):
        if mocker is None:
            raise ValueError("mocker is required for MockClassificationService")

        self.mock_objects = [
            mocker.Mock(name="topic1"),
            mocker.Mock(name="topic2"),
            mocker.Mock(name="topic3"),
        ]
        # Set name attribute for each mock
        for i, obj in enumerate(self.mock_objects, 1):
            obj.name = f"topic{i}"
        super().__init__(ollama_url)

    def _initialize_data(self) -> None:
        """Initialize mock data."""
        pass

    def _generate_prompt(self, text: str, max_items: int) -> str:
        """Generate mock prompt."""
        return f"Mock prompt for text: {text[:50]}... with max {max_items} items"

    def _get_name_to_object_mapping(self) -> dict:
        """Get mock name to object mapping."""
        return {obj.name: obj for obj in self.mock_objects}

    def _get_entity_type_name(self) -> str:
        """Get mock entity type name."""
        return "mock_topic"


@pytest.fixture
def service(mocker):
    """Set up test fixtures."""
    return MockClassificationService(mocker=mocker)


@pytest.fixture
def mock_news(mocker):
    """Set up mock news fixture."""
    mock_news = mocker.Mock()
    mock_news.content = "This is a test news content for classification."
    return mock_news


def test_initialization(service):
    """Test service initialization."""
    assert service.ollama_url == "http://localhost:11434/api/generate"
    assert service.mock_objects is not None


def test_create_ollama_payload(service, mocker):
    """Test Ollama payload creation."""
    mock_env = mocker.patch("digiliencia.configs.env.Env")
    mock_env_instance = mocker.Mock()
    mock_env_instance.classification_model = "test_model"
    mock_env.return_value = mock_env_instance

    payload = service._create_ollama_payload("test prompt")

    expected = {
        "model": "test_model",
        "prompt": "test prompt",
        "stream": False,
        "options": {
            "temperature": 0,
        },
    }
    assert payload == expected


def test_send_ollama_request_success(service, mocker):
    """Test successful Ollama request."""
    mock_post = mocker.patch(
        "digiliencia.data.services.neomodel.base_classification_service.requests.post"
    )
    # Mock response
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"response": "test response"}
    mock_response.raise_for_status = mocker.Mock()
    mock_post.return_value = mock_response

    payload = {"test": "payload"}
    result = service._send_ollama_request(payload)

    assert result == "test response"
    mock_post.assert_called_once_with(
        "http://localhost:11434/api/generate", json=payload, timeout=60000
    )


def test_send_ollama_request_no_response_field(service, mocker):
    """Test Ollama request with missing response field."""
    mock_post = mocker.patch(
        "digiliencia.data.services.neomodel.base_classification_service.requests.post"
    )
    # Mock response without 'response' field
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"error": "no response"}
    mock_response.raise_for_status = mocker.Mock()
    mock_post.return_value = mock_response

    payload = {"test": "payload"}

    with pytest.raises(ValueError) as exc_info:
        service._send_ollama_request(payload)

    assert "does not contain 'response' field" in str(exc_info.value)


def test_extract_and_validate_json_success(service, mocker):
    """Test successful JSON extraction and validation."""
    mock_extract = mocker.patch(
        "digiliencia.utils.llm.LLMUtils.extract_json_from_response"
    )
    mock_extract.return_value = ["topic1", "topic2"]

    result = service._extract_and_validate_json("mock response")

    assert result == ["topic1", "topic2"]
    mock_extract.assert_called_once_with("mock response")


def test_extract_and_validate_json_not_list(service, mocker):
    """Test JSON extraction when result is not a list."""
    mock_extract = mocker.patch(
        "digiliencia.utils.llm.LLMUtils.extract_json_from_response"
    )
    mock_extract.return_value = {"not": "a list"}

    with pytest.raises(ValueError) as exc_info:
        service._extract_and_validate_json("mock response")

    assert "Response is not a list" in str(exc_info.value)


def test_map_names_to_objects_success(service):
    """Test successful mapping of names to objects."""
    selected_names = ["topic1", "topic2"]

    result = service._map_names_to_objects(selected_names, 5)

    assert len(result) == 2
    assert result[0].name == "topic1"
    assert result[1].name == "topic2"


def test_map_names_to_objects_with_invalid_names(service, mocker):
    """Test mapping when some names are invalid."""
    selected_names = ["topic1", "invalid_topic", "topic2"]

    mock_logger = mocker.patch(
        "digiliencia.data.services.neomodel.base_classification_service.logger"
    )
    result = service._map_names_to_objects(selected_names, 5)

    assert len(result) == 2  # Only valid topics
    mock_logger.warning.assert_called_once()


def test_map_names_to_objects_max_items_limit(service):
    """Test that max_items limit is respected."""
    selected_names = ["topic1", "topic2", "topic3"]

    result = service._map_names_to_objects(selected_names, 2)

    assert len(result) == 2  # Limited to max_items


def test_classify_news_integration(service, mock_news, mocker):
    """Test full classification flow integration."""
    # Setup mocks
    mock_env = mocker.patch("digiliencia.configs.env.Env")
    mock_extract = mocker.patch(
        "digiliencia.utils.llm.LLMUtils.extract_json_from_response"
    )
    mock_post = mocker.patch(
        "digiliencia.data.services.neomodel.base_classification_service.requests.post"
    )

    mock_env_instance = mocker.Mock()
    mock_env_instance.classification_model = "test_model"
    mock_env.return_value = mock_env_instance

    mock_response = mocker.Mock()
    mock_response.json.return_value = {"response": "mock llm response"}
    mock_response.raise_for_status = mocker.Mock()
    mock_post.return_value = mock_response
    mock_extract.return_value = ["topic1", "topic2"]

    # Execute
    result = service.classify_news(mock_news, 3)

    # Verify
    assert len(result) == 2
    assert result[0].name == "topic1"
    assert result[1].name == "topic2"
