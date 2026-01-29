import time
from datetime import datetime
from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By
from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError
from digiliencia.utils.scrap import ScrapUtils
from digiliencia.utils.time import TimeUtils
from .abc_news_scraper import AbstractNewsScraper

"""
 2025-10-21 16:30:37.287 | ERROR    | digiliencia.data.scrapping.weforum.__main__:scrap_news:564 - Error scraping https://www.rand.org/pubs/perspectives/PEA4261-1.html:
 redefinition of group name 'Y' as group 6; was group 1 at position 133
"""


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
        if "https://www.rand.org" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Rand Corporation newsletter scrapper"
            )

        logger.debug(f"Scraping Rand Corporation story: {url}")
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)

        title = self.driver.find_element(By.ID, "RANDTitleHeadingId").text
        authors = self.driver.find_element(By.CLASS_NAME, "authors").text

        time_elem = self.driver.find_element(
            By.CLASS_NAME, "published"
        ).text  # Mirar el formato de la fecha
        time_elem.replace("Published ", "")
        date_ft = datetime.strptime(time_elem, TimeUtils().detect_fomat_date(time_elem))  # type: ignore

        if ScrapUtils.if_element_exists(
            self.driver,
            By.CLASS_NAME,
            "abstract-first-letter",  # type: ignore
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
            date=date_ft,
            source="Rand Corporation",
            content=content,
            url=HttpUrl(url),
            authors=[authors],
            topics=None,
        )
