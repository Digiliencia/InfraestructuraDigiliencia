import time
from datetime import datetime
from urllib.parse import parse_qs, urlparse

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError

from .abc_news_scraper import AbstractNewsScraper


class GlobalDataScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """Access the given URL and scrapes the publication.

        Args:
            url (str): GlobalData newsletter details URL

        Raises:
            WEForumError: If the URL is not a valid GlobalData newsletter details URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Scraping GlobalData newsletter: {url}")
        # Verify URL
        if "https://www.globaldata.com/newsletter/details" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for GlobalData newsletter scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)

        # Extract date from URL parameter if available
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        newsletter_date = query_params.get("newsletterdate", [None])[0]
        if newsletter_date:
            date = datetime.strptime(newsletter_date, "%Y-%m-%d")
        else:
            raise WEForumError(
                "newsletter date not found in URL. Cannot set publication date."
            )

        title_element = self.driver.find_element(By.CSS_SELECTOR, "h2>a")
        title = title_element.text

        content_container = title_element.find_element(By.XPATH, "./../../..")
        content = content_container.text
        content = content.replace(title, "")  # Remove title from content

        return ScrapedNews(
            header=title,
            date=date,
            source="GlobalData",
            content=content,
            url=HttpUrl(url),
            authors=[],
            topics=None,
        )
