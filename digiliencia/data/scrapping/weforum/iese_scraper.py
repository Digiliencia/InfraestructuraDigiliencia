import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError
from digiliencia.utils.scrap import ScrapUtils

from .abc_news_scraper import AbstractNewsScraper


class IESEScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes IESE.

        Args:
            url (str): IESE article URL

        Raises:
            WEForumError: If the URL is not a valid IESE URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Scraping IESE article: {url}")
        if "https://www.iese.edu/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for IESE article scrapper"
            )

        ScrapUtils.disable_js(self.driver)  # Disable JS

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(By.CLASS_NAME, "title").text

        time_elem = self.driver.find_element(By.CLASS_NAME, "small-txt").text
        date_ft = time_elem.replace(",", "")
        date = datetime.strptime(date_ft, "%B %d %Y")  # type: ignore

        authors_elem = self.driver.find_element(
            By.XPATH, '//div[@class="content description-subHeader"]/p[1]'
        ).text
        author = authors_elem.replace("By", "")

        content_container = self.driver.find_elements(
            By.XPATH, '//div[@class="content description-subHeader"]/p'
        )
        content = [contents.text for contents in content_container]
        content = "".join(content)

        ScrapUtils.enable_js(self.driver)  # Enable JS again

        return ScrapedNews(
            header=title,
            date=date,
            source="IESE",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )
