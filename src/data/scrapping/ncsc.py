# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 10:08:33 2025

@author: Carlos Prieto 
Intento de Scrapping de la página web: https://www.ncsc.gov.uk/
"""

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

__url_website__ = "https://www.ncsc.gov.uk/"

'''
url_cyber_pro = "https://www.ncsc.gov.uk/section/information-for/cyber-security-professionals"
url_ia = "https://www.ncsc.gov.uk/section/advice-guidance/all-topics?allTopics=true&topics=artificial%20intelligence&sort=date%2Bdesc"
url_cyber_stategy = "https://www.ncsc.gov.uk/section/advice-guidance/all-topics?allTopics=true&topics=cyber%20strategy&sort=date%2Bdesc"
url_cyptograpfy = "https://www.ncsc.gov.uk/section/advice-guidance/all-topics?allTopics=true&topics=cryptography&sort=date%2Bdesc"
'''

def __get_actual_date__():
    '''
    Returns
    -------
    Actual Date with fomat: Year-Month-Day
    '''
    date_actual = datetime.now()
    # Formatear la fecha (opcional)
    format_date = date_actual.strftime("%d %B %Y")  # Example: 23 June 2023
    return format_date

def __disablaled_cookie_popup__(driver, selector):
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

def __configuration__():
    '''
    Parameters
    ----------
    None

    Returns
    -------
    Driver

    '''
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

def __load_subpage__(driver, xpath):
    '''
    Parameters
    ----------
    driver : TYPE
        DESCRIPTION.
    xpath : String 
        DESCRIPTION.

    Returns
    -------
    None.

    '''
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

def __show_all_articles__(driver):
    '''
    '''
    # Bucle para cargar todos los artículos
    while True:
        try:
            # Intentar encontrar el botón "Cargar más artículos"     div.pcf-button button button--normalised button--secondary
            boton_cargar_mas = driver.find_element(By.XPATH, '//div[@data-testid="organisation-results-container"]/div[3]')
            boton_cargar_mas.click()  # Hacer clic en el botón
            time.sleep(1)  # Esperar unos segundos para que se carguen los nuevos artículos
        except NoSuchElementException:
            # Si no se encuentra el botón, asumimos que ya no hay más artículos por cargar
            print("No hay más artículos para cargar.")
            break

def __num_all_articles__(driver):
    show_art = driver.find_element(By.XPATH, '//div[@data-testid="search__results__showing"]').text.split()
    return int(show_art[3])

def __scrap_cyber_pro__(driver):
    '''
    Parameters
    ----------
    driver : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''    
    # Risk Management
    __load_subpage__(driver, '//div[@data-testid="pcf-topics-panel"]/div[1]')
    time.sleep(1)
    __show_all_articles__(driver)
    time.sleep(1)
    num_articles_page = __num_all_articles__(driver)
    articles = []
    for i in range(0, num_articles_page):   
        __load_subpage__(driver, f'//div[@class="pcf-search-result"]/a[@id="searchResult_{i}" and @class="reactLink"]')
        articles.append(__get_article__(driver))
        time.sleep(0.25)
        driver.back() # Vuelve a la pagina anterior

def __get_article__(driver):
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
    date = driver.find_element(By.XPATH, '//div[@data-testid="pcf-documentinformation"]/ul/li[1]/div/ul/li[@data-testid="sublist-item"]').text
    title = driver.find_element(By.XPATH, '//div[@class="pcf-title"]').text
    summary = driver.find_elements(By.XPATH, '//div[@class="summary-content-container"]')[0].text
    
    if(__exist_xpath__(driver, '//div[@class="details"]/p[@class="details__name"]')):
        author = driver.find_element(By.XPATH, '//div[@class="details"]/p[@class="details__name"]').text
    else:
        author = 'Anonymous'

    contents = driver.find_elements(By.XPATH, '//div[@data-testid="pcf-BodyText"]')
    content = ''
    for i in contents:
        content += i.text

    return {"title": summary, "content": content, "date": date, "author": author}


def __exist_xpath__(driver, xpath):
    try:
        driver.find_element(By.XPATH, xpath)
        return True
    except NoSuchElementException:
        return False

def start_scrapping():
    try:      
        driver = __configuration__()                    
        driver.get(__url_website__)
        print(driver.title)
        
        # Función para desactivar el popup de las cookies
        __disablaled_cookie_popup__(driver, '//div[@class="cookie-buttons"]/button[@data-testid="cookie-button-reject"]')

        load_cyber_pro = __load_subpage__(driver, '//div[@data-testid="pcf-guidance-for-panel"]/div[@class="row"]/div[6]')
        __scrap_cyber_pro__(driver)
        
    except Exception as e:
        print("ERROR: ", e)
        
    finally: #Siempre se ejecuta ocurra o no un error
        # Cierra el navegador
        driver.quit()

#DEVELOP
start_scrapping()