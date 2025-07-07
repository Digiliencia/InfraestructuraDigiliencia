import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError

from .abc_news_scraper import AbstractNewsScraper


class DIWBerlinScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes DIW Berlin.

        Args:
            url (str): DIW Berlin article URL.

        Raises:
            WEForumError: If the URL is not a valid DIW Berlin URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Scraping DIW Berlin article: {url}")
        if "https://www.diw.de/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for DIW Berlin article scrapper"
            )
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(By.CLASS_NAME, "header_text").text

        author = self.driver.find_element(By.CSS_SELECTOR, "a[class='info_link']").text

        date = datetime.now()  # There is not date

        content_container = self.driver.find_elements(
            By.CSS_SELECTOR, "div[class='row justify-content-md-center'] p"
        )
        content = [contents.text for contents in content_container]
        content = "".join(content)

        return ScrapedNews(
            header=title,
            date=date,
            source="DIW Berlin",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )
