import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError

from .abc_news_scraper import AbstractNewsScraper


class NextCityScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes Next City.

        Args:
            url (str): Next City article URL.

        Raises:
            WEForumError: If the URL is not a valid Next City URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Scraping Next City article: {url}")
        if "https://nextcity.org/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Next City article scrapper"
            )
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(By.CLASS_NAME, "daily-title").text

        time_elem = self.driver.find_element(
            By.CSS_SELECTOR, "span[itemprop='datePublished']"
        ).text
        date = datetime.strptime(time_elem, "%B %d, %Y")  # type: ignore

        authors_line = self.driver.find_elements(
            By.CSS_SELECTOR, "span[itemprop='author']"
        )
        author = [authors.text for authors in authors_line]
        author = "".join(author)

        contents_container = self.driver.find_elements(
            By.CSS_SELECTOR, "div.entry-content p"
        )
        content = [contents.text for contents in contents_container]
        content = "".join(content)

        return ScrapedNews(
            header=title,
            date=date,
            source="Next City",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )
