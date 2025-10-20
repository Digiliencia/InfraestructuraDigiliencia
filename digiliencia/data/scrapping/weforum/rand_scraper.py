import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError
from digiliencia.utils.scrap import ScrapUtils

from .abc_news_scraper import AbstractNewsScraper

'''
Error scraping https://www.rand.org/pubs/perspectives/PEA4261-1.html:
 Attempted to scrape invalid page for Rand Corporation newsletter scrapper
'''

'''
2025-10-20 09:28:14.120 | ERROR    | digiliencia.data.scrapping.weforum.__main__:scrap_news:565 - Error scraping https://www.rand.org/pubs/research_reports/RRA4159-1.html:
 time data '5' does not match format '%b %d, %Y'
'''

class RandScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes Rand Corporation

        Args:
            url (str): Rand Corporation url article

        Raises:
            WEForumError: If the URL is not a valid Rand Corporation article URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Return:
            ScrapedNews: An object with the publication information.
        """
        # Verify URL  # TODO fix: 'list' object has no attribute 'text'
        if (
            "https://www.rand.org/pubs/research_reports/" not in url
        ):  # TODO fix: Error scraping https://www.rand.org/pubs/perspectives/PEA3886-1.html: Attempted to scrape invalid page for Rand Corporation newsletter scrapper
            raise WEForumError(
                "Attempted to scrape invalid page for Rand Corporation newsletter scrapper"
            )

        logger.debug(f"Scraping Rand Corporation story: {url}")
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)

        title = self.driver.find_element(By.ID, "RANDTitleHeadingId").text
        authors = self.driver.find_element(By.CLASS_NAME, "authors").text
        date = self.driver.find_element(
            By.CLASS_NAME, "published"
        ).text  # Mirar el formato de la fecha
        date = date[10:]
        date = date[10:]

        if ScrapUtils.if_element_exists(
            self.driver, By.CLASS_NAME, "abstract-first-letter"
        ):  # type: ignore
            introduction = self.driver.find_element(
                By.CLASS_NAME, "abstract-first-letter"
            ).text
        else:
            introduction = ""  # there is not introduction

        sections = self.driver.find_elements(By.TAG_NAME, "li")  # type: ignore
        content = introduction + " ".join([section.text for section in sections])

        return ScrapedNews(
            header=title,
            date=datetime.strptime(
                date, "%b %d, %Y"
            ),  # ERROR se cambio la B en mayuscula por una b en minuscula
            source="Rand Corporation",
            content=content,
            url=HttpUrl(url),
            authors=[authors],
            topics=None,
        )
