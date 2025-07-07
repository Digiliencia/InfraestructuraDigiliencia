import locale
import time
from datetime import datetime

import dateparser
from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError
from digiliencia.utils.time import TimeUtils

from .abc_news_scraper import AbstractNewsScraper


class TrendsResearchAdvisoryScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes TRENDS Research & Advisory.

        Args:
            url (str): TRENDS Research & Advisory article URL.

        Raises:
            WEForumError: If the URL is not a valid TRENDS Research & Advisory URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Scraping TRENDS Research & Advisory article: {url}")
        if "https://trendsresearch.org/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for TRENDS Research & Advisory article scrapper"
            )
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(
            By.CSS_SELECTOR, "div[class='inner-text'] span"
        ).text

        time_elem = self.driver.find_element(By.CSS_SELECTOR, "div.inner-text p").text
        if TimeUtils.is_format_date_arabe(time_elem):
            date_ft = dateparser.parse(time_elem, languages=["ar"])
            date = date_ft.strptime(time_elem, "%d %b %Y")  # type: ignore   # ERROR con la B en mayuscula
            locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
        else:
            date = datetime.strptime(time_elem, "%d %b %Y")  # type: ignore

        author = self.driver.find_element(By.CSS_SELECTOR, "div.auth-pos h3").text

        contents_container = self.driver.find_elements(
            By.CSS_SELECTOR, "div.sp-content-full p"
        )
        content = [contents.text for contents in contents_container]
        content = "".join(content)

        return ScrapedNews(
            header=title,
            date=date,
            source="TRENDS Research & Advisory",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )
