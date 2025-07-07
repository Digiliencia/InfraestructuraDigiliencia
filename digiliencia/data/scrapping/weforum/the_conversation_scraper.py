import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError
from digiliencia.utils.scrap import ScrapUtils

from .abc_news_scraper import AbstractNewsScraper


class TheConversationScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes the publication.

        Args:
            url (str): The Conversation article URL

        Raises:
            WEForumError: If the URL is not a valid The Conversation URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Scraping The Conversation article: {url}")
        if "https://theconversation.com/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for The Conversation article scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)

        # Deny cookies if visible
        ScrapUtils.click_element(self.driver, ".didomi-continue-without-agreeing", 1)

        title = self.driver.find_element(By.CSS_SELECTOR, "h1").text

        authors_section = self.driver.find_element(By.CLASS_NAME, "content-authors")
        authors_list = authors_section.find_elements(By.TAG_NAME, "li")
        authors = [
            author.find_element(By.CLASS_NAME, "author-name").text
            for author in authors_list
        ]

        time_elem = self.driver.find_element(By.CSS_SELECTOR, ".timestamps time")
        date = datetime.fromisoformat(time_elem.get_attribute("datetime"))  # type: ignore

        content_elem = self.driver.find_element(By.CLASS_NAME, "entry-content")
        content = ""
        for element in content_elem.find_elements(By.XPATH, "./*"):
            if (
                element.tag_name == "h1"
                or element.tag_name == "h2"
                or element.tag_name == "h3"
            ):
                content += f"\n\n{element.text}\n"
            elif element.tag_name == "p":
                prev_sibling = element.find_elements(
                    By.XPATH, "preceding-sibling::*[1]"
                )
                next_sibling = element.find_elements(
                    By.XPATH, "following-sibling::*[1]"
                )
                if prev_sibling and next_sibling:
                    prev_sibling = prev_sibling[0]
                    next_sibling = next_sibling[0]
                    if prev_sibling.tag_name == "hr" and next_sibling.tag_name == "hr":
                        continue
                content += element.text + "\n\n"

        return ScrapedNews(
            header=title,
            date=date,
            source="The Conversation",
            content=content,
            url=HttpUrl(url),
            authors=authors,
            topics=None,
        )
