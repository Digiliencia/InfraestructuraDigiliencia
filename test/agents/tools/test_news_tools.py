"""Tests for news_tools module with 100% coverage."""

import pytest
from unittest.mock import Mock, patch
from datetime import datetime

from digiliencia.agents.tools.news_tools import get_news
from digiliencia.enums.topics import Topics
from digiliencia.enums.related_fields import RelatedFields


class TestGetNews:
    """Test class for get_news function with complete coverage."""

    @patch("digiliencia.agents.tools.news_tools.NewsService")
    def test_get_news_with_default_parameters(self, mock_news_service_class):
        """Test get_news with default parameters only."""
        # Arrange
        mock_service = Mock()
        mock_news_service_class.return_value = mock_service
        expected_result = []
        mock_service.get.return_value = expected_result

        # Act
        result = get_news()

        # Assert
        mock_news_service_class.assert_called_once()
        mock_service.get.assert_called_once_with(
            limit=10,
            topic=None,
            related_field=None,
            start_date=None,
            end_date=None,
            organization=None,
        )
        assert result == expected_result

    @patch("digiliencia.agents.tools.news_tools.NewsService")
    def test_get_news_with_custom_limit(self, mock_news_service_class):
        """Test get_news with custom limit parameter."""
        # Arrange
        mock_service = Mock()
        mock_news_service_class.return_value = mock_service
        expected_result = []
        mock_service.get.return_value = expected_result
        custom_limit = 25

        # Act
        result = get_news(limit=custom_limit)

        # Assert
        mock_service.get.assert_called_once_with(
            limit=custom_limit,
            topic=None,
            related_field=None,
            start_date=None,
            end_date=None,
            organization=None,
        )
        assert result == expected_result

    @patch("digiliencia.agents.tools.news_tools.NewsService")
    def test_get_news_with_topic_filter(self, mock_news_service_class):
        """Test get_news with topic parameter."""
        # Arrange
        mock_service = Mock()
        mock_news_service_class.return_value = mock_service
        expected_result = []
        mock_service.get.return_value = expected_result
        topic = Topics.CYBERBULLYING

        # Act
        result = get_news(topic=topic)

        # Assert
        mock_service.get.assert_called_once_with(
            limit=10,
            topic=topic,
            related_field=None,
            start_date=None,
            end_date=None,
            organization=None,
        )
        assert result == expected_result

    @patch("digiliencia.agents.tools.news_tools.NewsService")
    def test_get_news_with_related_field_filter(self, mock_news_service_class):
        """Test get_news with related_field parameter."""
        # Arrange
        mock_service = Mock()
        mock_news_service_class.return_value = mock_service
        expected_result = []
        mock_service.get.return_value = expected_result
        # Using specific enum value
        related_field = RelatedFields.InternetGovernance.ONLINE_SURVEILLANCE

        # Act
        result = get_news(related_field=related_field)  # type: ignore

        # Assert
        mock_service.get.assert_called_once_with(
            limit=10,
            topic=None,
            related_field=related_field,
            start_date=None,
            end_date=None,
            organization=None,
        )
        assert result == expected_result

    @patch("digiliencia.agents.tools.news_tools.NewsService")
    def test_get_news_with_start_date_filter(self, mock_news_service_class):
        """Test get_news with start_date parameter."""
        # Arrange
        mock_service = Mock()
        mock_news_service_class.return_value = mock_service
        expected_result = []
        mock_service.get.return_value = expected_result
        start_date = "2024-01-01"

        # Act
        result = get_news(start_date=start_date)

        # Assert
        mock_service.get.assert_called_once_with(
            limit=10,
            topic=None,
            related_field=None,
            start_date=start_date,
            end_date=None,
            organization=None,
        )
        assert result == expected_result

    @patch("digiliencia.agents.tools.news_tools.NewsService")
    def test_get_news_with_end_date_filter(self, mock_news_service_class):
        """Test get_news with end_date parameter."""
        # Arrange
        mock_service = Mock()
        mock_news_service_class.return_value = mock_service
        expected_result = []
        mock_service.get.return_value = expected_result
        end_date = "2024-12-31"

        # Act
        result = get_news(end_date=end_date)

        # Assert
        mock_service.get.assert_called_once_with(
            limit=10,
            topic=None,
            related_field=None,
            start_date=None,
            end_date=end_date,
            organization=None,
        )
        assert result == expected_result

    @patch("digiliencia.agents.tools.news_tools.NewsService")
    def test_get_news_with_organization_filter(self, mock_news_service_class):
        """Test get_news with organization parameter."""
        # Arrange
        mock_service = Mock()
        mock_news_service_class.return_value = mock_service
        expected_result = []
        mock_service.get.return_value = expected_result
        organization = "Test Organization"

        # Act
        result = get_news(organization=organization)

        # Assert
        mock_service.get.assert_called_once_with(
            limit=10,
            topic=None,
            related_field=None,
            start_date=None,
            end_date=None,
            organization=organization,
        )
        assert result == expected_result

    @patch("digiliencia.agents.tools.news_tools.NewsService")
    def test_get_news_with_date_range_filter(self, mock_news_service_class):
        """Test get_news with both start_date and end_date parameters."""
        # Arrange
        mock_service = Mock()
        mock_news_service_class.return_value = mock_service
        expected_result = []
        mock_service.get.return_value = expected_result
        start_date = "2024-01-01"
        end_date = "2024-12-31"

        # Act
        result = get_news(start_date=start_date, end_date=end_date)

        # Assert
        mock_service.get.assert_called_once_with(
            limit=10,
            topic=None,
            related_field=None,
            start_date=start_date,
            end_date=end_date,
            organization=None,
        )
        assert result == expected_result

    @patch("digiliencia.agents.tools.news_tools.NewsService")
    def test_get_news_with_all_parameters(self, mock_news_service_class):
        """Test get_news with all parameters specified."""
        # Arrange
        mock_service = Mock()
        mock_news_service_class.return_value = mock_service
        expected_result = []
        mock_service.get.return_value = expected_result

        limit = 50
        topic = Topics.MALWARE
        related_field = RelatedFields.BankingAndCapitalMarkets.FINANCIAL_TECHNOLOGY
        start_date = "2024-01-01"
        end_date = "2024-12-31"
        organization = "Cybersecurity News Corp"

        # Act
        result = get_news(
            limit=limit,
            topic=topic,
            related_field=related_field,  # type: ignore
            start_date=start_date,
            end_date=end_date,
            organization=organization,
        )

        # Assert
        mock_service.get.assert_called_once_with(
            limit=limit,
            topic=topic,
            related_field=related_field,
            start_date=start_date,
            end_date=end_date,
            organization=organization,
        )
        assert result == expected_result

    @patch("digiliencia.agents.tools.news_tools.NewsService")
    def test_get_news_returns_service_result(self, mock_news_service_class):
        """Test that get_news returns the exact result from NewsService.get."""
        # Arrange
        mock_service = Mock()
        mock_news_service_class.return_value = mock_service

        # Create mock news objects
        mock_news_1 = Mock()
        mock_news_1.header = "First News"
        mock_news_1.content = "First news content"

        mock_news_2 = Mock()
        mock_news_2.header = "Second News"
        mock_news_2.content = "Second news content"

        expected_result = [mock_news_1, mock_news_2]
        mock_service.get.return_value = expected_result

        # Act
        result = get_news()

        # Assert
        assert result == expected_result
        assert (
            result is expected_result
        )  # Should return the exact same object reference

    @patch("digiliencia.agents.tools.news_tools.NewsService")
    def test_get_news_with_zero_limit(self, mock_news_service_class):
        """Test get_news with zero limit (edge case)."""
        # Arrange
        mock_service = Mock()
        mock_news_service_class.return_value = mock_service
        expected_result = []
        mock_service.get.return_value = expected_result

        # Act
        result = get_news(limit=0)

        # Assert
        mock_service.get.assert_called_once_with(
            limit=0,
            topic=None,
            related_field=None,
            start_date=None,
            end_date=None,
            organization=None,
        )
        assert result == expected_result

    @patch("digiliencia.agents.tools.news_tools.NewsService")
    def test_get_news_with_negative_limit(self, mock_news_service_class):
        """Test get_news with negative limit (edge case)."""
        # Arrange
        mock_service = Mock()
        mock_news_service_class.return_value = mock_service
        expected_result = []
        mock_service.get.return_value = expected_result

        # Act
        result = get_news(limit=-5)

        # Assert
        mock_service.get.assert_called_once_with(
            limit=-5,
            topic=None,
            related_field=None,
            start_date=None,
            end_date=None,
            organization=None,
        )
        assert result == expected_result

    @patch("digiliencia.agents.tools.news_tools.NewsService")
    def test_get_news_creates_new_service_instance_each_call(
        self, mock_news_service_class
    ):
        """Test that get_news creates a new NewsService instance for each call."""
        # Arrange
        mock_service = Mock()
        mock_news_service_class.return_value = mock_service
        mock_service.get.return_value = []

        # Act
        get_news()
        get_news()
        get_news()

        # Assert
        assert mock_news_service_class.call_count == 3
        assert mock_service.get.call_count == 3

    @patch("digiliencia.agents.tools.news_tools.NewsService")
    def test_get_news_with_various_topic_values(self, mock_news_service_class):
        """Test get_news with different topic enum values."""
        # Arrange
        mock_service = Mock()
        mock_news_service_class.return_value = mock_service
        mock_service.get.return_value = []

        topics_to_test = [
            Topics.PHISHING,
            Topics.RANSOMWARE,
            Topics.SOCIAL_ENGINEERING,
            Topics.VULNERABILITY,
            Topics.DEEPFAKE,
        ]

        for topic in topics_to_test:
            mock_news_service_class.reset_mock()
            mock_service.reset_mock()

            # Act
            result = get_news(topic=topic)

            # Assert
            mock_service.get.assert_called_once_with(
                limit=10,
                topic=topic,
                related_field=None,
                start_date=None,
                end_date=None,
                organization=None,
            )
            assert result == []

    @patch("digiliencia.agents.tools.news_tools.NewsService")
    def test_get_news_with_various_related_field_values(self, mock_news_service_class):
        """Test get_news with different related field enum values."""
        # Arrange
        mock_service = Mock()
        mock_news_service_class.return_value = mock_service
        mock_service.get.return_value = []

        related_fields_to_test = [
            RelatedFields.InternetGovernance.DATA_PROTECTION,
            RelatedFields.Corruption.TECH_FOR_INTEGRITY,
            RelatedFields.ArtificialIntelligence.GENERATIVE_AI,
            RelatedFields.DigitalCommunications.SECURE_DATA_TRANSMISSION,
            RelatedFields.IllicitEconomy.CYBERCRIME,
        ]

        for related_field in related_fields_to_test:
            mock_news_service_class.reset_mock()
            mock_service.reset_mock()

            # Act
            result = get_news(related_field=related_field)  # type: ignore

            # Assert
            mock_service.get.assert_called_once_with(
                limit=10,
                topic=None,
                related_field=related_field,
                start_date=None,
                end_date=None,
                organization=None,
            )
            assert result == []

    @patch("digiliencia.agents.tools.news_tools.NewsService")
    def test_get_news_with_complex_combinations(self, mock_news_service_class):
        """Test get_news with complex parameter combinations."""
        # Arrange
        mock_service = Mock()
        mock_news_service_class.return_value = mock_service
        mock_service.get.return_value = []

        test_combinations = [
            {
                "limit": 15,
                "topic": Topics.CYBERBULLYING,
                "organization": "Security News",
            },
            {
                "limit": 100,
                "related_field": RelatedFields.Values.TRUST_AS_A_VALUE,
                "start_date": "2023-06-01",
                "end_date": "2023-06-30",
            },
            {
                "topic": Topics.BOTNET,
                "related_field": RelatedFields.InternetGovernance.PREVENTING_ONLINE_CRIME,
                "start_date": "2024-01-01",
            },
        ]

        for i, params in enumerate(test_combinations):
            mock_news_service_class.reset_mock()
            mock_service.reset_mock()

            # Act
            result = get_news(**params)  # type: ignore

            # Assert
            expected_call_params = {
                "limit": params.get("limit", 10),
                "topic": params.get("topic", None),
                "related_field": params.get("related_field", None),
                "start_date": params.get("start_date", None),
                "end_date": params.get("end_date", None),
                "organization": params.get("organization", None),
            }

            mock_service.get.assert_called_once_with(**expected_call_params)
            assert result == []

    @patch("digiliencia.agents.tools.news_tools.NewsService")
    def test_get_news_with_empty_string_parameters(self, mock_news_service_class):
        """Test get_news with empty string parameters."""
        # Arrange
        mock_service = Mock()
        mock_news_service_class.return_value = mock_service
        mock_service.get.return_value = []

        # Act
        result = get_news(start_date="", end_date="", organization="")

        # Assert
        mock_service.get.assert_called_once_with(
            limit=10,
            topic=None,
            related_field=None,
            start_date="",
            end_date="",
            organization="",
        )
        assert result == []

    @patch("digiliencia.agents.tools.news_tools.NewsService")
    def test_get_news_with_large_limit(self, mock_news_service_class):
        """Test get_news with a very large limit."""
        # Arrange
        mock_service = Mock()
        mock_news_service_class.return_value = mock_service
        mock_service.get.return_value = []
        large_limit = 99999

        # Act
        result = get_news(limit=large_limit)

        # Assert
        mock_service.get.assert_called_once_with(
            limit=large_limit,
            topic=None,
            related_field=None,
            start_date=None,
            end_date=None,
            organization=None,
        )
        assert result == []

    @patch("digiliencia.agents.tools.news_tools.NewsService")
    def test_get_news_service_exception_propagation(self, mock_news_service_class):
        """Test that exceptions from NewsService.get are properly propagated."""
        # Arrange
        mock_service = Mock()
        mock_news_service_class.return_value = mock_service
        mock_service.get.side_effect = Exception("Database connection error")

        # Act & Assert
        with pytest.raises(Exception, match="Database connection error"):
            get_news()

    @patch("digiliencia.agents.tools.news_tools.NewsService")
    def test_get_news_service_instantiation_exception(self, mock_news_service_class):
        """Test that exceptions during NewsService instantiation are properly propagated."""
        # Arrange
        mock_news_service_class.side_effect = Exception("Configuration error")

        # Act & Assert
        with pytest.raises(Exception, match="Configuration error"):
            get_news()

    @patch("digiliencia.agents.tools.news_tools.NewsService")
    def test_get_news_with_none_values_explicitly(self, mock_news_service_class):
        """Test get_news with None values passed explicitly."""
        # Arrange
        mock_service = Mock()
        mock_news_service_class.return_value = mock_service
        mock_service.get.return_value = []

        # Act
        result = get_news(
            limit=20,
            topic=None,
            related_field=None,
            start_date=None,
            end_date=None,
            organization=None,
        )

        # Assert
        mock_service.get.assert_called_once_with(
            limit=20,
            topic=None,
            related_field=None,
            start_date=None,
            end_date=None,
            organization=None,
        )
        assert result == []

    @patch("digiliencia.agents.tools.news_tools.NewsService")
    def test_get_news_with_realistic_news_data(self, mock_news_service_class):
        """Test get_news with realistic mock news data returned."""
        # Arrange
        mock_service = Mock()
        mock_news_service_class.return_value = mock_service

        # Create realistic mock news objects
        mock_news_1 = Mock()
        mock_news_1.header = "New Ransomware Variant Targets Healthcare Systems"
        mock_news_1.content = (
            "A sophisticated ransomware variant has been discovered..."
        )
        mock_news_1.date = datetime(2024, 9, 15, 10, 30)
        mock_news_1.url = "https://cybersecuritynews.com/ransomware-healthcare"
        mock_news_1.source_name = "CyberSecurity News"

        mock_news_2 = Mock()
        mock_news_2.header = "AI-Powered Phishing Attacks on the Rise"
        mock_news_2.content = "Security researchers report a 300% increase in AI-generated phishing emails..."
        mock_news_2.date = datetime(2024, 9, 14, 15, 45)
        mock_news_2.url = "https://securityreport.com/ai-phishing"
        mock_news_2.source_name = "Security Report"

        expected_result = [mock_news_1, mock_news_2]
        mock_service.get.return_value = expected_result

        # Act
        result = get_news(
            limit=5,
            topic=Topics.RANSOMWARE,
            related_field=RelatedFields.HealthAndLifeSciences.HOSPITAL_INFRASTRUCTURE,  # type: ignore
        )

        # Assert
        mock_service.get.assert_called_once_with(
            limit=5,
            topic=Topics.RANSOMWARE,
            related_field=RelatedFields.HealthAndLifeSciences.HOSPITAL_INFRASTRUCTURE,
            start_date=None,
            end_date=None,
            organization=None,
        )
        assert result == expected_result
        assert len(result) == 2
        assert result[0].header == "New Ransomware Variant Targets Healthcare Systems"
        assert result[1].header == "AI-Powered Phishing Attacks on the Rise"
