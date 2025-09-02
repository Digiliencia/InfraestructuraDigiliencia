# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 10:08:33 2025

@author: Carlos Prieto Viñuela
Web scrapping: https://www.asd.gov.au/
"""

import time
from datetime import datetime
from loguru import logger
from selenium.webdriver.common.by import By
from digiliencia.data.scrapping.abc_scraper import AbstractScraper
from digiliencia.utils.scrap import ScrapUtils
from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.utils.time import TimeUtils
from digiliencia.exc.america_cyber_agency_exec import AmericaCyberAgencyExec

class AmericaCyberAgencyScraper(AbstractScraper):
    def __init__(self):
        logger.debug("Initializing website America's CyberDefense Agency.")
        self.driver = ScrapUtils.get_driver()
        self.URLS_SECTIONS = {
            "news": "https://www.cisa.gov/news-events/news",
            "advisories": "https://www.cisa.gov/news-events/cybersecurity-advisories",
            "directives": "https://www.cisa.gov/news-events/directives"
        }

    def get_article(self) -> ScrapedNews | None:
        """
        Give an object ScrapedNews is an articles of a section.

        Return:
            An article of a section is a ScrapedNews or None, if article is not good format.
        """
        try:
            time.sleep(1)  # Wait to load article
            title = self.driver.find_element(By.CSS_SELECTOR, ".c-page-title__title").text
            date_str = str(self.driver.find_element(By.CSS_SELECTOR, ".c-field__content time").text)
            date_dt = datetime.strptime(date_str, "%B %d, %Y")
            topics_elem = self.driver.find_elements(By.CSS_SELECTOR, ".c-top__topics")
            topics = [str(topic.text) + " " for topic in topics_elem]
            container_content = self.driver.find_elements(By.CSS_SELECTOR, ".c-field__content")
            content = [contents.text for contents in container_content]
            content = "".join(content)
            url = self.driver.current_url
            author = ""  # There is not an author
            
            return ScrapedNews(
                header=title,
                date=date_dt,
                source="Canadian Center for Cybersegurity",
                content=content,
                url=str(url),       # type: ignore
                authors=[author],
                topics=topics,
            )
        except AmericaCyberAgencyExec as e:
            logger.warning("Article is not good format: ", e)
            return None
    
    def _is_there_button_next(self) -> bool:
        """
        Return:
            True: button next is disabled.
            False: button next is not disabled.
        """
        return ScrapUtils.if_element_exists(self.driver, By.CSS_SELECTOR, ".c-pager__item.c-pager__item--next")  # type: ignore

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
        name_section = url.replace("https://www.cisa.gov/news-events/", "")
        logger.debug(f"Scrap articles of section: {name_section}")

        articles_section: list[ScrapedNews] = []

        while self._is_there_button_next:
            articles = self.driver.find_elements(By.CSS_SELECTOR, ".c-teaser__title")
            links = [art.find_element(By.TAG_NAME, "a").get_attribute("href") for art in articles]

            pos = 0 # Busco la posición del último artículo hasta la fecha dada
            flag = False
            dates_page = self.driver.find_elements(By.CSS_SELECTOR, ".c-teaser__date time")
            for date in dates_page:
                date_dt = datetime.strptime(str(date.text), "%b %d, %Y") 
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
                        article = self.get_article()
                        if article is not None:
                            articles_section.append(article)
                break
            else:
                for i, link in enumerate(links):
                    self.driver.get(str(link))
                    article = self.get_article()
                    if article is not None:
                        articles_section.append(article)
            
            if self._is_there_button_next:
                button_next = self.driver.find_element(By.CSS_SELECTOR, ".c-pager__link.c-pager__link--next")
                button_next.click()   

        return articles_section

    def scrap_news(self, from_days_ago: int) -> list[ScrapedNews]:
        """
        Call the methods to get the information from the America's CyberDefense Agency website.

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

        logger.info("Finish scrap to America's CyberDefense Agency.")
        return news_articles
