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

        self.driver = ScrapUtils.get_driver()

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

    def get_urls_to_scrap(
        self, url, selector: str, days: int, get_urls_function: callable
    ) -> set[str]:
        """
        Retrieves a set of URLs to scrape from the specified website.

        This function extracts URLs based on a given CSS selector and filters
        them according to the specified number of days.

        Args:
            url (str): The target URL to scrape.
            selector (str): The CSS selector used to identify URLs within the webpage.
            days (int): The time range (in days) to filter the extracted URLs.
            get_urls_function (callable): A function responsible for fetching and extracting URLs from the webpage.

        Returns:
            set[str]: A set of URLs to be scraped.

        Example:
            urls = get_urls_to_scrap(
                "https://example.com", ".article-links", 7, extract_urls
            )
        """

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
        # docstring
        """
        Get the information from the URL title, content, date and author

        Args:

        url (str): The URL to get the information from
        classes (dict[str, str]): The classes to get the information from

        Returns:

        dict[str, str | datetime]: The information from the URL
        """

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

        # docstring
        """
        Open the Incibe blog page

        Args:

        url_to_open_incibe (str): The URL to open the Incibe blog page
        page_num (int): The page number to open

        Returns:

        None
        """

        try:
            self.driver.get(url_to_open_incibe + "?page=" + str(page_num))
            print("Incibe blog page opened")
        except Exception as e:
            print(f"Error opening Incibe blog page: {e}")

    def manage_cookies(self):
        """
        Manage the cookies in the Incibe page

        Args:

        None

        Returns:

        None
        """
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
        # docstring
        """
        Get the Incibe blog posts

        Args:

        url_to_open (str): The URL to open the Incibe blog page
        date (str): The date to get the blog posts
        posts_selector (str): The selector to get the blog posts
        page_num (int): The page number to open

        Returns:

        tuple[bool, set[str]]: A tuple with a boolean and a set of strings
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
        Get the Incibe bitacora posts

        Args:

        url_to_open (str): The URL to open the Incibe bitacora page
        date (str): The date to get the bitacora posts
        posts_selector (str): The selector to get the bitacora posts
        page_num (int): The page number to open

        Returns:

        tuple[bool, set[str]]: The boolean indicates if every article is older than the date, and the set of strings containing articles published or updated after the given date.
        """

        all_newer = False

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

                is_newer = TimeUtils.days_between_es_dates(date, published_date) > 0
                all_newer |= is_newer

                if is_newer:
                    link = post.find_element(
                        By.CSS_SELECTOR, ".node__links a"
                    ).get_attribute("href")
                    blog_urls.add(link)

            return (not all_newer, blog_urls)
        except NoSuchElementException:
            print(f"Error getting Incibe blog posts")
            return []

    # Main execution (verificar con Álvaro)
    def scrapper(self, from_days_ago: int) -> tuple[dict[str, str]]:

        # docstring

        """
        Call the methods to get the information from the Incibe page

        Args:

        from_days_ago (int): The number of days to get the information from

        Returns:

        tuple[dict[str, str]]: A tuple with a dictionary
        """

        self.driver.maximize_window()

        incibe_scrap = [  # Convert to dict (JSON)
            {
                "url": "https://www.incibe.es/incibe-cert/blog/",
                "class": self.CLASSES["cert"],
                "selector": "#views-bootstrap-blog-listado-page-1 > div > div",
                "scrap_function": self.get_blog_urls,
            },
            {
                "url": "https://www.incibe.es/incibe-cert/publicaciones/bitacora-ciberseguridad",
                "class": self.CLASSES["bitacora"],
                "selector": "#views-bootstrap-noticias-listado-page-2 > div > div",
                "scrap_function": self.get_bitacora_urls,
            },
        ]

        for data in incibe_scrap:
            url = data["url"]
            class_name = data["class"]
            selector = data["selector"]
            scrap_function = data["scrap_function"]

            urls_to_scrap = self.get_urls_to_scrap(
                url, selector, from_days_ago, scrap_function
            )

            # Recorrer las URLs para obtener la información
            p = []
            for url in urls_to_scrap:
                p.append(self.get_information_by_url(url, class_name))
                # print(info)
            print(len(p))

        input("Presiona Enter para cerrar el navegador...")  # Mantén la página abierta
        self.driver.quit()  # Cierra el navegador de forma controlada
        return None
