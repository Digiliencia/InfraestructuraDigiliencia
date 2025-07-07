import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError

from .abc_news_scraper import AbstractNewsScraper


class BankEnglandScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes Bank of England.

        Args:
            url (str): Bank of England article URL.

        Raises:
            WEForumError: If the URL is not a valid Bank of England URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        url = url
        logger.debug(f"Scraping Bank of England article: {url}")
        if "https://blogs.lse.ac.uk/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Bank of England article scrapper"
            )
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(By.CSS_SELECTOR, "h1[itemprop='name']").text

        time_elem = self.driver.find_element(By.CLASS_NAME, "published-date").text
        date_ft = time_elem.replace("Published on ", "")
        date = datetime.strptime(date_ft, "%B %d, %Y")  # type: ignore

        author = "Bank of England"  # There is not author

        content_container = self.driver.find_elements(
            By.CSS_SELECTOR, "div[id='output'] p"
        )
        content = [contents.text for contents in content_container]
        content = "".join(content)

        return ScrapedNews(
            header=title,
            date=date,
            source="Bank of England",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )
