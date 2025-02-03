# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 10:08:33 2025

@author: Esteban Peña Salazar
Web scrapping: https://www.incibe.es/
"""

# Importing the necessary libraries
import re
# Add the parent directory (src) to the Python path
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from utils.time import TimeUtils
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
import time




class IncibeScraper:
    def __init__(self):
        
        self.driver = WebDriver()
        options = Options()
        options.add_argument(
            "user-agent="
            + "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50"  # TODO to .env
        )
        options.add_argument("--disable-blink-features=AutomationControlled")
        prefs = {
            "profile.default_content_setting_values.geolocation": 2,
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "webrtc.ip_handling_policy": "disable_non_proxied_udp",
            "webrtc.multiple_routes_enabled": False,
            "webrtc.nonproxied_udp_enabled": False,
        }
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument("log-level=3")
        options.add_argument("--start-maximized")


    def get_urls_to_scrap(self, days:int=0)->list[str]:
        until_date = TimeUtils.format_spanish_date(days)
        self.getIncibeBlogUrls(0,until_date)

    def openIncibeBlog(self, page_num:int=0)->None:
        try:
            self.driver.get(f"https://www.incibe.es/incibe-cert/blog?page={page_num}")
            self.disable_cookie_popup()  # Cierra el popup de cookies
            self.hide_cookie_warning()    # Cierra el aviso de cookies
            print("Incibe blog page opened")
        except Exception as e:
            print(f"Error opening Incibe blog page: {e}")
    
    def disable_cookie_popup(self):
        """
        Cierra el popup de cookies si existe
        """
        try:
            # Esperar a que el botón de "Rechazar todas" sea clicable con el nuevo XPath
            wait = WebDriverWait(self.driver, 10)
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="cookiesjsr"]/div/div/div[2]/button[2]'))
            )
            cookie_button.click()
            print("Popup de cookies cerrado.")
        except Exception as e:
            print(f"No se encontró el popup de cookies o hubo un error: {e}")
    
    def hide_cookie_warning(self):
        """
        Clica el botón 'Ocultar' en el aviso de cookies si existe
        """
        try:
            # Esperar a que el botón de "Ocultar" sea clicable con su XPath
            wait = WebDriverWait(self.driver, 10)
            ocultar_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="hide-banner-button"]'))
            )
            ocultar_button.click()
            print("Aviso de cookies ocultado.")
        except Exception as e:
            print(f"No se encontró el botón de 'Ocultar' o hubo un error: {e}")

    

    def getIncibeBlogUrls(self, page_num:int, date:str)->list[str]:
        """
        Get the Incibe blog posts
        """
        try:
            self.openIncibeBlog(page_num)
            # Esperar a que se carguen los elementos de la página
            time.sleep(5)
            # Encontrar todos los elementos de la lista
            blog_posts = self.driver.find_elements(By.XPATH, '//*[@id="views-bootstrap-blog-listado-page-1"]/div/div')
            # Extraer los enlaces de los elementos
            blog_urls:list[str] = []
            for post in blog_posts:
                published_on_elem = post.find_element(By.CLASS_NAME, 'postedOnLabel')
                phrase = published_on_elem.text
                published_date = re.search(r'\d{2}/\d{2}/\d{4}', phrase).group()
                if TimeUtils.days_between_es_dates(date, published_date) > 0:
                    link = post.find_element(By.CSS_SELECTOR, '.node__links a').get_attribute('href')
                    blog_urls.append(link)
                else:
                    break
                
            return blog_urls
        except NoSuchElementException as e:
            print(f"Error al obtener los enlaces de los posts del blog: {e}")
            return []
        

    # Main execution
    def scrapper(self, from_days_ago:int)->tuple[dict[str, str]]:
        self.driver.maximize_window()
        self.get_urls_to_scrap(from_days_ago)
        input("Presiona Enter para cerrar el navegador...")  # Mantén la página abierta
        self.driver.quit()      # Cierra el navegador de forma controlada
        return None
#//*[@id="views-bootstrap-blog-listado-page-1"]/div/div[1]