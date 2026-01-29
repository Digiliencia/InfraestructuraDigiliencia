import time
import dateparser
from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By
from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError
from digiliencia.utils.time import TimeUtils
from .abc_news_scraper import AbstractNewsScraper

"""
2025-10-21 16:35:14.004 | ERROR    | digiliencia.data.scrapping.weforum.__main__:scrap_news:564 - Error scraping https://www.iris-france.org/cybersecurite-le-facteur-humain-en-est-il-le-centre-de-gravite/:
 redefinition of group name 'Y' as group 6; was group 1 at position 133
"""


class IRISScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes Institut des Relations Internationales et Stratégiques.

        Args:
            url (str): Institut des Relations Internationales et Stratégiques article URL.

        Raises:
            WEForumError: If the URL is not a valid Institut des Relations Internationales et Stratégiques URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(
            f"Scraping Institut des Relations Internationales et Stratégiques article: {url}"
        )
        if "https://www.iris-france.org/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Institut des Relations Internationales et Stratégiques article scrapper"
            )
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(By.CSS_SELECTOR, "h1.article-title").text

        time_elem = self.driver.find_element(By.CSS_SELECTOR, "p.article-date").text
        date_ft = dateparser.parse(time_elem, languages=["fr"])
        date = date_ft.strptime(time_elem, TimeUtils().detect_fomat_date(time_elem))  # type: ignore

        author = self.driver.find_element(
            By.CSS_SELECTOR, "div.card-content p.card-title"
        ).text

        content_container = self.driver.find_elements(
            By.CSS_SELECTOR, "div.cms-content p"
        )
        content = [contents.text for contents in content_container]
        content = "".join(content)

        return ScrapedNews(
            header=title,
            date=date,
            source="Institut des Relations Internationales et Stratégiques",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )
