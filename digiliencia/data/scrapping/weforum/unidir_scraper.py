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
        # This website takes a long time to load
        time.sleep(self.load_time + 1)  # Reject cookies if visible

        ScrapUtils.click_element(self.driver, "#cookiescript_reject")

        ScrapUtils.click_element(self.driver, "#cookiescript_reject")

        title = self.driver.find_element(By.CLASS_NAME, "post-title__heading").text

        time_elem = self.driver.find_element(
            By.CSS_SELECTOR, ".post-title__date-val"
        ).text
        
        try:
            date_ft = time_elem.replace(",", "")
            date = datetime.strptime(date_ft, TimeUtils().detect_fomat_date(time_elem))  # type: ignore 
        except ValueError:
            logger.warning("Date has not detected. By default date is today.")
            date = datetime.today()

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
