import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError
from digiliencia.utils.scrap import ScrapUtils

from .abc_news_scraper import AbstractNewsScraper


class WarOnTheRocksScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes War on the Rocks.

        Args:
            url (str): War on the Rocks article URL.

        Raises:
            WEForumError: If the URL is not a valid War on the Rocks URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Scraping War on the Rocks article: {url}")
        if "https://warontherocks.com/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for War on the Rocks article scrapper"
            )
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        # TODO fix: Message: no such element: Unable to locate element: {"method":"tag name","selector":"h1"}
        if ScrapUtils.if_element_exists(
            self.driver, By.CSS_SELECTOR, "span.dynamic-hover"
        ):  # type: ignore
            title = self.driver.find_element(By.CSS_SELECTOR, "span.dynamic-hover").text
        else:
            title = self.driver.find_element(By.TAG_NAME, "h1").text

        authors_elem = self.driver.find_elements(
            By.CSS_SELECTOR, "a[class='author url fn']"
        )
        author = [authors.text for authors in authors_elem]
        author = "".join(author)
        # TODO fix: Message: no such element: Unable to locate element: {"method":"css selector","selector":"div[class='small-12 large-4 columns wotr_meta wotr_datetime']"}
        if ScrapUtils.if_element_exists(
            self.driver,
            By.CSS_SELECTOR,  # type: ignore
            r"div.tw\:text-gray-500:nth-child(3)",  # type: ignore
        ):
            time_elem = self.driver.find_element(
                By.CSS_SELECTOR, r"div.tw\:text-gray-500:nth-child(3)"
            ).text
        else:
            time_elem = self.driver.find_element(
                By.CSS_SELECTOR,
                "div[class='small-12 large-4 columns wotr_meta wotr_datetime']",
            ).text
        date = datetime.strptime(time_elem, "%B %d, %Y")  # type: ignore

        content_container = self.driver.find_elements(
            By.CSS_SELECTOR,
            "div[class='small-12 small-centered columns wotr_content'] p",
        )
        content = [contents.text for contents in content_container]
        content = "".join(content)

        return ScrapedNews(
            header=title,
            date=date,
            source="War on the Rocks",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )
