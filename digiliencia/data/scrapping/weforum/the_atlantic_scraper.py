import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError
from digiliencia.utils.scrap import ScrapUtils

from .abc_news_scraper import AbstractNewsScraper


class TheAtlanticScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes The Atlantic.

        Args:
            url (str): The Atlantic article URL

        Raises:
            WEForumError: If the URL is not a valid The Atlantic URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Scraping The Atlantic article: {url}")
        if "https://www.theatlantic.com" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for The Atlantic article scrapper"
            )

        # Disable JS
        ScrapUtils.disable_js(self.driver)

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)

        title = self.driver.find_element(By.CSS_SELECTOR, "h1").text

        authors_line = self.driver.find_element(By.ID, "byline")
        authors = [
            author.text for author in authors_line.find_elements(By.TAG_NAME, "a")
        ]

        time_elem = self.driver.find_element(By.TAG_NAME, "time")
        date = datetime.fromisoformat(time_elem.get_attribute("datetime"))  # type: ignore

        content_elem = self.driver.find_element(
            By.CLASS_NAME, "ArticleBody_root__2gF81"
        )
        content = ""
        for element in content_elem.find_elements(By.XPATH, "./*"):
            if (
                element.tag_name == "p"
                and element.get_attribute("data-view-action") is not None
            ):
                continue
            else:
                content += element.text + "\n\n"

        ScrapUtils.enable_js(self.driver)  # Enable JS again

        return ScrapedNews(
            header=title,
            date=date,
            source="The Atlantic",
            content=content,
            url=HttpUrl(url),
            authors=authors,
            topics=None,
        )
