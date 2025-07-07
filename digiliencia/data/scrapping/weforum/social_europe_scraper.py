import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError
from digiliencia.utils.scrap import ScrapUtils
from digiliencia.utils.time import TimeUtils

from .abc_news_scraper import AbstractNewsScraper


class SocialEuropeScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes Social Europe.

        Args:
            url (str): The Social Europe article URL

        Raises:
            WEForumError: If the URL is not a valid Social Europe URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Scraping Social Europe article: {url}")
        if "https://www.socialeurope.eu/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for The Atlantic article scrapper"
            )

        ScrapUtils.disable_js(self.driver)  # Disable JS
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(By.CLASS_NAME, "entry-title").text

        authors_line = self.driver.find_element(By.CLASS_NAME, "entry-author").text
        authors_line = authors_line.replace(",", " ").replace("and", " ")
        authors = [authors_line.strip()]
        author = "".join(authors)

        time_elem = self.driver.find_element(By.CLASS_NAME, "entry-time").text
        date_without_suffix = TimeUtils.format_suffix_date(time_elem)

        date = datetime.strptime(date_without_suffix, "%d %B %Y")  # type: ignore

        content_container = self.driver.find_element(By.CLASS_NAME, "entry-content")
        content = content_container.text

        ScrapUtils.enable_js(self.driver)  # Enable JS again

        return ScrapedNews(
            header=title,
            date=date,
            source="Australian Institute Of International Affairs",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )
