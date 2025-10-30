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
2025-10-30 10:08:13.173 | ERROR    | digiliencia.data.scrapping.weforum.__main__:scrap_news:564 - Error scraping https://hbr.org/sponsored/2025/10/the-business-rewards-and-identity-risks-of-agentic-ai:
 time data 'October 10 2025' does not match format '%B %d, %Y'
'''

'''
Error scraping https://hbr.org/sponsored/2025/10/how-ai-will-forge-the-next-generation-of-cybersecurity-talent:
 time data 'October 29 2025' does not match format '%B %d, %Y'
'''

'''
 2025-10-30 10:07:14.415 | ERROR    | digiliencia.data.scrapping.weforum.__main__:scrap_news:564 - Error scraping https://hbr.org/2025/10/how-to-lead-when-the-conditions-for-success-suddenly-disappear:
 ScrapUtils.if_element_exists() missing 1 required positional argument: 'element'
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
        if "https://hbr.org/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Harvard Business Review article scrapper"
            )

        ScrapUtils.disable_js(self.driver)  # Disable JS

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        if ScrapUtils().if_element_exists(self.driver, By.CSS_SELECTOR, "h1.podcast-post__banner-title.podcast__h2"): # type: ignore
            title = self.driver.find_element(By.CSS_SELECTOR, "h1.podcast-post__banner-title.podcast__h2").text
        elif ScrapUtils().if_element_exists(self.driver, By.CSS_SELECTOR, "h1[class=sponsored-article-hed]"): # type: ignore
            title = self.driver.find_element(By.CSS_SELECTOR, "h1[class=sponsored-article-hed]").text
        elif ScrapUtils().if_element_exists(By.CSS_SELECTOR, "div.Title_standard__x_GEq.Title_standard__x_GEq"): # type: ignore
            title = self.driver.find_element(By.CSS_SELECTOR, "div.Title_standard__x_GEq.Title_standard__x_GEq").text
        else:
            title = self.driver.find_element(By.CSS_SELECTOR, ".Title_title__MZ67h.Title_premium__fWYHg").text

        if ScrapUtils().if_element_exists(self.driver, By.CSS_SELECTOR, "span[class='podcast-details__date publication-date text-gray']"): # type: ignore
            time_elem = self.driver.find_element(By.CSS_SELECTOR, "span[class='podcast-details__date publication-date text-gray']").text
        elif ScrapUtils().if_element_exists(self.driver, By.CSS_SELECTOR, ".publication-date"): # type: ignore
            time_elem = self.driver.find_element(By.CSS_SELECTOR, ".publication-date").text
        elif ScrapUtils().if_element_exists(self.driver, By.CSS_SELECTOR, "div.PublicationDate_standard__rpflO.PublicationDate_non-magazine-date-container__Ln4Wl"): # type: ignore
            time_elem = self.driver.find_element(By.CSS_SELECTOR, "div.PublicationDate_standard__rpflO.PublicationDate_non-magazine-date-container__Ln4Wl").text
        else:
            time_elem = self.driver.find_element(By.CSS_SELECTOR, ".PublicationDate_non-magazine-date___Oz7L").text

        date_ft = time_elem.replace(",", "")
        date = datetime.strptime(date_ft, TimeUtils().detect_fomat_date(time_elem))  # type: ignore 

        if ScrapUtils().if_element_exists(self.driver, By.CSS_SELECTOR, "section[id='details-section'] p"): # type: ignore
            content_container = self.driver.find_elements(By.CSS_SELECTOR, "section[id='details-section'] p")
        elif ScrapUtils().if_element_exists(self.driver, By.CSS_SELECTOR, "content p"): # type: ignore
            content_container = self.driver.find_elements(By.CSS_SELECTOR, "content p")
        elif ScrapUtils().if_element_exists(self.driver, By.CSS_SELECTOR, "div.Standard_content__mghDk p"): # type: ignore
            content_container = self.driver.find_elements(By.CSS_SELECTOR, "div.Standard_content__mghDk p")
        else:
            content_container = self.driver.find_elements(By.TAG_NAME, "p")

        content = [contents.text for contents in content_container]
        content = "".join(content)

        if ScrapUtils().if_element_exists(self.driver, By.CSS_SELECTOR, "a[class='topic--large']"):  # type: ignore
            topic = self.driver.find_element(By.CSS_SELECTOR, "a[class='topic--large']").text
        elif ScrapUtils().if_element_exists(self.driver, By.CSS_SELECTOR, "a strong em"): # type: ignore
            topic = self.driver.find_element(By.CSS_SELECTOR, "a strong em").text
        elif ScrapUtils().if_element_exists(self.driver, By.CSS_SELECTOR, "div.MainTopicLink_container__L7tHy.MainTopicLink_standard__WcK3Y"): # type: ignore
            topic = self.driver.find_element(By.CSS_SELECTOR, "div.MainTopicLink_container__L7tHy.MainTopicLink_standard__WcK3Y").text
        else:
            topic = "" # There is not a topic

        if ScrapUtils().if_element_exists(self.driver, By.CSS_SELECTOR, ".Byline_author__SdVEf"): # type: ignore
            author = self.driver.find_element(By.CSS_SELECTOR, ".Byline_author__SdVEf").text
        else:
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
