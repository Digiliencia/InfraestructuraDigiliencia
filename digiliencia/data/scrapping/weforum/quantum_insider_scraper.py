import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError
from digiliencia.utils.scrap import ScrapUtils

from .abc_news_scraper import AbstractNewsScraper


class QuantumInsiderScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """Access the given URL and scrapes the post.

        Args:
            url (str): The Quantum Insider URL

        Raises:
            WEForumError: If the URL is not a valid The Quantum Insider URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Scraping The Quantum Insider: {url}")
        if not url.startswith("https://thequantuminsider.com/"):
            raise WEForumError(
                "Attempted to scrape invalid page for The Quantum Insider scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time + 1)

        # Disable JS
        ScrapUtils.disable_js(self.driver)

        # Get the title
        title = self.driver.find_element(
            By.CSS_SELECTOR,
            "h1[class='elementor-heading-title elementor-size-default']",
        ).text

        # Get the date
        if ScrapUtils.if_element_exists(By.CSS_SELECTOR, "span time"):  # type: ignore
            date_element = self.driver.find_element(By.CSS_SELECTOR, "span time")
        else:
            date_element = self.driver.find_element(
                By.CSS_SELECTOR, ".elementor-post-info__item--type-custom"
            )
        date = datetime.strptime(date_element.text, "%B %d, %Y")

        # Get the author
        author = self.driver.find_element(
            By.CLASS_NAME, "elementor-post-info__item--type-author"
        ).text

        # Get the content
        content_container = self.driver.find_element(
            By.CSS_SELECTOR, "#cst-p-css .elementor-widget-container"
        )
        content = ""
        elements = content_container.find_elements(By.XPATH, "./*")
        for element in elements:
            tag = element.tag_name
            if tag == "p":
                content += element.text + "\n\n"
            elif tag == "h3":
                content += f"\n\n{element.text}\n"
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

        ScrapUtils.enable_js(self.driver)  # Enable JS again

        return ScrapedNews(
            header=title,
            date=date,
            source="The Quantum Insider",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )
