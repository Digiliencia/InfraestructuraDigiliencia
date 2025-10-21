import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError

from .abc_news_scraper import AbstractNewsScraper

'''
 2025-10-21 16:33:18.641 | ERROR    | digiliencia.data.scrapping.weforum.__main__:scrap_news:564 - Error scraping https://www.institutmontaigne.org/en/expressions/trump-tech-right-and-christian-nationalists-unnatural-coalition:
 time data '' does not match format '%d/%m/%Y'
'''

'''
2025-10-21 16:26:50.220 | ERROR    | digiliencia.data.scrapping.weforum.__main__:scrap_news:564 - Error scraping https://www.institutmontaigne.org/rencontres/usue-digital-ia-cloud-leurope-peut-elle-encore-reagir:
 Message: no such element: Unable to locate element: {"method":"css selector","selector":"div.date"}
  (Session info: chrome=141.0.7390.108); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#nosuchelementexception
Stacktrace:
'''

class InstitutMontaigneScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes Institut Montaigne.

        Args:
            url (str): Institut Montaigne article URL.

        Raises:
            WEForumError: If the URL is not a valid Institut Montaigne URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Scraping Institut Montaigne article: {url}")
        if "https://www.institutmontaigne.org/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Institut Montaigne article scrapper"
            )
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(By.CSS_SELECTOR, "h1[class='titre_3']").text

        time_elem = self.driver.find_element(By.CSS_SELECTOR, "div.date").text
        date = datetime.strptime(time_elem, "%d/%m/%Y")  # type: ignore

        author = self.driver.find_element(By.CSS_SELECTOR, "div.auteur__nom").text

        content_container = self.driver.find_elements(By.CSS_SELECTOR, "div p")
        content = [contents.text for contents in content_container]
        content = "".join(content)

        return ScrapedNews(
            header=title,
            date=date,
            source="Institut Montaigne",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )
