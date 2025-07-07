import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError

from .abc_news_scraper import AbstractNewsScraper


class EFFScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes Electronic Frontier Foundation deeplink.

        Args:
            url (str): Electronic Frontier Foundation deeplink URL

        Raises:
            WEForumError: If the URL is not a valid Electronic Frontier Foundation deeplink URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Scraping Electronic Frontier Foundation deeplink: {url}")
        if "https://www.eff.org/deeplinks/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Electronic Frontier Foundation deeplink scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(By.CSS_SELECTOR, "h1").text

        authors_line = self.driver.find_element(By.CLASS_NAME, "byline")
        authors = [
            author.text for author in authors_line.find_elements(By.TAG_NAME, "a")
        ]

        time_elem = self.driver.find_element(By.CLASS_NAME, "date")
        date = datetime.strptime(time_elem.text, "%B %d, %Y")  # type: ignore

        article = self.driver.find_element(By.CSS_SELECTOR, 'article[role="article"]')
        content_container = article.find_element(
            By.CSS_SELECTOR, "div.field--name-body"
        )
        content = content_container.text

        return ScrapedNews(
            header=title,
            date=date,
            source="Electronic Frontier Foundation",
            content=content,
            url=HttpUrl(url),
            authors=authors,
            topics=None,
        )
