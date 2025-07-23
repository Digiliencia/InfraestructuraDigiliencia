"""Tests for LLMUtils class."""

import pytest

from digiliencia.utils.llm import LLMUtils


class TestLLMUtils:
    """Test class for LLMUtils."""

    def test_extract_json_from_response_valid_json(self):
        """Test extracting valid JSON from response."""
        response_text = (
            'Here are the topics: ["Cybersecurity", "AI"] based on the analysis.'
        )

        result = LLMUtils.extract_json_from_response(response_text)

        assert result == ["Cybersecurity", "AI"]

    def test_extract_json_from_response_only_json(self):
        """Test extracting JSON when response contains only JSON."""
        response_text = '["Cybersecurity", "Data Privacy"]'

        result = LLMUtils.extract_json_from_response(response_text)

        assert result == ["Cybersecurity", "Data Privacy"]

    def test_extract_json_from_response_no_brackets(self):
        """Test handling response without brackets."""
        response_text = "Cybersecurity, Data Privacy"

        result = LLMUtils.extract_json_from_response(response_text)

        assert result == []

    def test_extract_json_from_response_malformed_json(self):
        """Test handling malformed JSON."""
        response_text = '["Cybersecurity", "Data Privacy"'  # Missing closing bracket

        result = LLMUtils.extract_json_from_response(response_text)

        assert result == []

    def test_extract_json_from_response_nested_brackets(self):
        """Test extracting JSON with multiple JSON arrays - should return the last valid one."""
        response_text = 'Analysis shows ["Cybersecurity", "AI"] and ["Data"] are relevant.'

        result = LLMUtils.extract_json_from_response(response_text)

        # Should return the last valid JSON array found
        assert result == ["Data"]

    def test_extract_json_from_response_clean_json_with_text(self):
        """Test extracting clean JSON surrounded by text."""
        response_text = 'Based on the analysis, the topics are: ["Cybersecurity", "AI"]. These are the most relevant.'

        result = LLMUtils.extract_json_from_response(response_text)

        assert result == ["Cybersecurity", "AI"]

    def test_extract_json_from_response_json_is_not_list(self):
        """Test handling when parsed JSON is not a list (covers lines 122-123)."""
        response_text = 'Here is the result: {"key": "value"}'

        result = LLMUtils.extract_json_from_response(response_text)

        assert result == []

    def test_extract_json_from_response_multiple_arrays_with_invalid_json(self):
        """Test handling multiple JSON candidates where some are invalid (covers lines 124-126)."""
        response_text = 'First: [invalid json] Second: ["Valid", "Topics"]'

        result = LLMUtils.extract_json_from_response(response_text)

        assert result == ["Valid", "Topics"]

    def test_extract_json_from_response_all_invalid_json(self):
        """Test when all potential JSONs are invalid (covers lines 127-129)."""
        response_text = "First: [invalid] Second: [also invalid"

        result = LLMUtils.extract_json_from_response(response_text)

        assert result == []

    def test_extract_json_from_response_valid_non_list_json(self):
        """Test when JSON is valid but not a list (covers lines 122-123)."""
        response_text = 'Result: {"topic": "Cybersecurity", "score": 0.9}'

        result = LLMUtils.extract_json_from_response(response_text)

        assert result == []

    def test_extract_json_from_response_multiple_jsons_first_not_list(self):
        """Test with multiple JSONs where first is valid but not a list (covers lines 122-123)."""
        response_text = (
            'First result: {"single": "object"} and then the list: ["Cybersecurity", "AI"]'
        )

        result = LLMUtils.extract_json_from_response(response_text)

        assert result == ["Cybersecurity", "AI"]
