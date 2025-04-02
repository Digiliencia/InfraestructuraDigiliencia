# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 10:08:33 2025

@author: Carlos Prieto
Scrapping of website: https://www.ncsc.gov.uk/
"""

import time

from loguru import logger
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from digiliencia.data.scrapping.abc_scraper import AbstractScraper
from digiliencia.utils.env_loader import EnvLoader
from digiliencia.utils.scrap import ScrapUtils
from digiliencia.data.models.news_model import ScrapedNewsModel
from digiliencia.utils.time import TimeUtils
from digiliencia.data.scrapping.abc_scraper import AbstractScraper
from digiliencia.exc.ncsc_exec import NcscExec

class Ncsc(AbstractScraper):
    def __init__(self):
        logger.debug("Initializing Scrapping of NCSC")
        self.scrapUtils = ScrapUtils()
        self.load = EnvLoader()
        self.driver = ScrapUtils.get_driver()
        self.articles = []
        self.topics = []

    def _show_all_articles(self):
        """Shows the browser all articles in a topic. Click the "Show 10 more" button repeatedly until it disappears."""
        logger.debug("Show all articles of topic")
        # Loop to load all articles
        while True:
            try:
                # Try to find the "Load more items" button     
                button_load = self.driver.find_element(By.XPATH, '//button[@data-testid="load-more-button"]')
                button_load.click()  # Click the button
                time.sleep(self.load.webdriverwait_timeout - 0.5) # Wait a few seconds for new articles to load
            except NoSuchElementException:
                # If the button is not found, we assume that there are no more items to load.
                logger.debug("there are not articles to load.")
                break

    def _get_article_to_date(self, until_date: str = '') -> dict[str, str]:
        '''
        Return an articles of a topic until date param

        Args:
            until_date (str), default without param
        
        Return:
            An article of a topic
            An article is divide:
                date
                title
                summary
                author
                content
                url
        '''               
        try:
            if self.scrapUtils.if_element_exists(
                self.driver,
                By.XPATH,
                '//div[@data-testid="pcf-documentinformation"]/ul/li[1]/div/ul/li[@data-testid="sublist-item"]',
            ):
                date = self.driver.find_element(
                    By.XPATH,
                    '//div[@data-testid="pcf-documentinformation"]/ul/li[1]/div/ul/li[@data-testid="sublist-item"]',
                ).text
            else:
                date = self.articles[len(self.articles) - 1]["date"]

            if(TimeUtils.days_between_es_dates(until_date, date) > 0):
                title = self.driver.find_element(By.ID, 'title').text
                summary = self.driver.find_element(By.CLASS_NAME, 'pcf-summary').text
                contents = self.driver.find_elements(By.XPATH, '//div[@data-testid="pcf-BodyText"]')
                content = ''.join(i.text for i in contents)
                url = self.driver.current_url

                if self.scrapUtils.if_element_exists(
                    self.driver,
                    By.XPATH,
                    '//div[@class="details"]/p[@class="details__name"]',
                ):
                    author = self.driver.find_element(
                        By.XPATH, '//div[@class="details"]/p[@class="details__name"]'
                    ).text
                else:
                    author = (
                        "Guidance"  # Case there is a Guidance, there is not an author
                    )

                return {"title": title, "content": content, "summary": summary, "date": date, "author": author, "url": url}
            else:
                return {"flag": "false"}
    
        except NoSuchElementException as e:
            logger.error(f"ERROR NoSuchElementException {e}")

    def scrap_glosary(self):
        '''
        Scrap subpage glosary, link: https://www.ncsc.gov.uk/section/advice-guidance/glossary
        The definitions is divided by sections

        Return:
            A list with all definitions, each defitions have a:
                Concept,
                Description,
        '''
        concepts = []
        descriptions = []

        self.driver.get("https://www.ncsc.gov.uk/section/advice-guidance/glossary")
        self.scrapUtils.click_element(
            self.driver, "button.pcf-button:nth-child(2)", 1
        )  # Function to disable the cookie popup

        logger.info(f"Scrap of glosarry title: {self.driver.title}")

        definitions = self.driver.find_elements(
            By.CSS_SELECTOR, ".pcf-accordionItem.whiteBg"
        )
        logger.info(f"Num total of definitions: {len(definitions)}")
        for i in definitions:
            i.click()
            time.sleep(self.load.webdriverwait_timeout)
            concept = i.find_element(
                By.CSS_SELECTOR, "div.pcf-accordionItem.whiteBg h3"
            ).text
            logger.debug(f"Definition: {concept}")
            concepts.append(concept)
            description = i.find_element(By.CSS_SELECTOR, "div.pcf-BodyText p").text
            descriptions.append(description)

        return {"concepts": concepts, "descriptions": descriptions}

    def scrap_news(self, from_days_ago: int = 0) -> list[ScrapedNewsModel]:
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
            logger.info(f"Title {self.driver.title}")

            # Function to disable the cookie popup
            self.scrapUtils.click_element(
                self.driver, "button.pcf-button:nth-child(2)", 1
            )

            until_date = TimeUtils.format_subtract_days_to_actual_date(from_days_ago) # Calculate date to scrap

            self._show_all_articles()

            total_articles = self.driver.find_elements(By.CSS_SELECTOR, '.search-results div.pcf-search-result')
            for i in range(1, len(total_articles)+1): # +1 to pick up the last item
                logger.info(f"Num de article: {i}")
                # Aquí extramos la informacion de todos los articulos de la pagina
                self.driver.find_element(By.XPATH, f'(//div[@class="search-results"]/div)[{i}]').click() # Selecionamos cada articulo aquí
                time.sleep(self.load.webdriverwait_timeout)
                article = self._get_article_to_date(until_date)
                if(article.get("flag") == "false"):
                    break
                else:
                    self.articles.append(article)
                time.sleep(self.load.webdriverwait_timeout)
                self.driver.back()
          
        except NcscExec as e:
            logger.error(f"ERROR: {e}")
            
        self.driver.quit() # Close navegator
        
