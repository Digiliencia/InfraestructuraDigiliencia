import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError

from .abc_news_scraper import AbstractNewsScraper

'''
2025-10-18 16:57:42.450 | ERROR    | digiliencia.data.scrapping.weforum.__main__:scrap_news:565 - Error scraping https://thelivinglib.org/proprietary-data-open-data-data-commons-who-owns-the-data-how-to-best-reconcile-conflicting-interests-in-exploiting-the-value-of-data-and-protecting-against-its-risks/:
 Message: no such element: Unable to locate element: {"method":"css selector","selector":"h1.entry-title"}
  (Session info: chrome=141.0.7390.77); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#nosuchelementexception
'''

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

        title = self.driver.find_element(By.CSS_SELECTOR, "h1.entry-title").text

        time_elem = self.driver.find_element(
            By.CSS_SELECTOR, "time.entry-date.published"
        ).text
        date_ft = time_elem.replace(",", "")
        date = datetime.strptime(date_ft, "%B %d %Y")  # type: ignore

        author = self.driver.find_element(By.CSS_SELECTOR, "span.author.vcard").text

        content_container = self.driver.find_elements(
            By.CSS_SELECTOR, "div.entry-content p"
        )
        content = [contents.text for contents in content_container]
        content = "".join(content)

        return ScrapedNews(
            header=title,
            date=date,
            source="GovLab - Living Library",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )
