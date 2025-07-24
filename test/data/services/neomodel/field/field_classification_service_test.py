import pytest

from digiliencia.data.models.neomodel.field import Field
from digiliencia.data.services.neomodel.field.field_classification_service import (
    FieldClassificationService,
)


@pytest.fixture
def mock_fields(mocker):
    """Create mock field objects for testing."""
    field1 = mocker.Mock(spec=Field)
    field1.name = "cybersecurity"

    field2 = mocker.Mock(spec=Field)
    field2.name = "artificial_intelligence"

    field3 = mocker.Mock(spec=Field)
    field3.name = "data_privacy"

    return [field1, field2, field3]


@pytest.fixture
def mock_fields_hierarchy():
    """Create mock fields hierarchy for testing."""
    return """
    Technology:
    - Cybersecurity
      - Network Security
      - Data Protection
    - Artificial Intelligence
      - Machine Learning
      - Natural Language Processing
    - Data Privacy
      - GDPR Compliance
      - Privacy Policies
    """


@pytest.fixture
def service(mocker, mock_fields, mock_fields_hierarchy):
    """Set up FieldClassificationService with mocked dependencies."""
    # Mock the FieldService
    mock_field_service = mocker.Mock()
    mock_field_service.get_all.return_value = mock_fields
    mock_field_service.get_fields_hierarchy.return_value = mock_fields_hierarchy

    # Mock the FieldClassificationPrompt
    mocker.patch(
        "digiliencia.data.services.neomodel.field.field_classification_service.FieldClassificationPrompt"
    )

    # Create service instance
    service = FieldClassificationService()

    # Replace the field_service with our mock
    service.field_service = mock_field_service
    service.fields = mock_fields
    service.fields_hierarchy = mock_fields_hierarchy

    return service


@pytest.fixture
def mock_news(mocker):
    """Create mock news object for testing."""
    mock_news = mocker.Mock()
    mock_news.content = "This article discusses cybersecurity threats and data privacy concerns in AI systems."
    return mock_news


def test_service_initialization(mocker):
    """Test service initialization and data loading."""
    # Mock dependencies
    mock_field_service = mocker.Mock()
    mock_fields = [mocker.Mock(name="field1"), mocker.Mock(name="field2")]
    mock_hierarchy = "mock hierarchy"

    mock_field_service.get_all.return_value = mock_fields
    mock_field_service.get_fields_hierarchy.return_value = mock_hierarchy

    # Mock the FieldService constructor
    mocker.patch(
        "digiliencia.data.services.neomodel.field.field_classification_service.FieldService",
        return_value=mock_field_service,
    )

    # Create service
    service = FieldClassificationService()

    # Verify initialization
    assert service.field_service == mock_field_service
    assert service.fields == mock_fields
    assert service.fields_hierarchy == mock_hierarchy
    mock_field_service.get_all.assert_called_once()
    mock_field_service.get_fields_hierarchy.assert_called_once()


def test_generate_prompt(service, mocker):
    """Test prompt generation for field classification."""
    # Mock the FieldClassificationPrompt
    mock_prompt_class = mocker.patch(
        "digiliencia.data.services.neomodel.field.field_classification_service.FieldClassificationPrompt"
    )
    mock_prompt_class.generate_news_classification_prompt.return_value = (
        "Generated prompt"
    )

    text = "Test news content"
    max_items = 5

    result = service._generate_prompt(text, max_items)

    assert result == "Generated prompt"
    mock_prompt_class.generate_news_classification_prompt.assert_called_once_with(
        fields=service.fields_hierarchy, text=text, max_fields=max_items
    )


def test_get_name_to_object_mapping(service, mock_fields):
    """Test mapping from field names to Field objects."""
    result = service._get_name_to_object_mapping()

    expected = {
        "cybersecurity": mock_fields[0],
        "artificial_intelligence": mock_fields[1],
        "data_privacy": mock_fields[2],
    }

    assert result == expected
    assert len(result) == 3


def test_get_entity_type_name(service):
    """Test entity type name for logging."""
    result = service._get_entity_type_name()
    assert result == "field"


def test_classify_news_fields_delegates_to_base_method(service, mock_news, mocker):
    """Test that classify_news_fields properly delegates to the base classify_news method."""
    # Mock the base classify_news method
    expected_fields = [mocker.Mock(name="field1"), mocker.Mock(name="field2")]
    mock_classify_news = mocker.patch.object(service, "classify_news")
    mock_classify_news.return_value = expected_fields

    max_fields = 8
    result = service.classify_news_fields(mock_news, max_fields)

    assert result == expected_fields
    mock_classify_news.assert_called_once_with(mock_news, max_fields)


def test_classify_news_fields_default_max_fields(service, mock_news, mocker):
    """Test classify_news_fields with default max_fields parameter."""
    expected_fields = [mocker.Mock(name="field1")]
    mock_classify_news = mocker.patch.object(service, "classify_news")
    mock_classify_news.return_value = expected_fields

    result = service.classify_news_fields(mock_news)

    assert result == expected_fields
    mock_classify_news.assert_called_once_with(mock_news, 10)  # default value


def test_field_classification_integration(mocker, mock_fields, mock_fields_hierarchy):
    """Test full field classification flow integration."""
    # Setup mocks for all dependencies
    mock_field_service = mocker.Mock()
    mock_field_service.get_all.return_value = mock_fields
    mock_field_service.get_fields_hierarchy.return_value = mock_fields_hierarchy

    mocker.patch(
        "digiliencia.data.services.neomodel.field.field_classification_service.FieldService",
        return_value=mock_field_service,
    )

    mock_prompt_class = mocker.patch(
        "digiliencia.data.services.neomodel.field.field_classification_service.FieldClassificationPrompt"
    )
    mock_prompt_class.generate_news_classification_prompt.return_value = (
        "Classification prompt"
    )

    # Mock base class methods
    mock_env = mocker.patch("digiliencia.configs.env.Env")
    mock_env_instance = mocker.Mock()
    mock_env_instance.classification_model = "test_model"
    mock_env.return_value = mock_env_instance

    mock_post = mocker.patch(
        "digiliencia.data.services.neomodel.base_classification_service.requests.post"
    )
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"response": "mock llm response"}
    mock_response.raise_for_status = mocker.Mock()
    mock_post.return_value = mock_response

    mock_extract = mocker.patch(
        "digiliencia.utils.llm.LLMUtils.extract_json_from_response"
    )
    mock_extract.return_value = ["cybersecurity", "data_privacy"]

    # Create service and mock news
    service = FieldClassificationService()
    mock_news = mocker.Mock()
    mock_news.content = "Test content about cybersecurity and privacy"

    # Execute classification
    result = service.classify_news_fields(mock_news, 5)

    # Verify results
    assert len(result) == 2
    assert result[0].name == "cybersecurity"
    assert result[1].name == "data_privacy"

    # Verify method calls
    mock_field_service.get_all.assert_called_once()
    mock_field_service.get_fields_hierarchy.assert_called_once()
    mock_prompt_class.generate_news_classification_prompt.assert_called_once()


def test_empty_fields_list(mocker):
    """Test behavior when no fields are available."""
    # Mock empty fields
    mock_field_service = mocker.Mock()
    mock_field_service.get_all.return_value = []
    mock_field_service.get_fields_hierarchy.return_value = ""

    mocker.patch(
        "digiliencia.data.services.neomodel.field.field_classification_service.FieldService",
        return_value=mock_field_service,
    )

    service = FieldClassificationService()

    assert service.fields == []
    assert service.fields_hierarchy == ""

    # Test mapping with empty fields
    mapping = service._get_name_to_object_mapping()
    assert mapping == {}


def test_fields_with_special_characters_in_names(mocker):
    """Test handling of fields with special characters in names."""
    # Create fields with special characters
    field1 = mocker.Mock(spec=Field)
    field1.name = "AI/ML Technologies"

    field2 = mocker.Mock(spec=Field)
    field2.name = "Privacy & Security"

    special_fields = [field1, field2]

    mock_field_service = mocker.Mock()
    mock_field_service.get_all.return_value = special_fields
    mock_field_service.get_fields_hierarchy.return_value = "hierarchy"

    mocker.patch(
        "digiliencia.data.services.neomodel.field.field_classification_service.FieldService",
        return_value=mock_field_service,
    )

    service = FieldClassificationService()
    mapping = service._get_name_to_object_mapping()

    assert "AI/ML Technologies" in mapping
    assert "Privacy & Security" in mapping
    assert mapping["AI/ML Technologies"] == field1
    assert mapping["Privacy & Security"] == field2
