import time
from datetime import datetime
from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By
from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError
from .abc_news_scraper import AbstractNewsScraper
from digiliencia.utils.scrap import ScrapUtils


class GovlabLivingLibraryScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes GovLab - Living Library.

        Args:
            url (str): GovLab - Living Library article URL.

        Raises:
            WEForumError: If the URL is not a valid GovLab - Living Library URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Scraping GovLab - Living Library article: {url}")
        if "https://thelivinglib.org/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for GovLab - Living Library article scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        if ScrapUtils.if_element_exists(self.driver, By.CSS_SELECTOR, "h1.entry-title"):  # type: ignore
            title = self.driver.find_element(By.CSS_SELECTOR, "h1.entry-title").text
        else:
            title = self.driver.find_element(By.CSS_SELECTOR, ".brxe-post-title").text

        if ScrapUtils.if_element_exists(
            self.driver, By.CSS_SELECTOR, "time.entry-date.published"
        ):  # type: ignore
            time_elem = self.driver.find_element(
                By.CSS_SELECTOR, "time.entry-date.published"
            ).text
            date_ft = time_elem.replace(",", "")
            date = datetime.strptime(date_ft, "%B %d %Y")  # type: ignore
        else:
            date = datetime.today()

        if ScrapUtils.if_element_exists(
            self.driver, By.CSS_SELECTOR, "span.author.vcard"
        ):  # type: ignore
            author = self.driver.find_element(By.CSS_SELECTOR, "span.author.vcard").text
        else:
            author = self.driver.find_element(By.CSS_SELECTOR, "h2.author-name").text

        if ScrapUtils.if_element_exists(
            self.driver, By.CSS_SELECTOR, "div.entry-content p"
        ):  # type: ignore
            content_container = self.driver.find_elements(
                By.CSS_SELECTOR, "div.entry-content p"
            )
            content = [contents.text for contents in content_container]
            content = "".join(content)
        else:
            content = self.driver.find_element(
                By.CSS_SELECTOR, ".brxe-post-content p"
            ).text

        return ScrapedNews(
            header=title,
            date=date,
            source="GovLab - Living Library",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )
