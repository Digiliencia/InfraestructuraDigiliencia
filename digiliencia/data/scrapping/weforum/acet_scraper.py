import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError

from .abc_news_scraper import AbstractNewsScraper


class ACETScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes African Center Economic Transformation.

        Args:
            url (str): The African Center Economic Transformation article URL

        Raises:
            WEForumError: If the URL is not a valid African Center Economic Transformation URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Scraping African Center Economic Transformation article: {url}")
        if "https://acetforafrica.org/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for African Center Economic Transformation article scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(
            By.CSS_SELECTOR, "div.et_pb_text_inner h1"
        ).text
        author = self.driver.find_element(
            By.CSS_SELECTOR, "div.dmach-postmeta-item-containter p span"
        ).text

        time_elem = self.driver.find_element(
            By.CSS_SELECTOR,
            "div.et_pb_module.et_pb_text.et_pb_text_3_tb_body.et_pb_text_align_left.et_pb_bg_layout_light div.et_pb_text_inner",
        ).text
        date_ft = time_elem.replace(",", "")
        date = datetime.strptime(date_ft, "%B %d %Y")  # type: ignore

        content_container = self.driver.find_elements(
            By.CSS_SELECTOR,
            "div.et_pb_module.et_pb_post_content.et_pb_post_content_0_tb_body p",
        )
        content = [contents.text for contents in content_container]
        content = "".join(content)

        return ScrapedNews(
            header=title,
            date=date,
            source="Australian Institute Of International Affairs",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )
