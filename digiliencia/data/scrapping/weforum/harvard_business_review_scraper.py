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
2025-10-21 16:35:39.170 | ERROR    | digiliencia.data.scrapping.weforum.__main__:scrap_news:564 - Error scraping https://hbr.org/2025/10/make-better-strategic-decisions-amid-uncertainty:
 Message: no such element: Unable to locate element: {"method":"css selector","selector":"div.Title_standard__x_GEq.Title_standard__x_GEq"}   
  (Session info: chrome=141.0.7390.108); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#nosuchelementexception
Stacktrace:
'''

class HarvardBusinessReviewScraper(AbstractNewsScraper):
    def scrap(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes Harvard Business Review.

        Args:
            url (str): Harvard Business Review article URL

        Raises:
            WEForumError: If the URL is not a valid Harvard Business Review URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
        """
        logger.debug(f"Scraping Harvard Business Review article: {url}")
        elems = {}
        if "https://hbr.org/" in url:
            if "podcast" in url:
                elems["title"] = "h1.podcast-post__banner-title.podcast__h2"
                elems["date"] = (
                    "span[class='podcast-details__date publication-date text-gray']"
                )
                elems["content"] = "section[id='details-section'] p"
                elems["topic"] = "a[class='topic--large']"
            elif "sponsored" in url:
                elems["title"] = "h1[class=sponsored-article-hed]"
                elems["date"] = ".publication-date"
                elems["content"] = "content p"
                elems["topic"] = "a strong em"
            else:
                elems["title"] = "div.Title_standard__x_GEq.Title_standard__x_GEq"
                elems["date"] = (
                    "div.PublicationDate_standard__rpflO.PublicationDate_non-magazine-date-container__Ln4Wl"
                )
                elems["content"] = "div.Standard_content__mghDk p"
                elems["topic"] = (
                    "div.MainTopicLink_container__L7tHy.MainTopicLink_standard__WcK3Y"
                )
        else:
            raise WEForumError(
                "Attempted to scrape invalid page for Harvard Business Review article scrapper"
            )

        ScrapUtils.disable_js(self.driver)  # Disable JS

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(By.CSS_SELECTOR, elems["title"]).text

        time_elem = self.driver.find_element(By.CSS_SELECTOR, elems["date"]).text
        date_ft = time_elem.replace(",", "")
        date = datetime.strptime(date_ft, TimeUtils().detect_fomat_date(time_elem))  # type: ignore 

        content_container = self.driver.find_elements(By.CSS_SELECTOR, elems["content"])
        content = [contents.text for contents in content_container]
        content = "".join(content)

        if ScrapUtils.if_element_exists(self.driver, By.CSS_SELECTOR, elems["topic"]):  # type: ignore
            topic = self.driver.find_element(By.CSS_SELECTOR, elems["topic"]).text
        else:
            topic = ""

        author = "HBR"  # There is not an author

        ScrapUtils.enable_js(self.driver)  # Enable JS again

        return ScrapedNews(
            header=title,
            date=date,
            source="Harvard Business Review",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=[topic],
        )
