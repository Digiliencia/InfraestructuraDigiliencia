# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 16:30:40 2025

@author: Álvaro Prieto Álvarez
Class to load environment variables from a .env file
"""

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

    @staticmethod
    def format_spanish_date(days_ago: int) -> str:
        """
        Formats a date based on the number of days ago in dd/mm/yyyy format.

        Args:
            days_ago (int): The number of days ago.

        Returns:
            str: A formatted string representing the date in dd/mm/yyyy format.
        """
        today = datetime.now()
        date_result = today - timedelta(days=days_ago)
        return date_result.strftime("%d/%m/%Y")

    @staticmethod
    def days_between_es_dates(date_str1: str, date_str2: str) -> int:
        """
        Calculates the difference in days between two dates in dd/mm/yyyy format.
        Args:
            date_str1 (str): The first date string (e.g., "1/10/2023").
            date_str2 (str): The second date string (e.g., "10/10/2023").
        Returns:
            int: The number of days between the two dates measured from the first to the second.
        Raises:
            ValueError: If the date strings are not in the correct format.
        Example:
            >>> TimeUtils.days_between_dates('1/10/2023', '10/10/2023')
            9
        """
        date_format = "%d/%m/%Y"
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        delta = date2 - date1
        return delta.days

    @staticmethod
    def format_subtract_days_to_actual_date(days: int=0) -> str:
        '''
       
        Args:
            days:
        Return: 
            A date subtract a days to actual date. If days = 0, else return actual date
            str: actual date or an earlier date with fomat: Year-Month-Day 
        Example:
            >>> subtract_days_to_actual_date()
            21 January 2025 # Actual Date
            >>> subtract_days_to_actual_date(2)
            19 January 2025
        '''
        date_actual = datetime.now()
        if(days == 0):
            format_date = date_actual.strftime("%d %B %Y") 
            return format_date
        else:
            days_subtract = timedelta(days)
            new_date = date_actual - days_subtract
            format_date = new_date.strftime("%d %B %Y") 
            return format_date

    @staticmethod
    def compare_two_dates(first_date: datetime, second_date:datetime) -> bool:
        '''

        Args:
            first_date
            second_date
        Return:
            True -> the first date is greater than the second
            False -> the second date is greater than the first
        '''
        date_first = datetime.strptime(first_date, "%d %B %Y").date()
        date_second = datetime.strptime(second_date, "%d %B %Y").date()

        if(date_first > date_second):
            return True
        else: 
            return False