# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 10:08:33 2025

@author: Carlos Prieto
Scrapping of website: https://www.ncsc.gov.uk/
"""

import time
from datetime import datetime
from loguru import logger
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from digiliencia.data.scrapping.abc_scraper import AbstractScraper
from digiliencia.utils.scrap import ScrapUtils
from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.exc.ncsc_exec import NcscExec
from digiliencia.configs.env import Env
from digiliencia.utils.time import TimeUtils


class Ncsc(AbstractScraper):
    def __init__(self):
        logger.debug("Initializing Scrapping of NCSC")
        self.scrapUtils = ScrapUtils()
        self.load = Env()
        self.driver = ScrapUtils.get_driver()
        self.articles: list[ScrapedNews] = []

    def _show_articles_until_date(self, until_date: str = ""):
        """
        Shows the browser all articles until a date give by param.

        Args:
            until_date (str), default without param
        """
        time.sleep(self.scrapUtils.timeout)
        logger.debug("Show all articles of topic")

        button_visible = True
        num_date = 1
        while button_visible:
            date_elem = self.driver.find_element(
                By.XPATH, f'(//li[@class="meta__item"])[{num_date}]'
            )
            date_ft = datetime.strptime(date_elem.text, "%d %b %Y").strftime("%d %B %Y")
            if TimeUtils.days_between_es_dates(until_date, date_ft) > 0:
                # Try to find the "Load more items" button
                button_load = self.driver.find_element(
                    By.XPATH, '//button[@data-testid="load-more-button"]'
                )
                button_load.click()  # Click the button
                num_date = num_date + 1
                time.sleep(
                    self.load.webdriverwait_timeout
                )  # Wait a few seconds for new articles to load
            else:
                button_visible = False

    def _show_all_articles(self):
        """ """
        time.sleep(self.scrapUtils.timeout)

        button_visible = True
        while button_visible:
            try:
                button_load = self.driver.find_element(
                    By.XPATH, '//button[@data-testid="load-more-button"]'
                )
                button_load.click()  # Click the button

                time.sleep(self.scrapUtils.timeout - 0.5)
            except NoSuchElementException:
                button_visible = False

    def _get_article_by_link(self, url: str = "") -> ScrapedNews | None:
        """
        Give an object ScrapedNewsModel is an articles of a topic. The article is given by param.

        Args:
            url (str): link to article

        Return:
            An object of ScrapedNewsModel, containing the article information.
        """
        try:
            self.driver.get(url)
            time.sleep(self.scrapUtils.timeout)

            title = self.driver.find_element(By.ID, "title").text
            contents = self.driver.find_elements(
                By.XPATH, '//div[@data-testid="pcf-BodyText"]'
            )
            content = "".join(i.text for i in contents)
            url = self.driver.current_url

            if self.scrapUtils.if_element_exists(
                self.driver,
                By.XPATH,  # type: ignore
                '//div[@class="details"]/p[@class="details__name"]',
            ):
                author = self.driver.find_element(
                    By.XPATH, '//div[@class="details"]/p[@class="details__name"]'
                ).text
            else:
                author = "Guidance"  # Case there is a Guidance, there is not an author

            date = datetime.now().strftime("%d %B %Y")
            if self.scrapUtils.if_element_exists(
                self.driver,
                By.CSS_SELECTOR,  # type: ignore
                ".group-wrap:first-child div div div div",
            ):
                date = self.driver.find_element(
                    By.CSS_SELECTOR,
                    ".group-wrap:first-child div div div div",
                ).text
            else:
                date = self.articles[-1].date.strftime("%d %B %Y")

            date_dt = datetime.strptime(date, "%d %B %Y")

            return ScrapedNews(
                header=title,
                date=date_dt,
                source="NCSC",
                content=content,
                url=url,
                authors=[author],
                topics=None,
            )

        except NoSuchElementException as e:
            logger.warning(f"ERROR Article NoSuchElementException {e}")

    def scrap_glosary(self):
        """
        Scrap subpage glosary, link: https://www.ncsc.gov.uk/section/advice-guidance/glossary
        The definitions is divided by sections

        Return:
            A list with all definitions, each defitions have a:

                Concept (str),
                Description (str),
        """
        concepts = []
        descriptions = []

        self.driver.get("https://www.ncsc.gov.uk/section/advice-guidance/glossary")
        self.scrapUtils.click_element(
            self.driver, "button.pcf-button:nth-child(2)", 1
        )  # Function to disable the cookie popup

        logger.info(f"Scrap subpage title: {self.driver.title}")

        definitions = self.driver.find_elements(
            By.CSS_SELECTOR, ".pcf-accordionItem.whiteBg"
        )
        logger.debug(f"Found {len(definitions)} definitions to process")
        for i in definitions:
            i.click()
            time.sleep(self.load.webdriverwait_timeout)
            concept = i.find_element(
                By.CSS_SELECTOR, "div.pcf-accordionItem.whiteBg h3"
            ).text
            concepts.append(concept)
            description = i.find_element(By.CSS_SELECTOR, "div.pcf-BodyText p").text
            descriptions.append(description)

        return {"concepts": concepts, "descriptions": descriptions}

    def scrap_news(self, from_days_ago: int = 0) -> list[ScrapedNews]:
        """
        Inicialite scrapping of website: https://www.ncsc.gov.uk/section/advice-guidance/all-articles?q=&defaultTypes=guidance,information,blog-post,collection&sort=date%2Bdesc

        Args:
            from_days_ago(int) default = 0, days back to scrape

        Example:
            >>> strat_scrapping(7)  # Run date in 20/03/2025, scrape all articles to 13/03/2025

        Return:
            None
        """
        try:
            url = "https://www.ncsc.gov.uk/section/advice-guidance/all-articles?q=&defaultTypes=guidance,information,blog-post,collection&sort=date%2Bdesc"

            self.driver.get(url)

            # Function to disable the cookie popup
            self.scrapUtils.click_element(
                self.driver, "button.pcf-button:nth-child(2)", 1
            )

            until_date = TimeUtils.format_subtract_days_to_actual_date(
                from_days_ago
            )  # Calculate date to scrap

            self._show_articles_until_date(until_date)

            # self._show_all_articles()

            articles_tag_a = self.driver.find_elements(By.CSS_SELECTOR, "a.reactLink")
            links_articles = [art.get_attribute("href") for art in articles_tag_a]

            logger.debug(f"Found {len(links_articles)} articles to process")
            for link in links_articles:
                art: ScrapedNews | None = self._get_article_by_link(str(link))
                if art is not None:
                    self.articles.append(art)

        except NcscExec as e:
            logger.error(f"ERROR: {e}")

        self.driver.quit()  # Close navegator
        return self.articles