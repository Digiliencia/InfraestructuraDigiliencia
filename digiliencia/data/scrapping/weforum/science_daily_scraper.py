import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError

from .abc_news_scraper import AbstractNewsScraper


class SienceDailyScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes Science Daily

        Args:
            url (str): Science Daily url article

        Raises:
            WEForumError: If the URL is not a valid Science Daily article URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Return:
            ScrapedNews: An object with the publication information.
        """
        # Verify URL
        if "https://www.sciencedaily.com/releases/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Science Daily newsletter scrapper"
            )

        logger.debug(f"Scraping Science Daily story: {url}")
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)

        title = self.driver.find_element(By.ID, "headline").text
        content = self.driver.find_element(By.ID, "text").text
        date = self.driver.find_element(
            By.ID, "date_posted"
        ).text  # Mirar el formato de la fecha
        authors = self.driver.find_element(By.ID, "source").text

        return ScrapedNews(
            header=title,
            date=datetime.strptime(date, "%B %d, %Y"),
            source="Science Daily",
            content=content,
            url=HttpUrl(url),
            authors=[authors],
            topics=None,
        )
