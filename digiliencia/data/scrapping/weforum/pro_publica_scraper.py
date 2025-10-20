import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError

from .abc_news_scraper import AbstractNewsScraper

'''
2025-10-20 09:40:14.749 | ERROR    | digiliencia.data.scrapping.weforum.__main__:scrap_news:565 - Error scraping https://www.propublica.org/article/pentagon-dod-microsoft-digital-escorts-china-ban-cybersecurity:
 time data '2025-09-19EDT05:00' does not match format '%Y-%m-%dEST%H:%M'
'''

class ProPublicaScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """Access the given URL and scrapes the publication.

        Args:
            url (str): ProPublica article URL

        Raises:
            WEForumError: If the URL is not a valid ProPublica article URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Scraping ProPublica article: {url}")
        if "https://www.propublica.org/article/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for ProPublica article scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time * 1.5)

        # Get the title
        title = self.driver.find_element(By.TAG_NAME, "h1").text

        # Get the date
        time_elems = self.driver.find_elements(By.TAG_NAME, "time")
        for elm in time_elems:
            if elm.get_attribute("datetime"):
                time_elem = elm
                break
        time_data = time_elem.get_attribute("datetime")  # type: ignore
        date = datetime.strptime(time_data, "%Y-%m-%dEST%H:%M")  # type: ignore

        # Get the author
        authors_elem = self.driver.find_element(
            By.XPATH, '//*[@id="main"]/article/div[2]/div/[1]span[1]'
        )
        authors = []
        for elem in authors_elem.find_elements(By.XPATH, ".//p"):
            if elem.tag_name in ["span", "a"]:
                authors.append(elem.text)

        # Get the content
        content_div = self.driver.find_element(By.CLASS_NAME, "article-body")
        content = ""
        for p in content_div.find_elements(By.TAG_NAME, "p"):
            content += p.text + "\n\n"

        return ScrapedNews(
            header=title,
            date=date,
            source="ProPublica",
            content=content,
            url=HttpUrl(url),
            authors=authors,
            topics=None,
        )
