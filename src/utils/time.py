from datetime import datetime, timedelta
import platform


class TimeUtils:
    @staticmethod
    def format_days_ago(days_ago: int) -> str:
        """
        Formats a date based on the number of days ago.
        If the number of days ago is less than 7, it returns a string indicating the number of days ago.
        Otherwise, it returns the date in a formatted string.
        Args:
            days_ago (int): The number of days ago.
        Returns:
            str: A formatted string representing the date or the number of days ago.
        Raises:
            ValueError: If days_ago is negative.
        Example:
            >>> TimeUtils.age_format_date(3)
            '3 days ago'
            >>> TimeUtils.age_format_date(10)
            'Oct 1, 2023'
        """
        if days_ago < 1:
            raise ValueError("days_ago must be positive")

        today = datetime.now()
        if days_ago == 1:
            return "1 day ago"
        elif days_ago < 7:
            return f"{days_ago} days ago"
        else:
            date_result = today - timedelta(days=days_ago)

            # Detecta el sistema operativo y usa el formato adecuado
            if platform.system() == "Windows":
                date_format = "%b %#d, %Y"  # Formato para Windows
            else:
                date_format = "%b %-d, %Y"  # Formato para Unix/Linux/MacOS

            return date_result.strftime(date_format)

    @staticmethod
    def days_between_dates(date_str1: str, date_str2: str) -> int:
        """
        Calculates the difference in days between two dates.
        Args:
            date_str1 (str): The first date string (e.g., "3 days ago" or "Oct 1, 2023").
            date_str2 (str): The second date string (e.g., "1 day ago" or "Oct 10, 2023").
        Returns:
            int: The number of days between the two dates measured from the first to the second.
        Raises:
            ValueError: If the date strings are not in the correct format.
        Example:
            >>> TimeUtils.days_between_dates('3 days ago', 'Oct 10, 2023')
            7
        """

        def parse_date(date_str: str) -> datetime:
            # Handle "N days ago"
            if "day" in date_str and "ago" in date_str:
                try:
                    days_ago = int(date_str.split()[0])
                    return datetime.now() - timedelta(days=days_ago)
                except ValueError:
                    raise ValueError(f"Invalid relative date format: {date_str}")

            # Handle formatted dates like "Oct 1, 2023"
            if platform.system() == "Windows":
                formats = [
                    "%b %#d, %Y",
                    "%b %d, %Y",
                ]  # Handle both variants for Windows
            else:
                formats = [
                    "%b %-d, %Y",
                    "%b %d, %Y",
                ]  # Handle both variants for Unix/Linux/MacOS

            for date_format in formats:
                try:
                    return datetime.strptime(date_str, date_format)
                except ValueError:
                    continue

            raise ValueError(f"Invalid absolute date format: {date_str}")

        # Parse both dates
        try:
            date1 = parse_date(date_str1)
            date2 = parse_date(date_str2)
        except ValueError as e:
            raise ValueError(f"Error parsing dates: {e}")

        # Calculate the difference in days
        delta = date2 - date1
        return delta.days
