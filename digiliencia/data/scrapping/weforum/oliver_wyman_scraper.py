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
2025-10-20 09:33:18.425 | ERROR    | digiliencia.data.scrapping.weforum.__main__:scrap_news:565 - Error scraping https://www.oliverwyman.com/our-expertise/insights/2025/sep/operational-resilience-banks-southeast-asia.html:
 Message: no such element: Unable to locate element: {"method":"css selector","selector":"div.heading > div:first-child"}
  (Session info: chrome=141.0.7390.108); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#nosuchelementexception
Stacktrace:
        GetHandleVerifier [0x0xe3fe83+66515]
        GetHandleVerifier [0x0xe3fec4+66580]
'''

'''
2025-10-20 09:41:18.911 | ERROR    | digiliencia.data.scrapping.weforum.__main__:scrap_news:565 - Error scraping https://www.oliverwyman.com/our-expertise/perspectives/health/2025/september/from-ai-to-value-based-care-success-depends-on-execution.html:
 Message: no such element: Unable to locate element: {"method":"css selector","selector":"div.heading > div:first-child"}
  (Session info: chrome=141.0.7390.108); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#nosuchelementexception
Stacktrace:
        GetHandleVerifier [0x0xe3fe83+66515]
'''

class OliverWymanScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes Oliver Wyman.

        Args:
            url (str): Oliver Wyman article URL

        Raises:
            WEForumError: If the URL is not a valid Oliver Wyman URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Scraping Oliver Wyman article: {url}")
        elems = {}
        if "https://www.oliverwyman.com/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Oliver Wyman article scrapper"
            )
        else:
            if "our-expertise" == url:
                elems["title"] = ".page-banner__title"
                elems["author"] = "p.page-banner__authors"
                elems["content"] = "div.main-content p"
            else:
                elems["title"] = "div.text-primary.text-primary--subheading"
                elems["author"] = (
                    "div.authors.text-secondary.text-secondary--description__small"
                )
                elems["content"] = "div.text-secondary"

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        if ScrapUtils.if_element_exists(self.driver, By.CSS_SELECTOR, elems["title"]):  # type: ignore
            title = self.driver.find_element(By.CSS_SELECTOR, elems["title"]).text
        elif ScrapUtils.if_element_exists(self.driver, By.CSS_SELECTOR, "h1.text-primary.text-primary--subheading"): # type: ignore
            title = self.driver.find_element(By.CSS_SELECTOR, "h1.text-primary.text-primary--subheading").text
        else:
            title = self.driver.find_element(
                By.CSS_SELECTOR, "div.heading > div:first-child"
            ).text

        author_elem = self.driver.find_element(By.CSS_SELECTOR, elems["author"]).text
        author = "".join(author_elem.replace("By ", ""))

        date = datetime.now()  # article´s website without date

        contents_container = self.driver.find_element(By.CSS_SELECTOR, elems["content"])
        content = contents_container.text

        return ScrapedNews(
            header=title,
            date=date,
            source="Oliver Wyman",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )
