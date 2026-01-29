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


class AsianDevelopmentBankScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes Asian Development Bank.

        Args:
            url (str): Asian Development Bank article URL.

        Raises:
            WEForumError: If the URL is not a valid Asian Development URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Scraping Asian Development Bank article: {url}")
        elems = {}
        if "https://development.asia/" in url:
            elems["title"] = ".title"
            elems["date"] = "time[class='datetime']"
            elems["content"] = "div.field__item p"
            elems["author"] = "p.meta a"
        elif "https://blogs.adb.org/blog/" in url:
            elems["title"] = ".article-title span"
            elems["date"] = "p.article-timestamp"
            elems["content"] = "main p"
            elems["author"] = "p.meta a"
        elif "https://www.adb.org/" in url:
            elems["title"] = "div.row h1"
            elems["date"] = ""
            elems["content"] = "ul li"
            elems["author"] = "li.field-item a"
        else:
            raise WEForumError(
                "Attempted to scrape invalid page for Asian Development Bank article scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(By.CSS_SELECTOR, elems["title"]).text

        if elems["date"] == "":
            date = datetime.now()
        else:
            time_elem = self.driver.find_element(By.CSS_SELECTOR, elems["date"]).text
            time_elem = time_elem.replace("Published: ", "")
            fmt_date = TimeUtils().detect_fomat_date(time_elem)
            if fmt_date is not None:
                date = datetime.strptime(time_elem, fmt_date)  # type: ignore
            else:
                logger.warning("Date has not detected. By default date is today.")
                date = datetime.now()

        content_container = self.driver.find_elements(By.CSS_SELECTOR, elems["content"])
        content = [contents.text for contents in content_container]
        content = "".join(content)

        if ScrapUtils.if_element_exists(self.driver, By.CSS_SELECTOR, elems["author"]):  # type: ignore
            author = self.driver.find_element(By.CSS_SELECTOR, elems["author"]).text
        else:
            author = "Asian Development Bank"  # There is not author

        return ScrapedNews(
            header=title,
            date=date,
            source="Asian Development Bank",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )
