# -*- coding: utf-8 -*-
from datetime import datetime

import pytest

from digiliencia.utils.time import TimeUtils


@pytest.fixture
def mock_platform(mocker):
    """Mock the platform.system function."""

    def _mock_platform(system_name):
        return mocker.patch("platform.system", return_value=system_name)

    return _mock_platform


@pytest.fixture
def mock_datetime(mocker):
    """Mock the datetime module and provide a fixed now() function."""

    def _mock_datetime():
        mock_dt = mocker.patch("digiliencia.utils.time.datetime")
        mock_now = mocker.MagicMock()
        mock_dt.now.return_value = mock_now

        # Create a mock result for subtraction
        mock_result = mocker.MagicMock()
        mock_now.__sub__.return_value = mock_result

        # Create mock timedelta
        mock_timedelta = mocker.MagicMock()
        mock_dt.timedelta.return_value = mock_timedelta

        return mock_dt, mock_now, mock_result, mock_timedelta

    return _mock_datetime


class TestTimeUtils:
    """Test class for TimeUtils utility functions."""

    def test_format_days_ago_negative_value(self):
        """Test that format_days_ago raises ValueError for negative input."""
        with pytest.raises(ValueError, match="days_ago must be positive"):
            TimeUtils.format_days_ago(-1)

    def test_format_days_ago_zero_value(self):
        """Test that format_days_ago raises ValueError for zero input."""
        with pytest.raises(ValueError, match="days_ago must be positive"):
            TimeUtils.format_days_ago(0)

    def test_format_days_ago_one_day(self):
        """Test format_days_ago returns '1 day ago' for input 1."""
        result = TimeUtils.format_days_ago(1)
        assert result == "1 day ago"

    def test_format_days_ago_multiple_days_less_than_seven(self):
        """Test format_days_ago returns 'X days ago' for input less than 7."""
        for days in range(2, 7):
            result = TimeUtils.format_days_ago(days)
            assert result == f"{days} days ago"

    def test_format_days_ago_seven_or_more_days_windows(
        self, mock_platform, mock_datetime
    ):
        """Test format_days_ago returns formatted date for 7+ days on Windows."""
        mock_platform("Windows")
        mock_dt, mock_now, mock_result, _ = mock_datetime()

        # Mock strftime to return expected format
        mock_result.strftime.return_value = "Jun 1, 2025"

        result = TimeUtils.format_days_ago(10)

        # Verify the correct format was used
        mock_result.strftime.assert_called_once_with("%b %#d, %Y")
        assert result == "Jun 1, 2025"

    def test_format_days_ago_seven_or_more_days_unix(
        self, mock_platform, mock_datetime
    ):
        """Test format_days_ago returns formatted date for 7+ days on Unix/Linux."""
        mock_platform("Linux")
        mock_dt, mock_now, mock_result, _ = mock_datetime()

        # Mock strftime to return expected format
        mock_result.strftime.return_value = "Jun 1, 2025"

        result = TimeUtils.format_days_ago(10)

        # Verify the correct format was used
        mock_result.strftime.assert_called_once_with("%b %-d, %Y")
        assert result == "Jun 1, 2025"

    def test_days_between_dates_relative_dates(self, mocker):
        """Test days_between_dates with relative date strings."""
        mock_datetime = mocker.patch("digiliencia.utils.time.datetime")
        # Mock datetime.now() to return a fixed date
        fixed_date = datetime(2025, 6, 11, 12, 0, 0)
        mock_datetime.now.return_value = fixed_date

        # Test case: from "3 days ago" to "1 day ago" should be 2 days
        result = TimeUtils.days_between_dates("3 days ago", "1 day ago")
        assert result == 2

    def test_days_between_dates_now(self, mocker):
        """Test days_between_dates with 'now' as one of the dates."""
        mock_datetime = mocker.patch("digiliencia.utils.time.datetime")
        fixed_date = datetime(2025, 6, 11, 12, 0, 0)
        mock_datetime.now.return_value = fixed_date

        result = TimeUtils.days_between_dates("now", "1 day ago")
        assert result == -1

    def test_days_between_dates_formatted_dates_windows(self, mock_platform):
        """Test days_between_dates with formatted date strings on Windows."""
        mock_platform("Windows")
        result = TimeUtils.days_between_dates("Jun 1, 2025", "Jun 10, 2025")
        assert result == 9

    def test_days_between_dates_formatted_dates_unix(self, mock_platform):
        """Test days_between_dates with formatted date strings on Unix."""
        mock_platform("Linux")
        result = TimeUtils.days_between_dates("Jun 1, 2025", "Jun 10, 2025")
        assert result == 9

    def test_days_between_dates_invalid_relative_format(self):
        """Test days_between_dates raises ValueError for invalid relative format."""
        with pytest.raises(ValueError, match="Invalid relative date format"):
            TimeUtils.days_between_dates("invalid days ago", "1 day ago")

    def test_days_between_dates_invalid_absolute_format(self):
        """Test days_between_dates raises ValueError for invalid absolute format."""
        with pytest.raises(ValueError, match="Invalid absolute date format"):
            TimeUtils.days_between_dates("invalid date", "Jun 10, 2025")

    def test_days_between_dates_error_parsing_first_date(self):
        """Test days_between_dates handles parsing errors gracefully."""
        with pytest.raises(ValueError, match="Error parsing dates"):
            TimeUtils.days_between_dates("completely invalid", "Jun 10, 2025")

    def test_format_spanish_date(self, mock_datetime):
        """Test format_spanish_date returns date in dd/mm/yyyy format."""
        mock_dt, mock_now, mock_result, _ = mock_datetime()

        # Mock strftime to return expected format
        mock_result.strftime.return_value = "06/06/2025"

        result = TimeUtils.format_spanish_date(5)

        # Verify the correct format was used
        mock_result.strftime.assert_called_once_with("%d/%m/%Y")
        assert result == "06/06/2025"

    def test_days_between_es_dates_valid_format(self):
        """Test days_between_es_dates with valid dd/mm/yyyy format."""
        result = TimeUtils.days_between_es_dates("01/06/2025", "10/06/2025")
        assert result == 9

    def test_days_between_es_dates_alternative_formats(self):
        """Test days_between_es_dates with alternative date formats."""
        # Test with full month name format
        result = TimeUtils.days_between_es_dates("1 June 2025", "10 June 2025")
        assert result == 9

        # Test with abbreviated month format
        result = TimeUtils.days_between_es_dates("1 Jun 2025", "10 Jun 2025")
        assert result == 9

    def test_days_between_es_dates_no_format_matched(self):
        """Test days_between_es_dates raises ValueError when no format matches."""
        with pytest.raises(ValueError, match="No format matched date text"):
            TimeUtils.days_between_es_dates("invalid format", "10/06/2025")

    def test_format_subtract_days_to_actual_date_zero_days(self, mock_datetime):
        """Test format_subtract_days_to_actual_date with zero days."""
        mock_dt, mock_now, _, _ = mock_datetime()
        # Mock strftime to return expected format
        mock_now.strftime.return_value = "11 June 2025"

        result = TimeUtils.format_subtract_days_to_actual_date(0)

        # Verify the correct format was used
        mock_now.strftime.assert_called_once_with("%d %B %Y")
        assert result == "11 June 2025"

    def test_format_subtract_days_to_actual_date_with_days(self, mock_datetime):
        """Test format_subtract_days_to_actual_date with specific number of days."""
        mock_dt, mock_now, mock_result, _ = mock_datetime()

        # Mock strftime to return expected format
        mock_result.strftime.return_value = "06 June 2025"

        result = TimeUtils.format_subtract_days_to_actual_date(5)

        # Verify the correct format was used
        mock_result.strftime.assert_called_once_with("%d %B %Y")
        assert result == "06 June 2025"

    def test_format_suffix_date_with_st_suffix(self):
        """Test format_suffix_date removes 'st' suffix."""
        result = TimeUtils.format_suffix_date("1st May 2025")
        assert result == "1 May 2025"

    def test_format_suffix_date_with_nd_suffix(self):
        """Test format_suffix_date removes 'nd' suffix."""
        result = TimeUtils.format_suffix_date("2nd May 2025")
        assert result == "2 May 2025"

    def test_format_suffix_date_with_rd_suffix(self):
        """Test format_suffix_date removes 'rd' suffix."""
        result = TimeUtils.format_suffix_date("3rd May 2025")
        assert result == "3 May 2025"

    def test_format_suffix_date_with_th_suffix(self):
        """Test format_suffix_date removes 'th' suffix."""
        result = TimeUtils.format_suffix_date("9th May 2025")
        assert result == "9 May 2025"

    def test_format_suffix_date_with_multiple_suffixes(self):
        """Test format_suffix_date removes multiple suffixes if present."""
        result = TimeUtils.format_suffix_date("1st of the 4th May 2025")
        assert result == "1 of e 4 May 2025"

    def test_format_suffix_date_no_suffix(self):
        """Test format_suffix_date returns unchanged string when no suffix present."""
        result = TimeUtils.format_suffix_date("9 May 2025")
        assert result == "9 May 2025"

    def test_format_suffix_date_empty_string(self):
        """Test format_suffix_date handles empty string."""
        result = TimeUtils.format_suffix_date("")
        assert result == ""

    # Additional edge cases for better coverage

    def test_days_between_dates_same_date(self):
        """Test days_between_dates when both dates are the same."""
        result = TimeUtils.days_between_es_dates("01/06/2025", "01/06/2025")
        assert result == 0

    def test_days_between_dates_reverse_order(self):
        """Test days_between_dates with dates in reverse chronological order."""
        result = TimeUtils.days_between_es_dates("10/06/2025", "01/06/2025")
        assert result == -9

    def test_format_days_ago_large_number(self, mock_datetime):
        """Test format_days_ago with a large number of days."""
        mock_dt, mock_now, mock_result, _ = mock_datetime()
        mock_result.strftime.return_value = "Jun 11, 2024"

        result = TimeUtils.format_days_ago(365)

        # Should call strftime with platform-appropriate format
        mock_result.strftime.assert_called_once()
        assert result == "Jun 11, 2024"

    def test_format_spanish_date_zero_days(self, mock_datetime):
        """Test format_spanish_date with zero days (today)."""
        mock_dt, mock_now, mock_result, _ = mock_datetime()
        mock_result.strftime.return_value = "11/06/2025"

        result = TimeUtils.format_spanish_date(0)

        assert result == "11/06/2025"

    # Additional tests to catch edge cases in days_between_dates parsing

    def test_days_between_dates_continue_loop_formats(self, mock_platform):
        """Test days_between_dates continues through format attempts on Windows."""
        mock_platform("Windows")
        result = TimeUtils.days_between_dates("Jun 01, 2025", "Jun 10, 2025")
        assert result == 9

    def test_days_between_dates_continue_loop_formats_unix(self, mock_platform):
        """Test days_between_dates continues through format attempts on Unix."""
        mock_platform("Linux")
        result = TimeUtils.days_between_dates("Jun 01, 2025", "Jun 10, 2025")
        assert result == 9

    def test_days_between_es_dates_continue_loop_formats(self):
        """Test days_between_es_dates continues through format attempts."""
        # This should work with the full month name format
        result = TimeUtils.days_between_es_dates("1 June 2025", "10 June 2025")
        assert result == 9
