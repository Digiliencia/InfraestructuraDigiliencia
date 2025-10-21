import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError

from .abc_news_scraper import AbstractNewsScraper

'''
2025-10-21 16:40:14.995 | ERROR    | digiliencia.data.scrapping.weforum.__main__:scrap_news:564 - Error scraping https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2025.1687708/full:
 Message: no such element: Unable to locate element: {"method":"css selector","selector":"div.JournalAbstract__titleWrapper h1"}
  (Session info: chrome=141.0.7390.108); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#nosuchelementexception
Stacktrace:
'''
'''
 2025-10-21 16:29:54.437 | ERROR    | digiliencia.data.scrapping.weforum.__main__:scrap_news:564 - Error scraping https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2025.1595310/full:
 Message: no such element: Unable to locate element: {"method":"css selector","selector":".JournalAbstract__titleWrapper"}
  (Session info: chrome=141.0.7390.108); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#nosuchelementexception
Stacktrace:
'''

class FrontiersScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes Frontiers.

        Args:
            url (str): Frontiers article URL.

        Raises:
            WEForumError: If the URL is not a valid Frontiers URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Scraping Frontiers article: {url}")
        if "https://www.frontiersin.org/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Frontiers article scrapper"
            )
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(
            By.CSS_SELECTOR, "div.JournalAbstract__titleWrapper h1"
        ).text

        time_elem = self.driver.find_element(
            By.XPATH, '//p[@class="ArticleLayoutHeader__info__journalDate"]/span[2]'
        ).text
        date_ft = time_elem.replace(", ", "")
        date = datetime.strptime(date_ft, "%d %B %Y")  # type: ignore

        authors_group = self.driver.find_elements(By.CLASS_NAME, "authors")
        author = [authors.text for authors in authors_group]
        author = "".join(author)

        content_container = self.driver.find_element(By.CLASS_NAME, "JournalFullText")
        content = content_container.text

        return ScrapedNews(
            header=title,
            date=date,
            source="GovLab - Living Library",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )
