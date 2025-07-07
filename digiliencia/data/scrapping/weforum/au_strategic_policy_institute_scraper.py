import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError

from .abc_news_scraper import AbstractNewsScraper


class AuStrategicInstituteScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """Access the given URL and scrapes the publication.

        Args:
            url (str): Australian Strategic Policy Institute URL

        Raises:
            WEForumError: If the URL is not a valid Australian Strategic Policy Institute URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Scraping Australian Strategic Policy Institute: {url}")
        if "https://www.aspistrategist.org.au/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Australian Strategic Policy Institute scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)

        # Get the title
        title = self.driver.find_element(By.CLASS_NAME, "entry-title").text

        # Get the date
        date_elem = self.driver.find_element(
            By.CSS_SELECTOR, "article > header > .meta"
        )
        date = datetime.fromisoformat(date_elem.get_attribute("datetime"))  # type: ignore

        # Get the author
        author_elems = self.driver.find_elements(
            By.CSS_SELECTOR, "article > header > .meta > .author"
        )
        authors = [author_elem.text for author_elem in author_elems]

        # Get the content
        content_div = self.driver.find_element(By.CLASS_NAME, "entry-content")
        content = ""
        for element in content_div.find_elements(By.XPATH, "./*"):
            tag = element.tag_name
            if tag == "p":
                content += element.text + "\n\n"
            elif tag == "h3":
                content += f"{element.text}\n"
            elif tag == "ul":
                for li in element.find_elements(By.TAG_NAME, "li"):
                    content += f"* {li.text}\n"
            elif tag == "ol":
                for i, li in enumerate(element.find_elements(By.TAG_NAME, "li"), 1):
                    content += f"{i}. {li.text}\n"
            elif tag == "img":
                img_link = element.get_attribute("src")
                img_alt = element.get_attribute("alt")
                content += f"![{img_alt}]({img_link})\n"

        content = content
        return ScrapedNews(
            header=title,
            date=date,
            source="Australian Strategic Policy Institute",
            content=content,
            url=HttpUrl(url),
            authors=authors,
            topics=None,
        )
