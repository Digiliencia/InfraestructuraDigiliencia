"""Tests for NewsService.get method with 100% coverage."""

from unittest.mock import Mock, patch
from datetime import datetime

from digiliencia.data.services.neomodel.news_service import NewsService
from digiliencia.enums.topics import Topics
from digiliencia.enums.related_fields import RelatedFields


class TestNewsServiceGet:
    """Test class for NewsService.get method with complete coverage."""

    @patch("digiliencia.data.services.neomodel.news_service.configure_neomodel")
    @patch("digiliencia.data.services.neomodel.news_service.News")
    def test_news_service_get_default_parameters(self, mock_news_model, mock_configure):
        """Test NewsService.get with default parameters."""
        # Arrange
        mock_queryset = Mock()
        mock_news_model.nodes = mock_queryset
        mock_queryset.filter.return_value = mock_queryset

        # Mock news objects
        mock_news_1 = Mock()
        mock_news_1.topics = []
        mock_news_1.fields = []
        mock_news_2 = Mock()
        mock_news_2.topics = []
        mock_news_2.fields = []

        mock_queryset.__iter__ = Mock(return_value=iter([mock_news_1, mock_news_2]))

        service = NewsService()

        # Act
        result = service.get()

        # Assert
        mock_queryset.filter.assert_called_once_with()
        assert len(result) == 2
        assert result[0] == mock_news_1
        assert result[1] == mock_news_2

    @patch("digiliencia.data.services.neomodel.news_service.configure_neomodel")
    @patch("digiliencia.data.services.neomodel.news_service.News")
    def test_news_service_get_with_limit(self, mock_news_model, mock_configure):
        """Test NewsService.get respects limit parameter."""
        # Arrange
        mock_queryset = Mock()
        mock_news_model.nodes = mock_queryset
        mock_queryset.filter.return_value = mock_queryset

        # Create 5 mock news objects
        mock_news_list = []
        for i in range(5):
            mock_news = Mock()
            mock_news.topics = []
            mock_news.fields = []
            mock_news_list.append(mock_news)

        mock_queryset.__iter__ = Mock(return_value=iter(mock_news_list))

        service = NewsService()

        # Act - limit to 3
        result = service.get(limit=3)

        # Assert
        assert len(result) == 3

    @patch("digiliencia.data.services.neomodel.news_service.configure_neomodel")
    @patch("digiliencia.data.services.neomodel.news_service.News")
    def test_news_service_get_with_organization_filter(
        self, mock_news_model, mock_configure
    ):
        """Test NewsService.get with organization filter."""
        # Arrange
        mock_queryset = Mock()
        mock_news_model.nodes = mock_queryset
        mock_queryset.filter.return_value = mock_queryset
        mock_queryset.__iter__ = Mock(return_value=iter([]))

        service = NewsService()
        organization = "Test Organization"

        # Act
        result = service.get(organization=organization)

        # Assert
        mock_queryset.filter.assert_called_once_with(source_name=organization)
        assert result == []

    @patch("digiliencia.data.services.neomodel.news_service.configure_neomodel")
    @patch("digiliencia.data.services.neomodel.news_service.News")
    def test_news_service_get_with_start_date_filter(
        self, mock_news_model, mock_configure
    ):
        """Test NewsService.get with start_date filter."""
        # Arrange
        mock_queryset = Mock()
        mock_news_model.nodes = mock_queryset
        mock_queryset.filter.return_value = mock_queryset
        mock_queryset.__iter__ = Mock(return_value=iter([]))

        service = NewsService()
        start_date = "2024-01-01"

        # Act
        result = service.get(start_date=start_date)

        # Assert
        expected_date = datetime.strptime(start_date, "%Y-%m-%d")
        mock_queryset.filter.assert_called_once_with(date__gte=expected_date)
        assert result == []

    @patch("digiliencia.data.services.neomodel.news_service.configure_neomodel")
    @patch("digiliencia.data.services.neomodel.news_service.News")
    def test_news_service_get_with_end_date_filter(
        self, mock_news_model, mock_configure
    ):
        """Test NewsService.get with end_date filter."""
        # Arrange
        mock_queryset = Mock()
        mock_news_model.nodes = mock_queryset
        mock_queryset.filter.return_value = mock_queryset
        mock_queryset.__iter__ = Mock(return_value=iter([]))

        service = NewsService()
        end_date = "2024-12-31"

        # Act
        result = service.get(end_date=end_date)

        # Assert
        expected_date = datetime.strptime(end_date, "%Y-%m-%d")
        mock_queryset.filter.assert_called_once_with(date__lte=expected_date)
        assert result == []

    @patch("digiliencia.data.services.neomodel.news_service.configure_neomodel")
    @patch("digiliencia.data.services.neomodel.news_service.News")
    def test_news_service_get_with_date_range_filter(
        self, mock_news_model, mock_configure
    ):
        """Test NewsService.get with both start_date and end_date filters."""
        # Arrange
        mock_queryset = Mock()
        mock_news_model.nodes = mock_queryset
        mock_queryset.filter.return_value = mock_queryset
        mock_queryset.__iter__ = Mock(return_value=iter([]))

        service = NewsService()
        start_date = "2024-01-01"
        end_date = "2024-12-31"

        # Act
        result = service.get(start_date=start_date, end_date=end_date)

        # Assert
        expected_start = datetime.strptime(start_date, "%Y-%m-%d")
        expected_end = datetime.strptime(end_date, "%Y-%m-%d")
        mock_queryset.filter.assert_called_once_with(
            date__gte=expected_start, date__lte=expected_end
        )
        assert result == []

    @patch("digiliencia.data.services.neomodel.news_service.configure_neomodel")
    @patch("digiliencia.data.services.neomodel.news_service.News")
    def test_news_service_get_with_all_filters(self, mock_news_model, mock_configure):
        """Test NewsService.get with all filter parameters."""
        # Arrange
        mock_queryset = Mock()
        mock_news_model.nodes = mock_queryset
        mock_queryset.filter.return_value = mock_queryset
        mock_queryset.__iter__ = Mock(return_value=iter([]))

        service = NewsService()
        organization = "Security News"
        start_date = "2024-01-01"
        end_date = "2024-12-31"

        # Act
        result = service.get(
            organization=organization, start_date=start_date, end_date=end_date
        )

        # Assert
        expected_start = datetime.strptime(start_date, "%Y-%m-%d")
        expected_end = datetime.strptime(end_date, "%Y-%m-%d")
        mock_queryset.filter.assert_called_once_with(
            source_name=organization, date__gte=expected_start, date__lte=expected_end
        )
        assert result == []

    @patch("digiliencia.data.services.neomodel.news_service.configure_neomodel")
    @patch("digiliencia.data.services.neomodel.news_service.News")
    def test_news_service_get_with_topic_filter(self, mock_news_model, mock_configure):
        """Test NewsService.get with topic filter."""
        # Arrange
        mock_queryset = Mock()
        mock_news_model.nodes = mock_queryset
        mock_queryset.filter.return_value = mock_queryset

        # Create mock news with matching topic
        mock_news_1 = Mock()
        mock_topic_1 = Mock()
        mock_topic_1.name = "Malware"
        mock_news_1.topics = [mock_topic_1]
        mock_news_1.fields = []

        # Create mock news without matching topic
        mock_news_2 = Mock()
        mock_topic_2 = Mock()
        mock_topic_2.name = "Phishing"
        mock_news_2.topics = [mock_topic_2]
        mock_news_2.fields = []

        mock_queryset.__iter__ = Mock(return_value=iter([mock_news_1, mock_news_2]))

        service = NewsService()
        topic = Topics.MALWARE

        # Act
        result = service.get(topic=topic)

        # Assert
        mock_queryset.filter.assert_called_once_with()
        assert len(result) == 1
        assert result[0] == mock_news_1

    @patch("digiliencia.data.services.neomodel.news_service.configure_neomodel")
    @patch("digiliencia.data.services.neomodel.news_service.News")
    def test_news_service_get_with_related_field_filter(
        self, mock_news_model, mock_configure
    ):
        """Test NewsService.get with related_field filter."""
        # Arrange
        mock_queryset = Mock()
        mock_news_model.nodes = mock_queryset
        mock_queryset.filter.return_value = mock_queryset

        # Create mock news with matching field
        mock_news_1 = Mock()
        mock_field_1 = Mock()
        mock_field_1.name = "Cybercrime"
        mock_news_1.topics = []
        mock_news_1.fields = [mock_field_1]

        # Create mock news without matching field
        mock_news_2 = Mock()
        mock_field_2 = Mock()
        mock_field_2.name = "Other Field"
        mock_news_2.topics = []
        mock_news_2.fields = [mock_field_2]

        mock_queryset.__iter__ = Mock(return_value=iter([mock_news_1, mock_news_2]))

        service = NewsService()
        related_field = RelatedFields.IllicitEconomy.CYBERCRIME

        # Act
        result = service.get(related_field=related_field)  # type: ignore

        # Assert
        mock_queryset.filter.assert_called_once_with()
        assert len(result) == 1
        assert result[0] == mock_news_1

    @patch("digiliencia.data.services.neomodel.news_service.configure_neomodel")
    @patch("digiliencia.data.services.neomodel.news_service.News")
    def test_news_service_get_with_topic_and_field_filters(
        self, mock_news_model, mock_configure
    ):
        """Test NewsService.get with both topic and related_field filters."""
        # Arrange
        mock_queryset = Mock()
        mock_news_model.nodes = mock_queryset
        mock_queryset.filter.return_value = mock_queryset

        # Create mock news matching both topic and field
        mock_news_1 = Mock()
        mock_topic_1 = Mock()
        mock_topic_1.name = "Malware"
        mock_field_1 = Mock()
        mock_field_1.name = "Cybercrime"
        mock_news_1.topics = [mock_topic_1]
        mock_news_1.fields = [mock_field_1]

        # Create mock news matching only topic
        mock_news_2 = Mock()
        mock_topic_2 = Mock()
        mock_topic_2.name = "Malware"
        mock_field_2 = Mock()
        mock_field_2.name = "Other Field"
        mock_news_2.topics = [mock_topic_2]
        mock_news_2.fields = [mock_field_2]

        mock_queryset.__iter__ = Mock(return_value=iter([mock_news_1, mock_news_2]))

        service = NewsService()
        topic = Topics.MALWARE
        related_field = RelatedFields.IllicitEconomy.CYBERCRIME

        # Act
        result = service.get(topic=topic, related_field=related_field)  # type: ignore

        # Assert
        mock_queryset.filter.assert_called_once_with()
        assert len(result) == 1
        assert result[0] == mock_news_1

    @patch("digiliencia.data.services.neomodel.news_service.configure_neomodel")
    @patch("digiliencia.data.services.neomodel.news_service.News")
    def test_news_service_get_invalid_date_format(
        self, mock_news_model, mock_configure
    ):
        """Test NewsService.get with invalid date format (should not filter)."""
        # Arrange
        mock_queryset = Mock()
        mock_news_model.nodes = mock_queryset
        mock_queryset.filter.return_value = mock_queryset
        mock_queryset.__iter__ = Mock(return_value=iter([]))

        service = NewsService()
        invalid_date = "invalid-date-format"

        # Act
        result = service.get(start_date=invalid_date)

        # Assert
        # Should call filter with empty params due to date parsing failure
        mock_queryset.filter.assert_called_once_with()
        assert result == []

    @patch("digiliencia.data.services.neomodel.news_service.configure_neomodel")
    @patch("digiliencia.data.services.neomodel.news_service.News")
    def test_news_service_get_no_matching_topic(self, mock_news_model, mock_configure):
        """Test NewsService.get when no news match the topic filter."""
        # Arrange
        mock_queryset = Mock()
        mock_news_model.nodes = mock_queryset
        mock_queryset.filter.return_value = mock_queryset

        # Create mock news with different topic
        mock_news_1 = Mock()
        mock_topic_1 = Mock()
        mock_topic_1.name = "Phishing"
        mock_news_1.topics = [mock_topic_1]
        mock_news_1.fields = []

        mock_queryset.__iter__ = Mock(return_value=iter([mock_news_1]))

        service = NewsService()
        topic = Topics.MALWARE  # Different topic

        # Act
        result = service.get(topic=topic)

        # Assert
        assert len(result) == 0

    @patch("digiliencia.data.services.neomodel.news_service.configure_neomodel")
    @patch("digiliencia.data.services.neomodel.news_service.News")
    def test_news_service_get_no_matching_field(self, mock_news_model, mock_configure):
        """Test NewsService.get when no news match the related_field filter."""
        # Arrange
        mock_queryset = Mock()
        mock_news_model.nodes = mock_queryset
        mock_queryset.filter.return_value = mock_queryset

        # Create mock news with different field
        mock_news_1 = Mock()
        mock_field_1 = Mock()
        mock_field_1.name = "Other Field"
        mock_news_1.topics = []
        mock_news_1.fields = [mock_field_1]

        mock_queryset.__iter__ = Mock(return_value=iter([mock_news_1]))

        service = NewsService()
        related_field = RelatedFields.IllicitEconomy.CYBERCRIME

        # Act
        result = service.get(related_field=related_field)  # type: ignore

        # Assert
        assert len(result) == 0

    @patch("digiliencia.data.services.neomodel.news_service.configure_neomodel")
    @patch("digiliencia.data.services.neomodel.news_service.News")
    def test_news_service_get_news_without_topics_or_fields(
        self, mock_news_model, mock_configure
    ):
        """Test NewsService.get with news that have no topics or fields."""
        # Arrange
        mock_queryset = Mock()
        mock_news_model.nodes = mock_queryset
        mock_queryset.filter.return_value = mock_queryset

        # Create mock news without topics or fields
        mock_news_1 = Mock()
        mock_news_1.topics = []
        mock_news_1.fields = []

        mock_queryset.__iter__ = Mock(return_value=iter([mock_news_1]))

        service = NewsService()
        topic = Topics.MALWARE

        # Act
        result = service.get(topic=topic)

        # Assert
        assert len(result) == 0  # Should not match since no topics

    @patch("digiliencia.data.services.neomodel.news_service.configure_neomodel")
    @patch("digiliencia.data.services.neomodel.news_service.News")
    def test_news_service_get_multiple_topics_one_matches(
        self, mock_news_model, mock_configure
    ):
        """Test NewsService.get when news has multiple topics and one matches."""
        # Arrange
        mock_queryset = Mock()
        mock_news_model.nodes = mock_queryset
        mock_queryset.filter.return_value = mock_queryset

        # Create mock news with multiple topics
        mock_news_1 = Mock()
        mock_topic_1 = Mock()
        mock_topic_1.name = "Phishing"
        mock_topic_2 = Mock()
        mock_topic_2.name = "Malware"  # This one matches
        mock_news_1.topics = [mock_topic_1, mock_topic_2]
        mock_news_1.fields = []

        mock_queryset.__iter__ = Mock(return_value=iter([mock_news_1]))

        service = NewsService()
        topic = Topics.MALWARE

        # Act
        result = service.get(topic=topic)

        # Assert
        assert len(result) == 1
        assert result[0] == mock_news_1

    @patch("digiliencia.data.services.neomodel.news_service.configure_neomodel")
    @patch("digiliencia.data.services.neomodel.news_service.News")
    def test_news_service_get_multiple_fields_one_matches(
        self, mock_news_model, mock_configure
    ):
        """Test NewsService.get when news has multiple fields and one matches."""
        # Arrange
        mock_queryset = Mock()
        mock_news_model.nodes = mock_queryset
        mock_queryset.filter.return_value = mock_queryset

        # Create mock news with multiple fields
        mock_news_1 = Mock()
        mock_field_1 = Mock()
        mock_field_1.name = "Other Field"
        mock_field_2 = Mock()
        mock_field_2.name = "Cybercrime"  # This one matches
        mock_news_1.topics = []
        mock_news_1.fields = [mock_field_1, mock_field_2]

        mock_queryset.__iter__ = Mock(return_value=iter([mock_news_1]))

        service = NewsService()
        related_field = RelatedFields.IllicitEconomy.CYBERCRIME

        # Act
        result = service.get(related_field=related_field)  # type: ignore

        # Assert
        assert len(result) == 1
        assert result[0] == mock_news_1

    @patch("digiliencia.data.services.neomodel.news_service.configure_neomodel")
    @patch("digiliencia.data.services.neomodel.news_service.News")
    def test_news_service_get_edge_case_zero_limit(
        self, mock_news_model, mock_configure
    ):
        """Test NewsService.get with zero limit."""
        # Arrange
        mock_queryset = Mock()
        mock_news_model.nodes = mock_queryset
        mock_queryset.filter.return_value = mock_queryset

        # Create mock news
        mock_news_1 = Mock()
        mock_news_1.topics = []
        mock_news_1.fields = []

        mock_queryset.__iter__ = Mock(return_value=iter([mock_news_1]))

        service = NewsService()

        # Act
        result = service.get(limit=0)

        # Assert
        assert len(result) == 0

    @patch("digiliencia.data.services.neomodel.news_service.configure_neomodel")
    @patch("digiliencia.data.services.neomodel.news_service.News")
    def test_news_service_get_topic_without_name_attribute(
        self, mock_news_model, mock_configure
    ):
        """Test NewsService.get when topic object doesn't have name attribute."""
        # Arrange
        mock_queryset = Mock()
        mock_news_model.nodes = mock_queryset
        mock_queryset.filter.return_value = mock_queryset

        # Create mock news with topic without name attribute
        mock_news_1 = Mock()
        mock_topic_1 = Mock(spec=[])  # Mock without name attribute
        mock_news_1.topics = [mock_topic_1]
        mock_news_1.fields = []

        mock_queryset.__iter__ = Mock(return_value=iter([mock_news_1]))

        service = NewsService()
        topic = Topics.MALWARE

        # Act
        result = service.get(topic=topic)

        # Assert
        assert len(result) == 0  # Should not match due to getattr returning None

    @patch("digiliencia.data.services.neomodel.news_service.configure_neomodel")
    @patch("digiliencia.data.services.neomodel.news_service.News")
    def test_news_service_get_field_without_name_attribute(
        self, mock_news_model, mock_configure
    ):
        """Test NewsService.get when field object doesn't have name attribute."""
        # Arrange
        mock_queryset = Mock()
        mock_news_model.nodes = mock_queryset
        mock_queryset.filter.return_value = mock_queryset

        # Create mock news with field without name attribute
        mock_news_1 = Mock()
        mock_field_1 = Mock(spec=[])  # Mock without name attribute
        mock_news_1.topics = []
        mock_news_1.fields = [mock_field_1]

        mock_queryset.__iter__ = Mock(return_value=iter([mock_news_1]))

        service = NewsService()
        related_field = RelatedFields.IllicitEconomy.CYBERCRIME

        # Act
        result = service.get(related_field=related_field)  # type: ignore

        # Assert
        assert len(result) == 0  # Should not match due to getattr returning None
