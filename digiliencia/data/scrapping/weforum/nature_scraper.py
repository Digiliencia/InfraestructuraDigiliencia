import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError

from .abc_news_scraper import AbstractNewsScraper


class NatureScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes Nature.

        Args:
            url (str): Nature article URL.

        Raises:
            WEForumError: If the URL is not a valid Nature URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Scraping Nature article: {url}")
        elems = {}
        # TODO ERROR: articles con varios identificadores diferentes
        if "https://www.nature.com/" in url:
            if "articles" in url:
                elems["title"] = "h1.c-article-title"
                elems["date"] = "li.c-article-identifiers__item time"
                elems["author"] = "//li[@class='c-article-author-list__item']/a"
                elems["content"] = "div.c-article-body p"
            else:
                elems["title"] = (
                    "h1.c-article-magazine-title"  # https://www.nature.com/articles/d41586-025-01034-x
                )
                elems["date"] = "li time"
                elems["author"] = "//li[@class='c-article-author-list__item']/a"
                elems["content"] = "div.main-content p"
        else:
            raise WEForumError(
                "Attempted to scrape invalid page for Nature article scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(By.CSS_SELECTOR, elems["title"]).text

        time_elem = self.driver.find_element(By.CSS_SELECTOR, elems["date"]).text
        date_ft = time_elem.replace("Published: ", "")
        date = datetime.strptime(date_ft, "%d %B %Y")  # type: ignore

        author = self.driver.find_element(By.XPATH, elems["author"]).text

        content_container = self.driver.find_elements(By.CSS_SELECTOR, elems["content"])
        content = [contents.text for contents in content_container]
        content = "".join(content)

        return ScrapedNews(
            header=title,
            date=date,
            source="Nature",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )
