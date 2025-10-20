import time
from datetime import datetime
from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By
from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.WEForum_exc import WEForumError
from digiliencia.utils.time import TimeUtils
from .abc_news_scraper import AbstractNewsScraper

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

        if time_data is not None:
            fmt_date = TimeUtils().detect_fomat_date(time_data)
            if  fmt_date is not None:
                date = datetime.strptime(time_data, fmt_date)  # type: ignore
            else:
                logger.warning("The format of date has not detected. By default, date is today.")
                date = datetime.today()
        else:
            logger.warning("The format of date has not detected. By default, date is today.")
            date = datetime.today()
            

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
