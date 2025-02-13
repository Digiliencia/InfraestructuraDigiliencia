# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 10:08:33 2025

@author: Carlos Prieto 
Scrapping of website: https://www.ncsc.gov.uk/
"""

'''DEVELOP'''

# Importing the necessary libraries
import sys
import os
# Add the parent directory (src) to the Python path 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
''''''

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.env_loader import EnvLoader
from utils.scrap import ScrapUtils
from utils.time import TimeUtils

'''
https://www.ncsc.gov.uk/section/advice-guidance/glossary
https://www.ncsc.gov.uk/section/keep-up-to-date/ncsc-news?q=&defaultTypes=news,information&sort=date%2Bdesc
https://www.ncsc.gov.uk/section/keep-up-to-date/ncsc-blog
'''
class Ncsc:
    
    def __init__(self):
        self.scrap = ScrapUtils()
        self.load = EnvLoader()

    def _show_all_articles(self, driver):
        '''
        Shows the browser all articles in a topic. Click the "Show 10 more" button repeatedly until it disappears.

        Args:
            driver: Selenium browser instance.
        Raise:
            TypeError: not found drive
        Return:
            None
        '''
        if(driver is None):
            raise TypeError("ERROR: drive not found")
        # Loop to load all articles
        while True:
            try:
                # Try to find the "Load more items" button     
                button_load = driver.find_element(By.XPATH, '//div[@data-testid="organisation-results-container"]/div[3]')
                button_load.click()  # Click the button
                time.sleep(self.load.webdriverwait_timeout) # Wait a few seconds for new articles to load
            except NoSuchElementException:
                # If the button is not found, we assume that there are no more items to load.
                print("No hay más artículos para cargar.")
                break

    def _get_num_all_articles(self, driver) -> int:
        '''
        Return number all articles of a topic
        
        Args:
            driver: Selenium browser instance.
        Raise:
            TypeError: not found drive
        Return:
            number all articles of a topic
        '''
        if(driver is None):
            raise TypeError("ERROR: drive not found")
        
        show_art = driver.find_element(By.XPATH, '//div[@data-testid="search__results__showing"]').text.split()
        return int(show_art[5])

    def _is_error_not_found(self, driver, num_topic: int = 1):
        '''
        The website has a bug. Sometimes, if you access a topic you can find the 404 page and if you exit and select the same topic again, it lets you access the same topic.

        Args:
            driver: Selenium browser instance.
            num_topic: topic number of the topics to be scraped
        Raise:
            TypeError: Not found drive
        Return:
            TRUE -> There is a page not found 404
            FALSE -> There is a topic
        ''' 
        if(driver is None):
            raise TypeError("ERROR: drive not found")
        # Error page not found, page back and go to page
        if(self.scrap.if_element_exists(driver, By.XPATH, '//div[@class="pcf-error" or @data-testid="pcf-error"]')):
            print("Anomalia detectada")
            driver.back()
            time.sleep(self.load.webdriverwait_timeout)
            driver.find_element(By.XPATH, f'//div[@data-testid="all-topics-panel-row"]/div[{num_topic}]').click()

    def _scrap_all_topics_articles(self, driver)-> dict[str, str]:
        '''
        main function of website scraping https://www.ncsc.gov.uk/

        Raise:
            TypeError: Not found driver
        Args:
            driver: Selenium browser instance.
        Return:
            all topics and all articles on topics
        '''  
        if(driver is None):
            raise TypeError("ERROR: drive not found")

        time.sleep(self.load.webdriverwait_timeout)
        num_topics = driver.find_element(By.XPATH, '//p[@data-testid="panel-subtitle"]').text.split()
        num_all_topics = int(num_topics[0])
        
        topics = []
        articles = []
        num_art = 0
        for i in range(1, (num_all_topics+1)):
            driver.find_element(By.XPATH, f'//div[@data-testid="all-topics-panel-row"]/div[{i}]').click()

            time.sleep(self.load.webdriverwait_timeout)
            
            # Extract Topic
            print("Num tema: " + str(i))
            topics.append(self._get_topic(driver))

            self._is_error_not_found(driver, i)  
            time.sleep(self.load.webdriverwait_timeout)
            num_articles_page = self._get_num_all_articles(driver)
            time.sleep(self.load.webdriverwait_timeout)
            self._show_all_articles(driver)
            
            print("Num de articulos por tema: " + str(num_articles_page))
            for j in range(0, num_articles_page):  
                print("Num articulo: " + str(j))

                page = WebDriverWait(driver, self.load.webdriverwait_timeout).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, f'//div[@class="pcf-search-result"]/a[@id="searchResult_{j}" and @class="reactLink"]')
                    )  # Adjust the XPATH according to the link
                )
                page.click()

                time.sleep(self.load.webdriverwait_timeout)
                articles.append(self._get_article(driver, num_art, articles))
                num_art += 1 
                time.sleep(self.load.webdriverwait_timeout)
                driver.back() # Back to last page
            driver.back()
        
        print("Total de articulos: ", len(articles))        

        return {topics, articles}


    def _scrap_all_topics_articles_to_days(self, driver, days:int=0)-> dict[str, str]:
        '''
        main function of website scraping https://www.ncsc.gov.uk/

        Raise:
            TypeError: Not found driver
        Args:
            driver: Selenium browser instance.
            days: days from today's date to extract data
        Return:
            all topics and all articles on topics
        '''  
        if(driver is None):
            raise TypeError("ERROR: drive not found")

        until_date = TimeUtils.format_subtract_days_to_actual_date(days)

        time.sleep(self.load.webdriverwait_timeout)
        num_topics = driver.find_element(By.XPATH, '//p[@data-testid="panel-subtitle"]').text.split()
        num_all_topics = int(num_topics[0])
        
        topics = []
        articles = []
        num_art = 0
        for i in range(1, (num_all_topics+1)):
            driver.find_element(By.XPATH, f'//div[@data-testid="all-topics-panel-row"]/div[{i}]').click()
            time.sleep(self.load.webdriverwait_timeout)
            
            # Extract Topic
            print("Num tema: " + str(i))
            topics.append(self._get_topic(driver))

            self._is_error_not_found(driver, i)  
            time.sleep(self.load.webdriverwait_timeout)
            num_articles_page = self._get_num_all_articles(driver)
            time.sleep(self.load.webdriverwait_timeout)
            self._show_all_articles(driver)
            
            print("Num de articulos por tema: " + str(num_articles_page))
            for j in range(0, num_articles_page):  
                print("Num articulo: " + str(j))
                driver.find_element(By.XPATH, f'//div[@class="pcf-search-result"]/a[@id="searchResult_{j}" and @class="reactLink"]').click() 
                time.sleep(self.load.webdriverwait_timeout)
                article = self._get_article_to_date(driver, num_art, articles, until_date)
                if(article == False):
                    break
                else:
                    articles.append(article)
                    num_art += 1 
                    time.sleep(self.load.webdriverwait_timeout)
                    driver.back() # Back to last page
            driver.back()
        
        print("Total de articulos: ", len(articles))        

        return {topics, articles}


    def _scrap_glosary(self, driver) -> dict[str, str]:
        '''
        Scrap subpage glosary, link: https://www.ncsc.gov.uk/section/advice-guidance/glossary
        The definitions is divided by sections

        Args:
            driver: Selenium browser instance.
        Return:
            A list with all definitions, each defitions have a:
                Concept,
                Description,
        '''
        time.sleep(self.load.webdriverwait_timeout)

        concepts = []
        descriptions = []

        if(self.scrap.if_element_exists(driver, By.XPATH, '//li[@id="2"]/a')): # ¿Are there button glosary?
            driver.find_element(By.XPATH, '//li[@id="2"]/a').click() # Click button Glosary
            time.sleep(self.load.webdriverwait_timeout)

            definitions = driver.find_elements(By.XPATH, f'//div[@class="pcf-accordionItem whiteBg"]')
            for i in definitions:
                i.click()
                time.sleep(self.load.webdriverwait_timeout)
                concept = i.find_element(By.CSS_SELECTOR, 'div.pcf-accordionItem.whiteBg h3').text
                concepts.append(concept)
                description = i.find_element(By.CSS_SELECTOR, 'div.pcf-BodyText p').text
                descriptions.append(description)

        else:
            print("There are not a button glosary")    
        
        return {"concepts": concepts, "descriptions": descriptions}

    def _get_article_to_date(self, driver, index: int = 0, articles: dict = [], until_date: str = '') -> dict[str, str]:
        '''
        Return an article of a topic until date param

        Args:
            driver: Selenium browser instance.
            index: counter of array articles
            articles: array of all articles
            until_date: 
        Return:
            An article of a topic
            An article is divide:
                date
                title
                summary
                author
                content
        ''' 
        if(driver is None):
            raise("ERROR: drive not found")

        time.sleep(self.load.webdriverwait_timeout) 
        
        if(self.scrap.if_element_exists(driver, By.XPATH, '//div[@data-testid="pcf-documentinformation"]/ul/li[1]/div/ul/li[@data-testid="sublist-item"]')):
            date = driver.find_element(By.XPATH, '//div[@data-testid="pcf-documentinformation"]/ul/li[1]/div/ul/li[@data-testid="sublist-item"]').text
        else:
            date = articles[index-1]["date"]

        if(until_date < date):  
            if(self.scrap.if_element_exists(driver, By.XPATH, '//div[@class="pcf-title"]')):
                title = driver.find_element(By.XPATH, '//div[@class="pcf-title"]').text
            else:
                title = 'NONE'
                
            if(self.scrap.if_element_exists(driver, By.XPATH, '//div[@class="summary-content-container"]')):
                summary = driver.find_elements(By.XPATH, '//div[@class="summary-content-container"]')[0].text
            else:
                summary = 'NONE'
                
            if(self.scrap.if_element_exists(driver, By.XPATH, '//div[@class="details"]/p[@class="details__name"]')):
                author = driver.find_element(By.XPATH, '//div[@class="details"]/p[@class="details__name"]').text
            else:
                author = 'Anonymous'

            if(self.scrap.if_element_exists(driver, By.XPATH, '//div[@data-testid="pcf-BodyText"]')):
                contents = driver.find_elements(By.XPATH, '//div[@data-testid="pcf-BodyText"]')
                content = ''
                for i in contents:
                    content += i.text
            else:
                content = 'ERROR' 
        else:
            return False

        return {"title": title, "content": content, "summary": summary, "date": date, "author": author}

    def _get_topic(self, driver) -> dict[str, str]:
        '''
        Return a topic of NCSC

        Args:       
            driver: Selenium browser instance.
        Raise:
            TypeError: Not found driver
        Return:
            A topic of NCSC
            A topic is divide:
                title
                description
        '''
        if(driver is None):
            raise TypeError("ERROR: drive not found")
        
        time.sleep(self.load.webdriverwait_timeout)

        if(self.scrap.if_element_exists(driver, By.XPATH, '//div[@data-testid="pcf-title"]')):
            title_topic = driver.find_element(By.XPATH, '//div[@data-testid="pcf-title"]').text
        else:
            title_topic = 'NONE'

        if(self.scrap.if_element_exists(driver, By.XPATH, '//div[@data-testid="summary"]')):
            description_topic = driver.find_element(By.XPATH, '//div[@data-testid="summary"]').text
        else:
            description_topic = title_topic

        return {"title_topic": title_topic, "description": description_topic}

    def _get_article(self, driver, index: int = 0, articles: dict = []) -> dict[str, str]:
        '''
        Return an article of a topic

        Args:
            driver: Selenium browser instance.
            index: counter of array articles
            articles: array of all articles
        Return:
            An article of a topic
            An article is divide:
                date
                title
                summary
                author
                content
        ''' 
        if(driver is None):
            raise("ERROR: drive not found")

        time.sleep(self.load.webdriverwait_timeout) 
        
        if(self.scrap.if_element_exists(driver, By.XPATH, '//div[@data-testid="pcf-documentinformation"]/ul/li[1]/div/ul/li[@data-testid="sublist-item"]')):
            date = driver.find_element(By.XPATH, '//div[@data-testid="pcf-documentinformation"]/ul/li[1]/div/ul/li[@data-testid="sublist-item"]').text
        else:
            date = articles[index-1]["date"]
        
        if(self.scrap.if_element_exists(driver, By.XPATH, '//div[@class="pcf-title"]')):
            title = driver.find_element(By.XPATH, '//div[@class="pcf-title"]').text
        else:
            title = 'NONE'
            
        if(self.scrap.if_element_exists(driver, By.XPATH, '//div[@class="summary-content-container"]')):
            summary = driver.find_elements(By.XPATH, '//div[@class="summary-content-container"]')[0].text
        else:
            summary = 'NONE'
               
        if(self.scrap.if_element_exists(driver, By.XPATH, '//div[@class="details"]/p[@class="details__name"]')):
            author = driver.find_element(By.XPATH, '//div[@class="details"]/p[@class="details__name"]').text
        else:
            author = 'Anonymous'

        if(self.scrap.if_element_exists(driver, By.XPATH, '//div[@data-testid="pcf-BodyText"]')):
            contents = driver.find_elements(By.XPATH, '//div[@data-testid="pcf-BodyText"]')
            content = ''
            for i in contents:
                content += i.text
        else:
            content = 'ERROR' 

        return {"title": title, "content": content, "summary": summary, "date": date, "author": author}

    def start_scrapping(self): 
        """
        Inicialite scrapping of website: https://www.ncsc.gov.uk/

        Args:
            None
        Return:
            None
        """
        try:    
            url_website_all_topics = "https://www.ncsc.gov.uk/section/advice-guidance/all-topics"
 
            driver = self.scrap.get_driver()      
            driver.get(url_website_all_topics)   
            print(driver.title)
            
            # Function to disable the cookie popup
            self.scrap.click_element(driver, 'button.pcf-button:nth-child(2)', 1)

            #self._scrap_all_topics_articles(driver)
            
            # scrap glosary
            self._scrap_glosary(driver)

        except Exception as e:
            print("ERROR: ", e)
            
        finally: # It always runs whether an error occurs or not.
            # Close navegator
            driver.quit()

''''''
# DEVELOP
if __name__ == "__main__":
    ncsc = Ncsc()
    ncsc.start_scrapping()
''''''