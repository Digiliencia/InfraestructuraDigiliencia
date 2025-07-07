import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError

from .abc_news_scraper import AbstractNewsScraper


class FrontiersDigitalHealthScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes Frontiers in Digital Health.

        Args:
            url (str): Frontiers in Digital Health article URL.

        Raises:
            WEForumError: If the URL is not a valid Frontiers in Digital Health URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Scraping Frontiers in Digital Health article: {url}")
        if "https://www.frontiersin.org/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Frontiers in Digital Health article scrapper"
            )
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(
            By.CLASS_NAME, "JournalAbstract__titleWrapper"
        ).text

        time_elem = self.driver.find_element(
            By.XPATH, "//p[@class='ArticleLayoutHeader__info__journalDate']/span[2]"
        ).text
        date_ft = time_elem.replace(", ", "")
        date = datetime.strptime(date_ft, "%d %B %Y")  # type: ignore

        author_line = self.driver.find_elements(
            By.CSS_SELECTOR, "span.author-wrapper a"
        )
        author = [authors.text for authors in author_line]
        author = "".join(author)

        content_container = self.driver.find_elements(
            By.CSS_SELECTOR, "div.JournalFullText p"
        )
        content = [contents.text for contents in content_container]
        content = "".join(content)

        return ScrapedNews(
            header=title,
            date=date,
            source="Frontiers in Digital Health",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )
