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

url_website = "https://www.ncsc.gov.uk/"

'''
url_cyber_pro = "https://www.ncsc.gov.uk/section/information-for/cyber-security-professionals"
url_ia = "https://www.ncsc.gov.uk/section/advice-guidance/all-topics?allTopics=true&topics=artificial%20intelligence&sort=date%2Bdesc"
url_cyber_stategy = "https://www.ncsc.gov.uk/section/advice-guidance/all-topics?allTopics=true&topics=cyber%20strategy&sort=date%2Bdesc"
url_cyptograpfy = "https://www.ncsc.gov.uk/section/advice-guidance/all-topics?allTopics=true&topics=cryptography&sort=date%2Bdesc"
'''

def get_actual_date():
    '''
    Returns
    -------
    Actual Date with fomat: Year-Month-Day
    '''
    date_actual = datetime.now()
    # Formatear la fecha (opcional)
    format_date = date_actual.strftime("%d %B %Y")  # Example: 23 June 2023
    return format_date

def disablaled_cookie_popup(driver, selector):
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

def configuration():
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
    
    opt.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.84 ")
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=opt
    )

    return driver

def load_subpage(driver, identificator):
    '''
    Parameters
    ----------
    driver : TYPE
        DESCRIPTION.
    identificator : String 
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    # Esperar hasta que el enlace de la subpágina esté visible y hacer clic en él
    subpage_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, identificator))  # Ajusta el XPATH según el enlace
    )
    subpage_link.click()
    
    # Esperar que la subpágina se cargue
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))  # Espera hasta que el contenido del cuerpo se cargue
    )

    return subpage_link

def scrap_cyber_pro(driver):
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
    load_subpage(driver, '//div[@data-testid="pcf-topics-panel"]/div[1]')
    #load_subpage(driver, '/html/body/div/div[2]/div[2]/main/div/div/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div[1]')
    time.sleep(1)
    #Siempre que no se de al boton de mas articulos, seran 20
    #show_art = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/main/div/div/main/div/div/div/div[4]/div[4]/div[2]').text.split()
    show_art = driver.find_element(By.XPATH, '//div[@data-testid="search__results__showing"]').text.split()
    num_articles_page = int(show_art[3])
    articles = []
    for i in range(0, num_articles_page):   # //div[@class="search-results"]/div[@class="pcf-search-result"]/a[@id="searchResult_{i}"]
        subpage_link = load_subpage(driver, f'//div[@class="pcf-search-result"]/a[@id="searchResult_{i}" and @class="reactLink"]')
        #driver.execute_script("arguments[0].scrollIntoView(true);", subpage_link)  # Asegurarse de que el elemento esté visible
        #time.sleep(0.5)  # Pausa breve para evitar problemas de sincronización
        articles.append(get_article(driver))
        time.sleep(1)
        driver.back() # Vuelve a la pagina anterior
    
    '''
    hacer mientras alla articulos, despues del artiuclo le puedo llegar a presionar el boton:
        load_subpage(driver, //div[@class='pcf-search-result' and @data-testid='pcf-search-result']/a[@id='searchResult_0'])
        articulos[i] = getarticle()
        i++
    '''
    
    ''' Example
    time.sleep(1)
    lista_ejemplo = driver.find_elements(By.XPATH, '//div[@data-testid="pcf-BodyText"]')
    #lista_ejemplo = driver.find_elements(By.XPATH, '/html/body/div/div[2]/div[2]/main/div/div/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div')
    for uni in lista_ejemplo:
        print(uni.text + "\n\n")
    '''

def get_article(driver):
    '''
    Parameters
    ----------
    driver : TYPE
        DESCRIPTION.

    Returns
    -------
    Article

    ''' 
    time.sleep(1)
    # NO USAR XPATH ABSOLUTOS NO FUNCIONAN EN TODOS LOS CASOS
    #date = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/main/div/div[1]/div[2]/aside/div[2]/div[1]/ul/li[1]/div/ul/li').text # Mirrar si haría falta
    title = driver.find_element(By.XPATH, '//div[@class="pcf-title"]').text
    summary = driver.find_elements(By.XPATH, '//div[@class="summary-content-container"]')[0].text

    #print(date + " " + get_actual_date())

    return {"title": title, "content": summary}

try:      
    driver = configuration()                    
    driver.get(url_website)
    print(driver.title)
    
    # Función para desactivar el popup de las cookies
    disablaled_cookie_popup(driver, '//div[@class="cookie-buttons"]/button[@data-testid="cookie-button-reject"]')

    load_cyber_pro = load_subpage(driver, '//div[@data-testid="pcf-guidance-for-panel"]/div[@class="row"]/div[6]')
    scrap_cyber_pro(driver)
    
except Exception as e:
    print("ERROR: ", e)
    
finally: #Siempre se ejecuta ocurra o no un error
    # Cierra el navegador
    driver.quit()