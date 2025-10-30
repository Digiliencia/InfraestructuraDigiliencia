import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError

from .abc_news_scraper import AbstractNewsScraper

'''
- Error scraping https://www.findevgateway.org/blog/2025/10/driving-womens-empowerment-and-economy-one-chat-at-time:
 Message: no such element: Unable to locate element: {"method":"css selector","selector":".author"}
  (Session info: chrome=141.0.7390.123); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#nosuchelementexception
Stacktrace:
        GetHandleVerifier [0x0x3dfe43+66515]
        GetHandleVerifier [0x0x3dfe84+66580]
        (No symbol) [0x0x1cdc48]
        (No symbol) [0x0x218704]
'''

class FindevGatewayScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes FinDev Gateway.

        Args:
            url (str): FinDev Gateway article URL.

        Raises:
            WEForumError: If the URL is not a valid FinDev Gateway URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Scraping FinDev Gateway article: {url}")
        if "https://www.findevgateway.org/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for FinDev Gateway article scrapper"
            )
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(
            By.CSS_SELECTOR, "div.field--name-node-title h1"
        ).text

        time_elem = self.driver.find_element(
            By.CSS_SELECTOR,
            "div.heading div.field--name-field-date-m-y.field--type-datetime.field--label-hidden.field__item time.datetime",
        ).text
        date = datetime.strptime(time_elem, "%d %B %Y")  # type: ignore

        author = self.driver.find_element(By.CLASS_NAME, "author").text

        contents_container = self.driver.find_elements(
            By.CSS_SELECTOR, "div.text-formatted.field.field--name-body p"
        )
        content = [contents.text for contents in contents_container]
        content = "".join(content)

        return ScrapedNews(
            header=title,
            date=date,
            source="FinDev Gateway",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )
