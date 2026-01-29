import time
from datetime import datetime
from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By
from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError
from .abc_news_scraper import AbstractNewsScraper
from digiliencia.utils.scrap import ScrapUtils


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
        if "https://www.nature.com/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Nature article scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        if ScrapUtils.if_element_exists(
            self.driver, By.CSS_SELECTOR, "h1.c-article-title"
        ):  # type: ignore
            elems["title"] = "h1.c-article-title"
        elif ScrapUtils.if_element_exists(
            self.driver, By.CSS_SELECTOR, "h1.Theme-StoryTitle"
        ):  # type: ignore
            elems["title"] = "h1.Theme-StoryTitle"
        else:
            elems["title"] = "h1.c-article-magazine-title"

        if ScrapUtils.if_element_exists(
            self.driver, By.CSS_SELECTOR, "li.c-article-identifiers__item time"
        ):  # type: ignore
            elems["date"] = "li.c-article-identifiers__item time"
        elif ScrapUtils.if_element_exists(
            self.driver, By.CSS_SELECTOR, ".Theme-Byline p"
        ):  # type: ignore
            elems["date"] = ".Theme-Byline p"
        else:
            elems["date"] = "li time"

        if ScrapUtils.if_element_exists(
            self.driver, By.CSS_SELECTOR, "div.c-article-body p"
        ):  # type: ignore
            elems["content"] = "div.c-article-body p"
        elif ScrapUtils.if_element_exists(
            self.driver, By.CSS_SELECTOR, "div.main-content p"
        ):  # type: ignore
            elems["content"] = "div.main-content p"
        else:
            elems["content"] = ".Theme-Layer-BodyText--inner p"

        if ScrapUtils.if_element_exists(
            self.driver, By.XPATH, "//li[@class='c-article-author-list__item']/a"
        ):  # type: ignore
            elems["author"] = "//li[@class='c-article-author-list__item']/a"
            author = self.driver.find_element(By.XPATH, elems["author"]).text
        else:
            author = ""  # There are not author

        title = self.driver.find_element(By.CSS_SELECTOR, elems["title"]).text

        time_elem = self.driver.find_element(By.CSS_SELECTOR, elems["date"]).text
        date_ft = time_elem.replace("Published: ", "")
        date = datetime.strptime(date_ft, "%d %B %Y")  # type: ignore

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
