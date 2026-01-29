import time
from datetime import datetime
from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By
from digiliencia.utils.time import TimeUtils
from digiliencia.utils.scrap import ScrapUtils
from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError
from .abc_news_scraper import AbstractNewsScraper

"""
2025-10-21 16:30:51.162 | ERROR    | digiliencia.data.scrapping.weforum.__main__:scrap_news:564 - Error scraping https://www.eco-business.com/research/sustainability-a-business-essential-for-asean-smes-amidst-escalating-global-volatility/:
 redefinition of group name 'Y' as group 6; was group 1 at position 133
"""


class EcoBusinessScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes Eco-bussiness.

        Args:
            url (str): Eco-bussiness URL

        Raises:
            WEForumError: If the URL is not a valid Eco-bussiness URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Eco-bussiness: {url}")
        if "https://www.eco-business.com" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Eco-bussiness scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(By.ID, "ebStoryHeadline").text

        author_line = self.driver.find_element(
            By.CLASS_NAME, "eb-article__byline__author"
        ).text
        author_line = author_line.replace("By", "")
        authors = author_line.rsplit(",", 1)
        author = authors[0].strip()

        if ScrapUtils.if_element_exists(self.driver, By.TAG_NAME, "time"):  # type: ignore
            time_elem = self.driver.find_element(  # Esperar a que se carge
                By.TAG_NAME, "time"
            ).text
        else:
            time_elem = self.driver.find_element(
                By.CSS_SELECTOR, ".eb-article__byline__publish-date"
            ).text
        fmt_date = TimeUtils().detect_fomat_date(time_elem)
        date = datetime.strptime(time_elem, fmt_date)  # type: ignore

        content_container = self.driver.find_elements(
            By.CSS_SELECTOR, "section.eb-article__body-content p"
        )
        content = [contents.text for contents in content_container]
        content = "".join(content)

        return ScrapedNews(
            header=title,
            date=date,
            source="Eco-bussiness",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )
