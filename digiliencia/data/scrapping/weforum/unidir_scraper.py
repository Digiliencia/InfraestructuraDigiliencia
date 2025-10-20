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
2025-10-20 09:41:47.056 | ERROR    | digiliencia.data.scrapping.weforum.__main__:scrap_news:565 - Error scraping https://unidir.org/publication/evaluating-the-alignment-between-budgetary-allocations-and-national-security-priorities-exploratory-case-study-kenya/:
 time data '' does not match format '%d %B %Y'
'''

class UnidirScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes UNIDIR.

        Args:
            url (str): UNIDIR article URL.

        Raises:
            WEForumError: If the URL is not a valid UNIDIR URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Scraping UNIDIR article: {url}")
        if "https://unidir.org/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for UNIDIR article scrapper"
            )
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        ScrapUtils.click_element(self.driver, "#cookiescript_reject")

        ScrapUtils.click_element(self.driver, "#cookiescript_reject")

        title = self.driver.find_element(By.CLASS_NAME, "post-title__heading").text

        time_elem = self.driver.find_element(
            By.CSS_SELECTOR, ".post-title__date-val"
        ).text
        date = datetime.strptime(time_elem, "%d %B %Y")  # type: ignore

        author = "UNIDIR"  # There are not author

        content_container = self.driver.find_elements(
            By.CSS_SELECTOR, "div.post-content p"
        )
        content = [contents.text for contents in content_container]
        content = "".join(content)

        return ScrapedNews(
            header=title,
            date=date,
            source="UNIDIR",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )
