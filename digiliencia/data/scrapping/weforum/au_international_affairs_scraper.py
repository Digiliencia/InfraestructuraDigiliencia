import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError
from digiliencia.utils.scrap import ScrapUtils

from .abc_news_scraper import AbstractNewsScraper


class AuInternationalAffairsScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes Australian Institute Of International Affairs page.

        Args:
            url (str): Australian Institute Of International Affairs URL

        Raises:
            WEForumError: If the URL is not a valid Australian Institute Of International Affairs URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Scraping Australian Institute Of International Affairs: {url}")
        if "https://www.internationalaffairs.org.au/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Australian Institute Of International Affairs scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        if ScrapUtils.if_element_exists(self.driver, By.CLASS_NAME, "post-title"):  # type: ignore
            title = self.driver.find_element(By.CLASS_NAME, "post-title").text
        else:
            title = self.driver.find_element(By.CSS_SELECTOR, ".entry-title").text

        authors_line = self.driver.find_element(By.CLASS_NAME, "author-name").text
        authors_line = authors_line.replace("By ", "")
        authors = [
            author.strip() for author in authors_line.replace(" and ", ", ").split(",")
        ]
        author = ", ".join(authors)

        time_elem = self.driver.find_element(By.CLASS_NAME, "publish-date")
        date = datetime.strptime(time_elem.text, "%d %b %Y")  # type: ignore

        content_container = self.driver.find_elements(
            By.CSS_SELECTOR, "div.body-content p"
        )
        content = [contents.text for contents in content_container]
        content = "".join(content)

        return ScrapedNews(
            header=title,
            date=date,
            source="Australian Institute Of International Affairs",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )
