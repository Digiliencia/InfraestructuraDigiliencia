# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 10:08:33 2025

@author: Carlos Prieto 
Scrapping of website: https://www.ncsc.gov.uk/
"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from loguru import logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from digiliencia.utils.env_loader import EnvLoader
from digiliencia.utils.scrap import ScrapUtils
from digiliencia.utils.time import TimeUtils

class Ncsc:
    
    def __init__(self):
        logger.debug("Initializing Scrapping of NCSC")
        self.scrapUtils = ScrapUtils()
        self.load = EnvLoader()
        self.driver = ScrapUtils.get_driver()
        self.articles = []
        self.topics = []

    def _show_all_articles(self):
        '''  Shows the browser all articles in a topic. Click the "Show 10 more" button repeatedly until it disappears.  '''
        logger.debug("Show all articles of topic")
        # Loop to load all articles
        while True:
            try:
                # Try to find the "Load more items" button     
                button_load = self.driver.find_element(By.XPATH, '//div[@data-testid="organisation-results-container"]/div[3]')
                button_load.click()  # Click the button
                time.sleep(self.load.webdriverwait_timeout) # Wait a few seconds for new articles to load
            except NoSuchElementException:
                # If the button is not found, we assume that there are no more items to load.
                print("No hay más artículos para cargar.")
                break

    def _get_num_all_articles(self) -> int:
        '''  Return number all articles of a topic. '''
        show_art = self.driver.find_element(By.XPATH, '//div[@data-testid="search__results__showing"]').text.split()
        logger.debug(f"Get number of all articles: {int(show_art[5])}")
        return int(show_art[5])

    def _scrap_all_topics_articles(self, days:int=0):
        '''
        Scrap all articles and topics of website: https://www.ncsc.gov.uk/

        Args:
            days(int) default = 0, days back to scrape 
        ''' 
        until_date = TimeUtils.format_subtract_days_to_actual_date(days) # Calculate date to scrap
        time.sleep(self.load.webdriverwait_timeout)
        num_topics = self.driver.find_elements(By.XPATH, '(//div[@data-testid="all-topics-panel-row"]/div)')
        logger.debug(f"Num de temas: {len(num_topics)}")

        for i in range(1, len(num_topics)+1): # +1 is for taking the last topic
            time.sleep(self.load.webdriverwait_timeout)
            self.driver.find_element(By.XPATH, f'//div[@data-testid="all-topics-panel-row"]/div[{i}]').click()
            
            # Extract Topic
            logger.debug(f"Num tema: {str(i)}")
            self.topics.append(self._get_topic())
 
            time.sleep(self.load.webdriverwait_timeout)
            num_articles_page = self._get_num_all_articles()
            time.sleep(self.load.webdriverwait_timeout)
            self._show_all_articles()
            
            logger.debug("Num de articulos por tema: " + str(num_articles_page))

            for j in range(0, num_articles_page):  
                logger.debug("Num articulo: " + str(j))

                page = WebDriverWait(self.driver, self.load.webdriverwait_timeout).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, f'//div[@class="pcf-search-result"]/a[@id="searchResult_{j}" and @class="reactLink"]')
                    )  # Adjust the XPATH according to the link
                )
                page.click()

                time.sleep(self.load.webdriverwait_timeout)
                article = self._get_article_to_date(until_date) 
                if(article == False):
                    break
                else:
                    self.articles.append(article)
                    time.sleep(self.load.webdriverwait_timeout)
                    self.driver.back() # Back to last page
            self.driver.back()
                
        logger.debug(f"Total articles: {len(self.articles)}")

    def _scrap_glosary(self) -> dict[str, str]:
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
        self.scrapUtils.click_element(self.driver, 'button.pcf-button:nth-child(2)', 1) # Function to disable the cookie popup

        logger.debug(f"Scrap of glosarry title: {self.driver.title}")

        definitions = self.driver.find_elements(By.CSS_SELECTOR, '.pcf-accordionItem.whiteBg')
        logger.debug(f"Num total de definiciones {len(definitions)}")
        for i in definitions:
            i.click()
            time.sleep(self.load.webdriverwait_timeout)
            concept = i.find_element(By.CSS_SELECTOR, 'div.pcf-accordionItem.whiteBg h3').text
            logger.debug(f"Definition: {concept}")
            concepts.append(concept)
            description = i.find_element(By.CSS_SELECTOR, 'div.pcf-BodyText p').text
            descriptions.append(description)
        
        return {"concepts": concepts, "descriptions": descriptions}

    def _get_article_to_date(self, until_date: str = '') -> dict[str, str]:
        '''
        Return an articles of a topic until date param

        Args:
            until_date (str)    
        
        Return:
            An article of a topic
            An article is divide:
                date
                title
                summary
                author
                content
        '''               
        try:
            if(self.scrapUtils._if_element_exists(self.driver, By.XPATH, '//div[@data-testid="pcf-documentinformation"]/ul/li[1]/div/ul/li[@data-testid="sublist-item"]')):
                date = self.driver.find_element(By.XPATH, '//div[@data-testid="pcf-documentinformation"]/ul/li[1]/div/ul/li[@data-testid="sublist-item"]').text
            else:
                date = self.articles[len(self.articles)-1]["date"]

            if(TimeUtils.compare_two_dates(until_date, date)):
                title = self.driver.find_element(By.XPATH, '//div[@class="pcf-title"]').text
                summary = self.driver.find_elements(By.XPATH, '//div[@class="summary-content-container"]')[0].text
                contents = self.driver.find_elements(By.XPATH, '//div[@data-testid="pcf-BodyText"]')
                content = ''.join(i.text for i in contents)

                if(self.scrapUtils._if_element_exists(self.driver, By.XPATH, '//div[@class="details"]/p[@class="details__name"]')):
                    author = self.driver.find_element(By.XPATH, '//div[@class="details"]/p[@class="details__name"]').text
                else:
                    author = "Guidance" # Case there is a Guidance, there is not an author

                return {"title": title, "content": content, "summary": summary, "date": date, "author": author}
            else:
                return False
    
        except NoSuchElementException as e:
            logger.error(f"ERROR NoSuchElementException {e}")

    def _get_topic(self) -> dict[str, str]:
        '''
        Return a topic of NCSC

        Return:
            A topic of NCSC
            A topic is divide:
                title
                description
        '''
        try:
            title_topic = self.driver.find_element(By.ID, 'title').text
            if(self.scrapUtils._if_element_exists(self.driver, By.CSS_SELECTOR, '.pcf-summary.main-summary p')):
                description_topic = self.driver.find_element(By.CSS_SELECTOR, '.pcf-summary.main-summary p').text
            else:
                if(self.scrapUtils._if_element_exists(self.driver, By.XPATH, '//div[@data-testid="summary"]')):
                    description_topic = self.driver.find_element(By.XPATH, '//div[@data-testid="summary"]').text
                else:
                    description_topic = ""

            return {"title_topic": title_topic, "description": description_topic}
        except NoSuchElementException as e:
            logger.error(f"ERROR NoSuchElementException {e}")

    def start_scrapping(self, days: int = 0): 
        """
        Inicialite scrapping of website: https://www.ncsc.gov.uk/

        Args:
            days(int) default = 0, days back to scrape 

        Example:
            >>> strat_scrapping(7)  # Run date in 20/03/2025, scrape all articles to 13/03/2025
            
        Return:
            3 dict
                all articles (dict)
                all topics (dict)
                glosary (dict)
        """
        try:    
            url_website_all_topics = "https://www.ncsc.gov.uk/section/advice-guidance/all-topics"
      
            self.driver.get(url_website_all_topics)   
            logger.debug(f"Title {self.driver.title}")
            
            # Function to disable the cookie popup
            self.scrapUtils.click_element(self.driver, 'button.pcf-button:nth-child(2)', 1)

            self._scrap_all_topics_articles(days)
            
            # scrap glosary
            glosary = self._scrap_glosary()

            return {self.articles, self.topics, glosary}

        except Exception as e:
            logger.error(f"ERROR: {e}")
            
        finally: # It always runs whether an error occurs or not. 
            self.driver.quit() # Close navegator