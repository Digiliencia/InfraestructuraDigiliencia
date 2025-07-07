import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError
from digiliencia.utils.time import TimeUtils

from .abc_news_scraper import AbstractNewsScraper


class LondonSchoolEconomicsScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes London School of Economics and Political Science.

        Args:
            url (str): London School of Economics and Political Science article URL.

        Raises:
            WEForumError: If the URL is not a valid London School of Economics and Political Science URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(
            f"Scraping London School of Economics and Political Science article: {url}"
        )
        if "https://blogs.lse.ac.uk/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for London School of Economics and Political Science article scrapper"
            )
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(
            By.CSS_SELECTOR, "div.container.container--small h1"
        ).text

        time_elem = self.driver.find_element(  # TODO fix: Message: no such element: Unable to locate element: {"method":"css selector","selector":"div.mobile-post-main-image__date > h3:nth-of-type(4)"}
            By.CSS_SELECTOR, "div.mobile-post-main-image__date > h3:nth-of-type(4)"
        ).text
        date_ft = TimeUtils.format_suffix_date(
            time_elem
        )  # TODO fix: time data 'Sebaian Schwartz' does not match format '%B %d %Y'
        date_ft = date_ft.replace(",", "")
        date = datetime.strptime(date_ft, "%B %d %Y")  # type: ignore

        author = self.driver.find_element(
            By.XPATH, "//div[@class='mobile-post-main-image__date']/h3[1]"
        ).text

        contents_container = self.driver.find_elements(
            By.CSS_SELECTOR, "div.post-content p"
        )
        content = [contents.text for contents in contents_container]
        content = "".join(content)

        return ScrapedNews(
            header=title,
            date=date,
            source="London School of Economics and Political Science",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )
