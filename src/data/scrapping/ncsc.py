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

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from utils.env_loader import EnvLoader
from utils.scrap import Scrap

'''
https://www.ncsc.gov.uk/section/advice-guidance/glossary
https://www.ncsc.gov.uk/section/keep-up-to-date/ncsc-news?q=&defaultTypes=news,information&sort=date%2Bdesc
https://www.ncsc.gov.uk/section/keep-up-to-date/ncsc-blog
'''
class Ncsc:
    
    def __init__(self):
        self.scrap = Scrap()
        self.load = EnvLoader()

    def _show_all_articles(self, driver):
        '''
        '''
        # Bucle para cargar todos los artículos
        while True:
            try:
                # Intentar encontrar el botón "Cargar más artículos"     div.pcf-button button button--normalised button--secondary
                button_load = driver.find_element(By.XPATH, '//div[@data-testid="organisation-results-container"]/div[3]')
                button_load.click()  # Hacer clic en el botón
                time.sleep(self.load.webdriverwait_timeout) # Esperar unos segundos para que se carguen los nuevos artículos
            except NoSuchElementException:
                # Si no se encuentra el botón, asumimos que ya no hay más artículos por cargar
                print("No hay más artículos para cargar.")
                break

    def _num_all_articles(self, driver):
        show_art = driver.find_element(By.XPATH, '//div[@data-testid="search__results__showing"]').text.split()
        return int(show_art[3])

    #NO se usa
    def _is_error_not_found(self, driver, num_topic):
        '''
        The website have a bug. Sometimes, if you access a topic te puedes encontrar con la pagina de 404 y si sales y vuelves a seleccionar el mismo tema, te deja acceder al propio tema

        Parameters
        ----------
        driver : TYPE
            DESCRIPTION.

        Returns
        -------
        TRUE -> There is a page not found 404
        FALSE -> There is a topic
        ''' 
        # Error page not found, page back and go to page
        #print(self.scrap.exist_xpath(driver, '//div[@class="pcf-error" or @data-testid="pcf-error"]'))
        if(self.scrap.exist_xpath(driver, '//div[@class="pcf-error" or @data-testid="pcf-error"]')):
            print("Anomalia detectada")
            driver.back()
            time.sleep(self.load.webdriverwait_timeout)
            time.sleep(self.load.webdriverwait_timeout)
            self.scrap.load_subpage(driver, f'//div[@data-testid="all-topics-panel-row"]/div[{num_topic}]')

    def _scrap_all_topics(self, driver):
        '''
        Parameters
        ----------
        driver : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''  
        
        # //div[@data-testid="all-topics-panel-row"]/div[i]
        time.sleep(self.load.webdriverwait_timeout)
        num_topics = driver.find_element(By.XPATH, '//p[@data-testid="panel-subtitle"]').text.split()
        num_all_topics = int(num_topics[0])
        
        articles = []
        for i in range(1, num_all_topics):
            self.scrap.load_subpage(driver, f'//div[@data-testid="all-topics-panel-row"]/div[{i}]')
            time.sleep(self.load.webdriverwait_timeout)
            
            # Extraer temática
            print("Num tema: " + str(i) + "\n")
            
            self._is_error_not_found(driver, i)  
            time.sleep(self.load.webdriverwait_timeout)
            num_articles_page = self._num_all_articles(driver)
            time.sleep(self.load.webdriverwait_timeout)
            self._show_all_articles(driver)
            
            for j in range(0, num_articles_page):   
                print("Num articulo: " + str(j))
                self.scrap.load_subpage(driver, f'//div[@class="pcf-search-result"]/a[@id="searchResult_{j}" and @class="reactLink"]')
                time.sleep(self.load.webdriverwait_timeout)
                self._is_error_not_found(driver, j)  
                time.sleep(self.load.webdriverwait_timeout)
                articles.append(self._get_article(driver, j, articles))
                time.sleep(self.load.webdriverwait_timeout)
                driver.back() # Vuelve a la pagina anterior
            driver.back()
        
        print("Total de articulos: ", len(articles))        

    def _get_topic(self, driver) -> dict[str, str]:
        '''
        Parameters
        ----------
        driver : TYPE
            DESCRIPTION.

        Returns
        -------
        Article
        '''
        time.sleep(self.load.webdriverwait_timeout)

        if(self.scrap.exist_xpath(driver, '//div[@data-testid="pcf-title"]')):
            title_topic = driver.find_element(By.XPATH, '//div[@data-testid="pcf-title"]').text
        else:
            title_topic = 'NONE'

        if(self.scrap.exist_xpath(driver, '//div[@data-testid="summary"]')):
            description_topic = driver.find_elemnt(By.XPATH, '//div[@data-testid="summary"]').text
        else:
            description_topic = title_topic

        return {"title_topic": title_topic, "description": description_topic}

    def _get_article(self, driver, index: int = 0, articles=None) -> dict[str, str]:
        '''
        Parameters
        ----------
        driver : TYPE
            DESCRIPTION.

        Returns
        -------
        Article

        ''' 
        time.sleep(self.load.webdriverwait_timeout) 
        
        if(self.scrap.exist_xpath(driver, '//div[@data-testid="pcf-documentinformation"]/ul/li[1]/div/ul/li[@data-testid="sublist-item"]')):
            date = driver.find_element(By.XPATH, '//div[@data-testid="pcf-documentinformation"]/ul/li[1]/div/ul/li[@data-testid="sublist-item"]').text
        else:
            date = articles[index-1]["date"]
        
        if(self.scrap.exist_xpath(driver, '//div[@class="pcf-title"]')):
            title = driver.find_element(By.XPATH, '//div[@class="pcf-title"]').text
        else:
            title = 'NONE'
            
        if(self.scrap.exist_xpath(driver, '//div[@class="summary-content-container"]')):
            summary = driver.find_elements(By.XPATH, '//div[@class="summary-content-container"]')[0].text
        else:
            summary = 'NONE'
        
        
        if(self.scrap.exist_xpath(driver, '//div[@class="details"]/p[@class="details__name"]')):
            author = driver.find_element(By.XPATH, '//div[@class="details"]/p[@class="details__name"]').text
        else:
            author = 'Anonymous'


        if(self.scrap.exist_xpath(driver, '//div[@data-testid="pcf-BodyText"]')):
            contents = driver.find_elements(By.XPATH, '//div[@data-testid="pcf-BodyText"]')
            content = ''
            for i in contents:
                content += i.text
        else:
            content = 'ERROR' # Una vez que esten todas las noticias extraidas eliminar las erroneas

        return {"title": title, "content": content, "summary": summary, "date": date, "author": author}

    def start_scrapping(self):
        try:    
            url_website_all_topics = "https://www.ncsc.gov.uk/section/advice-guidance/all-topics"
 
            driver = self.scrap.configuration()      
            driver.get(url_website_all_topics)   
            print(driver.title)
            
            # Función para desactivar el popup de las cookies
            self.scrap.disablaled_cookie_popup(driver, '//div[@class="cookie-buttons"]/button[@data-testid="cookie-button-reject"]')

            self._scrap_all_topics(driver)
            
        except Exception as e:
            print("ERROR: ", e)
            
        finally: #Siempre se ejecuta ocurra o no un error
            # Cierra el navegador
            driver.quit()

# DEVELOP
if __name__ == "__main__":
    ncsc = Ncsc()
    ncsc.start_scrapping()