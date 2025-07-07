import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError

from .abc_news_scraper import AbstractNewsScraper


class DCAFScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes Geneva Centre for Security Sector Governance (DCAF).

        Args:
            url (str): Geneva Centre for Security Sector Governance (DCAF) article URL.

        Raises:
            WEForumError: If the URL is not a valid Geneva Centre for Security Sector Governance (DCAF) URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(
            f"Scraping Geneva Centre for Security Sector Governance (DCAF) article: {url}"
        )
        if "https://www.dcaf.ch/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Geneva Centre for Security Sector Governance (DCAF) article scrapper"
            )
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(By.CLASS_NAME, "title").text

        time_elem = self.driver.find_element(
            By.CLASS_NAME, "publication-date-display"
        ).text
        date = datetime.strptime(time_elem, "%d %B, %Y")  # type: ignore

        author = self.driver.find_element(
            By.CSS_SELECTOR, "div[itemprop='author']"
        ).text

        content = self.driver.find_element(
            By.CSS_SELECTOR, "div[itemprop='description']"
        ).text

        return ScrapedNews(
            header=title,
            date=date,
            source="Geneva Centre for Security Sector Governance (DCAF)",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )
