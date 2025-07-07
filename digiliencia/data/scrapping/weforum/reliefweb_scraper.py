import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError

from .abc_news_scraper import AbstractNewsScraper


class ReliefwebScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes ReliefWeb.

        Args:
            url (str): ReliefWeb article URL.

        Raises:
            WEForumError: If the URL is not a valid ReliefWeb URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Scraping ReliefWeb article: {url}")
        if "https://reliefweb.int/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for ReliefWeb article scrapper"
            )
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(
            By.CSS_SELECTOR, ".rw-article__title.rw-article__title"
        ).text

        date = datetime.now()

        contents_container = self.driver.find_elements(
            By.CSS_SELECTOR, "div.rw-report__content p"
        )
        content = [contents.text for contents in contents_container]
        content = "".join(content)

        author = "ReliefWeb"  # There is not author

        return ScrapedNews(
            header=title,
            date=date,
            source="ReliefWeb",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )
