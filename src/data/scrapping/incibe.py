# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 10:08:33 2025

@author: Esteban Peña Salazar
Web scrapping: https://www.incibe.es/
"""

# Importing the necessary libraries
from datetime import datetime
import re

# Add the parent directory (src) to the Python path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from utils.time import TimeUtils
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from utils.scrap import ScrapUtils
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

        self.CLASSES = {
            "cert": {
                "title": ".field--name-title",
                "content": "article[data-history-node-id] div.node__content div.clearfix.text-formatted.field.field--name-body.field--type-text-with-summary.field--label-hidden.field__item",
                "date": ".node__content.field--type-text-with-summary .field__item",
                "author": ".field.field--name-field-autor.field--type-entity-reference.field--label-above .field__item",
            },
            "bitacora": {
                "title": ".field--name-title",
                "content": "article[data-history-node-id] div.node__content div.clearfix.text-formatted.field.field--name-body.field--type-text-with-summary.field--label-hidden.field__item",
                "date": ".node__content.field--type-text-with-summary .field__item",
            },
        }

    def _if_element_exists(self, by: By, element: str) -> bool:
        """
        Check if an element exists on the web page.
        Args:
            by: The type of locator (e.g., By.ID, By.XPATH, etc.).
            element (str): The locator value of the element to find.
        Returns:
            bool: True if the element is found, False otherwise.
        """

        try:
            self.driver.find_element(by, element)
        except NoSuchElementException:
            return False
        return True

    def get_urls_to_scrap(self, url, selector: str, days: int, get_urls_function: callable) -> set[str]:
        until_date = TimeUtils.format_spanish_date(days)
        found_oldest = False
        url_to_open = url
        i = 0
        urls: set[str] = set()
        while not found_oldest:
            found_oldest, retrieved_urls = get_urls_function(
                url_to_open, until_date, selector, i
            )
            total_size = len(urls)
            # Si no funciona el set union, se puede hacer un for para añadir los elementos
            urls.update(retrieved_urls)
            i += 1
            if len(urls) == total_size:
                break
        return urls

    # Get the information from the URL (Verificar con Álvaro)
    def get_information_by_url(
        self, url: str, classes: dict[str, str]
    ) -> dict[str, str | datetime]:
        try:
            self.driver.get(url)
            time.sleep(2)
            title = self.driver.find_element(By.CSS_SELECTOR, classes["title"]).text
            content = self.driver.find_element(
                By.CSS_SELECTOR,
                classes["content"],
            ).text
            date = self.driver.find_element(
                By.CSS_SELECTOR,
                classes["date"],
            ).text
            author = None
            if classes.get("author"):
                author = self.driver.find_element(
                    By.CSS_SELECTOR,
                    classes["author"],
                ).text
            else:
                author = "INCIBE"

            date = date.split(" ")[-1]
            date = datetime.strptime(date, "%d/%m/%Y")
            return {"title": title, "content": content, "date": date, "author": author}
        except Exception as e:
            print(f"Error al obtener la información de la URL: {e}")
            return {}

    def open_incibe_blog(self, url_to_open_incibe, page_num: int = 0) -> None:
        try:
            self.driver.get(url_to_open_incibe + "?page=" + str(page_num))
            print("Incibe blog page opened")
        except Exception as e:
            print(f"Error opening Incibe blog page: {e}")

    def manage_cookies(self):
        ScrapUtils.click_element(
            self.driver,
            "#cookiesjsr > div > div > div:nth-of-type(2) > button:nth-of-type(2)",
        )
        """
        click the 'Ocultar' button in the cookie warning if it exists
        """
        ScrapUtils.click_element(
            self.driver,
            "#hide-banner-button",
        )

    def get_blog_urls(
        self, url_to_open: str, date: str, posts_selector: str, page_num: int = 0
    ) -> tuple[bool, set[str]]:
        """
        Get the Incibe blog posts
        """

        found_oldest = False
        try:
            self.open_incibe_blog(url_to_open, page_num)
            # Esperar a que se carguen los elementos de la página
            time.sleep(5)
            # Encontrar todos los elementos de la lista
            blog_posts = self.driver.find_elements(By.CSS_SELECTOR, posts_selector)
            # Extraer los enlaces de los elementos
            blog_urls: set[str] = set()
            for post in blog_posts:
                published_on_elem = post.find_element(By.CLASS_NAME, "postedOnLabel")
                phrase = published_on_elem.text
                published_date = re.search(r"\d{2}/\d{2}/\d{4}", phrase).group()
                if TimeUtils.days_between_es_dates(date, published_date) > 0:
                    link = post.find_element(
                        By.CSS_SELECTOR, ".node__links a"
                    ).get_attribute("href")
                    blog_urls.add(link)
                else:
                    found_oldest = True
                    break

            return (found_oldest, blog_urls)
        except NoSuchElementException as e:
            print(f"Error getting Incibe blog posts")
            return []
        
    def get_bitacora_urls(
        self, url_to_open: str, date: str, posts_selector: str, page_num: int = 0
    ) -> tuple[bool, set[str]]:
        """
        Get the Incibe blog posts
        """

        found_oldest = False
        try:
            self.open_incibe_blog(url_to_open, page_num)
            # Esperar a que se carguen los elementos de la página
            time.sleep(5)
            # Encontrar todos los elementos de la lista
            blog_posts = self.driver.find_elements(By.CSS_SELECTOR, posts_selector)
            # Extraer los enlaces de los elementos
            blog_urls: set[str] = set()
            for post in blog_posts:
                published_on_elem = post.find_element(By.CLASS_NAME, "postedOnLabel")
                
                phrase = published_on_elem.text
                published_date = re.search(r"\d{2}/\d{2}/\d{4}", phrase).group()
                if TimeUtils.days_between_es_dates(date, published_date) > 0:
                    link = post.find_element(
                        By.CSS_SELECTOR, ".node__links a"
                    ).get_attribute("href")
                    blog_urls.add(link)
                else:
                    found_oldest = True
                    break

            return (found_oldest, blog_urls)
        except NoSuchElementException as e:
            print(f"Error getting Incibe blog posts")
            return []



    # Main execution (verificar con Álvaro)
    def scrapper(self, from_days_ago: int) -> tuple[dict[str, str]]:
        self.driver.maximize_window()

        patata = [ # Convert to dict (JSON)
             (
                "https://www.incibe.es/incibe-cert/blog/",
                self.CLASSES["cert"],
                "#views-bootstrap-blog-listado-page-1 > div > div",
            ),
            (
                "https://www.incibe.es/incibe-cert/publicaciones/bitacora-ciberseguridad",
                self.CLASSES["bitacora"],
                "#views-bootstrap-noticias-listado-page-2 > div > div",
            ),
        ]

        for url, dict, id in patata:
            urls_to_scrap = self.get_urls_to_scrap(url, id, from_days_ago, self.get_blog_urls)

            # Recorrer las URLs para obtener la información
            for url in urls_to_scrap:
                print(f"Obteniendo información de la URL: {url}")
                info = self.get_information_by_url(url, dict)
                print(info)

        input("Presiona Enter para cerrar el navegador...")  # Mantén la página abierta
        self.driver.quit()  # Cierra el navegador de forma controlada
        return None
