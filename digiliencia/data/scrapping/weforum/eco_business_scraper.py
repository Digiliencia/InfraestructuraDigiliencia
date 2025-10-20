import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError

from .abc_news_scraper import AbstractNewsScraper

'''
Error scraping https://www.eco-business.com/news/asia-pacific-investment-in-smart-grids-could-free-up-us23-billion-by-2040-study/:
 time data '' does not match format '%B %d, %Y'
'''

'''
2025-10-20 09:23:51.950 | ERROR    | digiliencia.data.scrapping.weforum.__main__:scrap_news:565 - Error scraping https://www.eco-business.com/research/sustainability-a-business-essential-for-asean-smes-amidst-escalating-global-volatility/:
 time data 'Oct. 13, 2025' does not match format '%B %d, %Y'
'''

class EcoBusinessScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes Eco-bussiness.

        Args:
            url (str): Eco-bussiness URL

        Raises:
            WEForumError: If the URL is not a valid Eco-bussiness URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Eco-bussiness: {url}")
        if "https://www.eco-business.com" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Eco-bussiness scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(By.ID, "ebStoryHeadline").text

        author_line = self.driver.find_element(
            By.CLASS_NAME, "eb-article__byline__author"
        ).text
        author_line = author_line.replace("By", "")
        authors = author_line.rsplit(",", 1)
        author = authors[0].strip()

        time_elem = self.driver.find_element(  # Esperar a que se carge
            By.TAG_NAME, "time"
        ).text
        date = datetime.strptime(time_elem, "%B %d, %Y")  # type: ignore # TODO fix: time data '' does not match format '%B %d, %Y'

        content_container = self.driver.find_elements(
            By.CSS_SELECTOR, "section.eb-article__body-content p"
        )
        content = [contents.text for contents in content_container]
        content = "".join(content)

        return ScrapedNews(
            header=title,
            date=date,
            source="Eco-bussiness",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )
