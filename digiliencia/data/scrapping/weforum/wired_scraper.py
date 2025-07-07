import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.utils.scrap import ScrapUtils

from .abc_news_scraper import AbstractNewsScraper


class WiredScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """Access the given URL and scrapes the publication.

        Args:
            url (str): Wired story URL

        Raises:
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Scraping Wired story: {url}")
        # Disable JS
        ScrapUtils.disable_js(self.driver)

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)

        self._accept_cookies_if_visible("onetrust-accept-btn-handler")

        time_element = self.driver.find_element(By.TAG_NAME, "time")
        date_str = time_element.text
        date = datetime.strptime(
            date_str, "%b %d, %Y %I:%M %p"
        )  # TODO: take into account case like "Updated a month ago": https://www.wired.com/live/tiktok-scotus-live-coverage/

        author_element = self.driver.find_element(
            By.CSS_SELECTOR, '[data-testid="BylineName"]'
        )
        author = author_element.text

        title_element = self.driver.find_element(
            By.CSS_SELECTOR, 'h1[data-testid="ContentHeaderHed"]'
        )
        title = title_element.text

        content_elements = self.driver.find_elements(
            By.CSS_SELECTOR, "div.body__inner-container > p"
        )
        content = ""
        for element in content_elements:
            content += element.text + "\n"

        content = content
        ScrapUtils.enable_js(self.driver)  # Enable JS again
        return ScrapedNews(
            header=title,
            date=date,
            source="Wired",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )

    def _accept_cookies_if_visible(self, accept_bttn_id: str):
        """Accepts the cookies if the pop-up is visible.

        Args:
            accept_bttn_id (str): The ID of the accept button.
        """
        logger.debug("Accepting cookies if visible")
        if ScrapUtils.if_element_exists(self.driver, By.ID, accept_bttn_id):  # type: ignore
            accept_bttn = self.driver.find_element(By.ID, accept_bttn_id)
            if accept_bttn.is_displayed():
                accept_bttn.click()
                time.sleep(self.load_time)
