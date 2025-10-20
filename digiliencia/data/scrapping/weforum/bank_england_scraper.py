import time
from datetime import datetime

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError

from .abc_news_scraper import AbstractNewsScraper

'''
Error scraping https://www.bankofengland.co.uk/report/2025/the-boes-approach-to-innovation-in-ai-dlt-quantum-computing:
 Attempted to scrape invalid page for Bank of England article scrapper
'''

'''
2025-10-20 09:21:57.153 | ERROR    | digiliencia.data.scrapping.weforum.__main__:scrap_news:565 - Error scraping https://blogs.lse.ac.uk/europpblog/2025/10/14/attention-is-all-you-need-europe-should-decouple-from-us-technology-eurostack/:
 Message: no such element: Unable to locate element: {"method":"css selector","selector":"div.mobile-post-main-image__date > h3:nth-of-type(4)"}
  (Session info: chrome=141.0.7390.108); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#nosuchelementexception
Stacktrace:
        GetHandleVerifier [0x0xe3fe83+66515]
        GetHandleVerifier [0x0xe3fec4+66580]
        (No symbol) [0x0xc2dc48]
        (No symbol) [0x0xc78704]
'''

'''
2025-10-20 09:40:06.248 | ERROR    | digiliencia.data.scrapping.weforum.__main__:scrap_news:565 - Error scraping https://blogs.lse.ac.uk/usappblog/2025/09/19/geopolitics-isnt-killing-global-supply-chains-its-powering-them/:
 Message: no such element: Unable to locate element: {"method":"css selector","selector":"div.mobile-post-main-image__date > h3:nth-of-type(4)"}
  (Session info: chrome=141.0.7390.108); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#nosuchelementexception
Stacktrace:
        GetHandleVerifier [0x0xe3fe83+66515]
'''

class BankEnglandScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes Bank of England.

        Args:
            url (str): Bank of England article URL.

        Raises:
            WEForumError: If the URL is not a valid Bank of England URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        url = url
        logger.debug(f"Scraping Bank of England article: {url}")
        if "https://blogs.lse.ac.uk/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Bank of England article scrapper"
            )
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(By.CSS_SELECTOR, "h1[itemprop='name']").text

        time_elem = self.driver.find_element(By.CLASS_NAME, "published-date").text
        date_ft = time_elem.replace("Published on ", "")
        date = datetime.strptime(date_ft, "%B %d, %Y")  # type: ignore

        author = "Bank of England"  # There is not author

        content_container = self.driver.find_elements(
            By.CSS_SELECTOR, "div[id='output'] p"
        )
        content = [contents.text for contents in content_container]
        content = "".join(content)

        return ScrapedNews(
            header=title,
            date=date,
            source="Bank of England",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )
