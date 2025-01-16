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
from selenium.common.exceptions import NoSuchElementException
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
    format_date = date_actual.strftime("%Y-%m-%d")  # Fomat: Year-Month-Day
    return format_date


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
    load_subpage(driver, '/html/body/div/div[2]/div[2]/main/div/div/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div[1]')
    #time.sleep(2)
    #driver.find_element(By.XPATH, "//div[@class='row']/div[@data-testid='organisation-results-container']/div[@data-testid='button-container']/button[@data-testid='load-more-button']")
    driver.find_element(By.XPATH, "//div[@data-testid='button-container']/button")
    
    '''
    # Bucle para cargar todos los artículos
    while True:
        try:
            # Intentar encontrar el botón "Cargar más artículos"     div.pcf-button button button--normalised button--secondary
            boton_cargar_mas = driver.find_element(By.XPATH, "//div[@class='pcf-button button button--normalised button--secondary']")
            boton_cargar_mas.click()  # Hacer clic en el botón
            time.sleep(3)  # Esperar unos segundos para que se carguen los nuevos artículos
        except NoSuchElementException:
            # Si no se encuentra el botón, asumimos que ya no hay más artículos por cargar
            print("No hay más artículos para cargar.")
            break
    '''
    articulos = driver.find_elements(By.CLASS_NAME, "/html/body/div/div[2]/div[2]/main/div/div/main/div/div/div/div[4]/div[4]/div[1]")
    time.sleep(9)
    #get_articles(driver)
    
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

def get_articles(driver):
    return None

try:      
    driver = configuration()                    
    driver.get(url_website)
    print(driver.title)
    
    load_cyber_pro = load_subpage(driver, '/html/body/div/div[2]/div[2]/main/div/div[3]/div/div/div[6]/div/div/div/div/div[6]/div')
    scrap_cyber_pro(driver)
    
except Exception as e:
    print("ERROR: ", e)
    
finally: #Siempre se ejecuta ocurra o no un error
    # Cierra el navegador
    driver.quit()