import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError

from .abc_news_scraper import AbstractNewsScraper


class CoronellUniversityScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes Cornell University.

        Args:
            url (str): Cornell University article URL.

        Raises:
            WEForumError: If the URL is not a valid Cornell University URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Scraping Cornell University article: {url}")
        if "https://news.cornell.edu/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Cornell University article scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(
            By.CSS_SELECTOR, "header.expanded.stories h1"
        ).text

        time_elem = self.driver.find_element(By.CSS_SELECTOR, "span.byline time").text
        date_ft = time_elem.replace(",", "")
        date = datetime.strptime(date_ft, "%b %d %Y")  # type: ignore

        author = self.driver.find_element(By.CSS_SELECTOR, "h2.byline span").text

        content_container = self.driver.find_elements(
            By.CSS_SELECTOR, "div.field__item p"
        )
        content = [contents.text for contents in content_container]
        content = "".join(content)

        return ScrapedNews(
            header=title,
            date=date,
            source="Cornell University",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )
