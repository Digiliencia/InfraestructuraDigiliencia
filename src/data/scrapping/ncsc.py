# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 10:08:33 2025

@author: Carlos Prieto 
Scrapping de la página web: https://www.ncsc.gov.uk/
"""

# Importing the necessary libraries
import sys
import os
# Add the parent directory (src) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time

#from utils.time import TimeUtils
#from utils.env_loader import EnvLoader
from utils.scrap import Scrap

#from utils import *

'''
https://www.ncsc.gov.uk/section/advice-guidance/glossary
https://www.ncsc.gov.uk/section/keep-up-to-date/ncsc-news?q=&defaultTypes=news,information&sort=date%2Bdesc
https://www.ncsc.gov.uk/section/keep-up-to-date/ncsc-blog
'''
class Ncsc:
    '''
    def _disablaled_cookie_popup(driver, selector):
        """
        Desactiva los popups de cookies en un sitio web.

        :param driver: Instancia del navegador de Selenium.
        :param selectors: Lista de selectores (XPath, CSS) que identifican los botones de aceptar o rechazar cookies.
        """
        try:
            # Espera a que el botón esté presente
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, selector))).click()
            print(f"Popup de cookies cerrado con selector: {selector}")
            return
        except Exception as e:
            print("ERROR close popup cookies: " + e)

    def _configuration():
        """
        Parameters
        ----------
        None

        Returns
        -------
        Driver

        """
        opt = Options()
        #opt.add_argument("--headless") #Ejecuta el script sin usar una interfaz gráfica
        #Las siguientes funciones se usan para mejorar el rendimiento del scrpit
        opt.add_argument("--disable-gpu") #Durante la ejecución desactiva la gráfica
        opt.add_argument("--disable-dev-shm-usage") #Durante la ejecución evita el uso compartido de memoria
        opt.add_argument("--no-sandbox") #Desactiva el modo sandbox del ordenador
        opt.add_argument("--disable-extensions") #Inicia el navegador sin ningun tipo de extensión
        
        opt.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.84 ")
        
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=opt
        )

        return driver

    def _load_subpage(driver, xpath):
        """
        Parameters
        ----------
        driver : TYPE
            DESCRIPTION.
        xpath : String 
            DESCRIPTION.

        Returns
        -------
        None.

        """
        # Esperar hasta que el enlace de la subpágina esté visible y hacer clic en él
        subpage_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))  # Ajusta el XPATH según el enlace
        )
        subpage_link.click()
        
        # Esperar que la subpágina se cargue
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))  # Espera hasta que el contenido del cuerpo se cargue
        )

        return subpage_link
    '''
    def _show_all_articles(driver):
        '''
        '''
        # Bucle para cargar todos los artículos
        while True:
            try:
                # Intentar encontrar el botón "Cargar más artículos"     div.pcf-button button button--normalised button--secondary
                button_load = driver.find_element(By.XPATH, '//div[@data-testid="organisation-results-container"]/div[3]')
                button_load.click()  # Hacer clic en el botón
                time.sleep(1)  # Esperar unos segundos para que se carguen los nuevos artículos
            except NoSuchElementException:
                # Si no se encuentra el botón, asumimos que ya no hay más artículos por cargar
                print("No hay más artículos para cargar.")
                break

    def _num_all_articles(driver):
        show_art = driver.find_element(By.XPATH, '//div[@data-testid="search__results__showing"]').text.split()
        return int(show_art[3])
    '''
    def _exist_xpath(driver, xpath):
        elementos = driver.find_elements(By.XPATH, xpath)
        return len(elementos) > 0
    '''
    #NO se usa
    def _is_error_not_found_topic(self, driver, num_topic):
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
        print(Scrap.exist_xpath(driver, '//div[@class="pcf-error" or @data-testid="pcf-error"]'))
        if(Scrap.exist_xpath(driver, '//div[@class="pcf-error" or @data-testid="pcf-error"]')):
            print("Anomalia detectada")
            driver.back()
            time.sleep(3)
            Scrap.load_subpage(driver, f'//div[@data-testid="all-topics-panel-row"]/div[{num_topic}]')

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
        
        time.sleep(1)
        num_topics = driver.find_element(By.XPATH, '//p[@data-testid="panel-subtitle"]').text.split()
        num_all_topics = int(num_topics[0])
        
        articles = []
        for i in range(1, num_all_topics):
            Scrap.load_subpage(driver, f'//div[@data-testid="all-topics-panel-row"]/div[{i}]')
            time.sleep(1)
            
            # Extraer temática
            print("Num tema: " + str(i) + "\n")
            
            self._is_error_not_found_topic(driver, i)  
            time.sleep(1)
            num_articles_page = self._num_all_articles(driver)
            time.sleep(1)
            self._show_all_articles(driver)
            for j in range(0, num_articles_page):   
                print("Num articulo: " + str(j))
                Scrap.load_subpage(driver, f'//div[@class="pcf-search-result"]/a[@id="searchResult_{j}" and @class="reactLink"]')
                time.sleep(0.75)
                self._is_error_not_found_topic(driver, j)  
                time.sleep(0.75)
                articles.append(self._get_article(driver))
                time.sleep(0.75)
                driver.back() # Vuelve a la pagina anterior
            driver.back()
        
        print("Total de articulos: ", len(articles))        

    def _get_topic(self, driver):
        '''
        Parameters
        ----------
        driver : TYPE
            DESCRIPTION.

        Returns
        -------
        Article
        '''
        time.sleep(0.5)

        if(Scrap.exist_xpath(driver, '//div[@data-testid="pcf-title"]')):
            title_topic = driver.find_element(By.XPATH, '//div[@data-testid="pcf-title"]').text
        else:
            title_topic = 'NONE'

        if(Scrap.exist_xpath(driver, '//div[@data-testid="summary"]')):
            description_topic = driver.find_elemnt(By.XPATH, '//div[@data-testid="summary"]').text
        else:
            description_topic = title_topic

        return {"title_topic": title_topic, "description": description_topic}

    def _get_article(self, driver):
        '''
        Parameters
        ----------
        driver : TYPE
            DESCRIPTION.

        Returns
        -------
        Article

        ''' 
        time.sleep(0.5) 
        
        if(Scrap.exist_xpath(driver, '//div[@data-testid="pcf-documentinformation"]/ul/li[1]/div/ul/li[@data-testid="sublist-item"]')):
            date = driver.find_element(By.XPATH, '//div[@data-testid="pcf-documentinformation"]/ul/li[1]/div/ul/li[@data-testid="sublist-item"]').text
        else:
            date = 'UNDATED'
        
        if(Scrap.exist_xpath(driver, '//div[@class="pcf-title"]')):
            title = driver.find_element(By.XPATH, '//div[@class="pcf-title"]').text
        else:
            title = 'NONE'
            
        if(Scrap.exist_xpath(driver, '//div[@class="summary-content-container"]')):
            summary = driver.find_elements(By.XPATH, '//div[@class="summary-content-container"]')[0].text
        else:
            summary = 'NONE'
        
        
        if(Scrap.exist_xpath(driver, '//div[@class="details"]/p[@class="details__name"]')):
            author = driver.find_element(By.XPATH, '//div[@class="details"]/p[@class="details__name"]').text
        else:
            author = 'Anonymous'


        if(Scrap.exist_xpath(driver, '//div[@data-testid="pcf-BodyText"]')):
            contents = driver.find_elements(By.XPATH, '//div[@data-testid="pcf-BodyText"]')
            content = ''
            for i in contents:
                content += i.text
        else:
            content = 'ERROR' # Una vez que esten todas las noticias extraidas eliminar las erroneas


        return {"title": title, "content": content, "summary": summary, "date": date, "author": author}

    def start_scrapping(self):
        try:      
            srap = Scrap()
            _url_website = "https://www.ncsc.gov.uk/section/advice-guidance/all-topics"
            #driver = self._configuration()    
            driver = srap.configuration()                
            driver.get(_url_website)
            print(driver.title)
            
            # Función para desactivar el popup de las cookies
            Scrap.disablaled_cookie_popup(driver, '//div[@class="cookie-buttons"]/button[@data-testid="cookie-button-reject"]')

            self._scrap_all_topics(driver)
            
        except Exception as e:
            print("ERROR: ", e)
            
        finally: #Siempre se ejecuta ocurra o no un error
            # Cierra el navegador
            driver.quit()


if __name__ == "__main__":
    ncsc = Ncsc()
    ncsc.start_scrapping()