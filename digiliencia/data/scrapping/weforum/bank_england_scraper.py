import time
from datetime import datetime
from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By
from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError
from digiliencia.utils.scrap import ScrapUtils
from digiliencia.utils.time import TimeUtils
from .abc_news_scraper import AbstractNewsScraper

'''
 2025-10-21 16:32:49.891 | ERROR    | digiliencia.data.scrapping.weforum.__main__:scrap_news:564 - Error scraping https://www.bankofengland.co.uk/systemic-risk-survey/2025/2025-h2:
 Attempted to scrape invalid page for Bank of England article scrapper
'''

'''
 2025-10-21 16:31:39.939 | ERROR    | digiliencia.data.scrapping.weforum.__main__:scrap_news:564 - Error scraping https://blogs.lse.ac.uk/internationaldevelopment/2025/10/10/the-united-nations-new-ai-infrastructure-is-africas-strategic-edge/:
 Message: no such element: Unable to locate element: {"method":"css selector","selector":"div.mobile-post-main-image__date > h3:nth-of-type(4)"}
  (Session info: chrome=141.0.7390.108); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#nosuchelementexception
Stacktrace:


 2025-10-21 16:28:41.194 | ERROR    | digiliencia.data.scrapping.weforum.__main__:scrap_news:564 - Error scraping https://blogs.lse.ac.uk/europpblog/2025/10/14/attention-is-all-you-need-europe-should-decouple-from-us-technology-eurostack/:
 Message: no such element: Unable to locate element: {"method":"css selector","selector":"div.mobile-post-main-image__date > h3:nth-of-type(4)"}
  (Session info: chrome=141.0.7390.108); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#nosuchelementexception
Stacktrace:
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
        if ("https://blogs.lse.ac.uk/" not in url) or ("https://www.bankofengland.co.uk/" not in url):
            raise WEForumError(
                "Attempted to scrape invalid page for Bank of England article scrapper"
            )
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        if ScrapUtils().if_element_exists(self.driver, By.CSS_SELECTOR, "h1[itemprop='name']"): # type: ignore
            title = self.driver.find_element(By.CSS_SELECTOR, "h1[itemprop='name']").text
        elif ScrapUtils().if_element_exists(self.driver, By.CSS_SELECTOR, "h1[itemprop='name']"): # type: ignore
            title = self.driver.find_element(By.CSS_SELECTOR, "h1[itemprop='name']").text
        else:
            title = self.driver.find_element(By.CSS_SELECTOR, ".mobile-post-main-image__date + h1").text

        if ScrapUtils().if_element_exists(self.driver, By.CSS_SELECTOR, ".mobile-post-main-image__date h3"): # type: ignore
            time_elem = self.driver.find_elements(By.CSS_SELECTOR, ".mobile-post-main-image__date h3")[1].text
        elif ScrapUtils().if_element_exists(By.CSS_SELECTOR, ".published-date"): # type: ignore
            time_elem = self.driver.find_element(By.CSS_SELECTOR, ".published-date").text
        else:
            time_elem = self.driver.find_element(By.CLASS_NAME, "published-date").text

        fmt_date = TimeUtils().detect_fomat_date(time_elem)
        date_ft = time_elem.replace("Published on ", "")
        date = datetime.strptime(date_ft, fmt_date)  # type: ignore

        if ScrapUtils().if_element_exists(self.driver, By.CSS_SELECTOR, ".mobile-post-main-image__date h3"): # type: ignore
            author = self.driver.find_elements(By.CSS_SELECTOR, ".mobile-post-main-image__date h3")[0].text
        else:
            author = "Bank of England"  # There is not author

        if ScrapUtils().if_element_exists(self.driver, By.CSS_SELECTOR, "div[id='output'] p"): # type: ignore
            content_container = self.driver.find_elements(
                By.CSS_SELECTOR, "div[id='output'] p"
            )
        elif ScrapUtils().if_element_exists(self.driver, By.CSS_SELECTOR, ".page-section p"): # type: ignore
            content_container = self.driver.find_elements(
                By.CSS_SELECTOR, ".page-section p"
            )
        else:
            content_container = self.driver.find_elements(
                By.CSS_SELECTOR, ".post-content p"
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
