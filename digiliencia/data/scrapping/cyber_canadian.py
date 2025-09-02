# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 10:08:33 2025

@author: Carlos Prieto Viñuela
Web scrapping: https://www.cyber.gc.ca/en/
"""

import time
from datetime import datetime
from loguru import logger
from selenium.webdriver.common.by import By
from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.data.scrapping.abc_scraper import AbstractScraper
from digiliencia.exc.canadian_exec import CanadianExec
from digiliencia.utils.scrap import ScrapUtils
from digiliencia.utils.time import TimeUtils
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CanadianScraper(AbstractScraper):
    def __init__(self):
        logger.debug("Initializing CanadianScraper")
        self.driver = ScrapUtils.get_driver()
        self.date_articles = []
        self.num_page = 1
        self.URLS_SECTIONS = {
            "individuals": "https://www.cyber.gc.ca/en/individuals",
            "small-medium-businesses": "https://www.cyber.gc.ca/en/small-medium-businesses",
            "infrastructure": "https://www.cyber.gc.ca/en/large-organizations-infrastructure",
            "goverment": "https://www.cyber.gc.ca/en/government-institutions",
            "academia": "https://www.cyber.gc.ca/en/academia",
        }

    def get_article(self, pos: int = 0) -> ScrapedNews | None:
        """
        Give an object ScrapedNewsModel is an articles of a section.

        Return:
            An article of a section is a ScrapedNews or None, if article is not good format.
        """
        try:
            time.sleep(1)  # Wait to load article
            title = self.driver.find_element(By.ID, "wb-cont").text
            date_dt = self.date_articles[pos]
            container_content = self.driver.find_elements(By.CSS_SELECTOR, "div p")
            content = [contents.text for contents in container_content]
            content = "".join(content)
            url = self.driver.current_url
            author = ""  # There is not an author

            return ScrapedNews(
                header=title,
                date=date_dt,
                source="Canadian Center for Cybersegurity",
                content=content,
                url=str(url),   # type: ignore
                authors=[author],
                topics=None,
            )
        except CanadianExec as e:
            logger.warning("Article is not good format: ", e)
            return None

    def _is_there_button_next(self) -> bool:
        """
        Return:
            True: button next is disabled.
            False: button next is not disabled.
        """
        return ScrapUtils.if_element_exists(self.driver, By.ID, "table_next")  # type: ignore

    def scrap_section(self, url: str = "", until_date: str = "") -> list[ScrapedNews]:
        """
        Scrapes all articles in a section up to the date given by parameter.

        Args:
            url(str): The URL to open a section
            until_date(str): scrape up to this date

        Return:
            A list with all articles of a section.
        """
        self.driver.get(url)
        name_section = url.replace("https://www.cyber.gc.ca/en/", "")
        logger.debug(f"Scrap articles of section: {name_section}")

        articles_section: list[ScrapedNews] = []

        while self._is_there_button_next:
            table = self.driver.find_element(By.ID, "table")
            body = table.find_element(By.TAG_NAME, "tbody")
            rows_body = body.find_elements(By.TAG_NAME, "tr")

            links = [row.find_element(By.TAG_NAME, "a").get_attribute("href") for row in rows_body]
            
            pos = 0 # Busco la posición del último artículo hasta la fecha dada
            flag = False
            for row in rows_body:
                date_str = row.find_element(By.CLASS_NAME, "sorting_1").text
                date_dt = datetime.strptime(date_str, "%Y-%m-%d")
                self.date_articles.append(date_dt)
                date_ft = date_dt.strftime("%d %B %Y")

                if TimeUtils.days_between_es_dates(date_ft, until_date) > 0:
                    flag = True
                    break
                else:
                    pos = pos + 1

            if flag: # En la página, se encuentra el último artículo a extraer los datos
                for i, link in enumerate(links):
                    if pos == i: # Si la posición coincide con el ultimo articulo a extraer los datos, para el algoritmo
                        break
                    self.driver.get(str(link))
                    article = self.get_article(i)
                    if article is not None:
                        articles_section.append(article)
                break
            else:
                for i, link in enumerate(links):
                    self.driver.get(str(link))
                    article = self.get_article(i)
                    if article is not None:
                        articles_section.append(article)
                     
            if self._is_there_button_next:   
                #wait = WebDriverWait(self.driver, 10)
                #wait.until(EC.presence_of_element_located((By.ID, "table_next")))
                button_next = self.driver.find_element(By.ID, "table_next")
                button_next.click()   
       
        return articles_section

    def scrap_news(self, from_days_ago: int) -> list[ScrapedNews]:
        """
        Call the methods to get the information from the Canadian page

        Args:
            from_days_ago (int): The number of days to get the information from

        Returns:
            list[ScrapNews]: A list with several objects ScrapNews
        """
        logger.info(f"Getting events from {from_days_ago} days ago")
        if from_days_ago < 0:
            logger.error("from_days_ago must be greater than 0")
            raise ValueError("from_days_ago must be greater than 0")

        news_articles: list[ScrapedNews] = []

        until_date = TimeUtils.format_subtract_days_to_actual_date(from_days_ago)

        logger.info(f"Total sections to scrap: {len(self.URLS_SECTIONS)}")
        for name in self.URLS_SECTIONS:
            articles = self.scrap_section(self.URLS_SECTIONS[name], until_date)
            news_articles.extend(articles)

        logger.info("Finish scrap to Canadian Center for Cybersegurity.")
        return news_articles
