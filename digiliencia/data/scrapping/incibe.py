# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 10:08:33 2025

@author: Esteban Peña Salazar
Web scrapping: https://www.incibe.es/
"""

import re
import time

# Importing the necessary libraries
from datetime import datetime

from loguru import logger
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.data.scrapping.abc_scraper import AbstractScraper
from digiliencia.utils.scrap import ScrapUtils
from digiliencia.utils.time import TimeUtils


class IncibeScraper(AbstractScraper):
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
            "avisos": {
                "title": ".field--name-title",
                "affected_resources": "article[data-history-node-id] div.node__content div.clearfix.text-formatted.field.field--name-field-recursos-afectados.field--type-text-with-summary.field--label-above .field__item",
                "description": "article[data-history-node-id] div.node__content div.clearfix.text-formatted.field.field--name-body.field--type-text-with-summary.field--label-above .field__item",
                "solution": "article[data-history-node-id] div.node__content div.clearfix.text-formatted.field.field--name-field-solucion.field--type-text-with-summary.field--label-above .field__item",
                "details": "article[data-history-node-id] div.node__content div.clearfix.text-formatted.field.field--name-field-detalle.field--type-text-with-summary.field--label-above .field__item",
                "date": ".node__content.field--type-text-with-summary .field__item",
            },
        }

    def get_urls_to_scrap(
        self,
        url,
        selector: str,
        days: int,
        get_urls_function: callable,  # type: ignore[valid-type]
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
            found_oldest, retrieved_urls = get_urls_function(  # type: ignore
                url_to_open, until_date, selector, i
            )
            total_size = len(urls)
            # If set union does not work, a for loop can be used to add the elements
            # for url in retrieved_urls:
            #     urls.add(url)
            urls.update(retrieved_urls)
            i += 1
            if len(urls) == total_size:
                break
        return urls

    def get_information_by_url(
        self, url: str, classes: dict[str, str]
    ) -> ScrapedNews:
        """
        Get the information from the URL title, content, date and author

        Args:

        url (str): The URL to get the information from
        classes (dict[str, str]): The classes to get the information from

        Returns:

        ScrapedNews: The information from the URL
        """

        logger.debug(f"Scraping URL {url}")
        self.driver.get(url)
        time.sleep(2)
        title = self.driver.find_element(By.CSS_SELECTOR, classes["title"]).text
        content = ""
        if classes.get("content"):
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
        affected_resources = None
        if classes.get("affected_resources"):
            affected_resources = self.driver.find_element(  # noqa: F841
                By.CSS_SELECTOR,
                classes["affected_resources"],
            ).text
        description = None
        if classes.get("description"):
            description = self.driver.find_element(  # noqa: F841
                By.CSS_SELECTOR,
                classes["description"],
            ).text
        solution = None
        if classes.get("solution"):
            solution = self.driver.find_element(  # noqa: F841
                By.CSS_SELECTOR,
                classes["solution"],
            ).text
        details = None
        if classes.get("details"):
            details = self.driver.find_element(  # noqa: F841
                By.CSS_SELECTOR,
                classes["details"],
            ).text
        date = date.split(" ")[-1]
        date = datetime.strptime(date, "%d/%m/%Y")

        return ScrapedNews(
            header=title,
            date=date,
            source="INCIBE",
            content=content,
            url=url,
            authors=[author],
            topics=None,
        )

    def open_incibe_blog(self, url_to_open_incibe, page_num: int = 0) -> None:
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
            logger.debug(f"Incibe blog page number {page_num} opened")
        except Exception:
            logger.warning(f"Error opening Incibe blog page number {page_num}")

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

    def get_warning_urls(
        self, url_to_open: str, date: str, posts_selector: str, page_num: int = 0
    ) -> tuple[bool, set[str]]:
        """
        Get the Incibe warning posts from the main page

        Args:

        url_to_open (str): The URL to open the Incibe warning page
        date (str): The date to get the warning posts
        posts_selector (str): The selector to get the warning posts
        page_num (int): The page number to open

        Returns:

        tuple[bool, set[str]]: A tuple with a boolean and a set of strings
        """
        found_oldest = False
        try:
            self.open_incibe_blog(url_to_open, page_num)
            # Wait for the page elements to load
            time.sleep(5)
            # Find all the elements in the list
            blog_posts = self.driver.find_elements(By.CSS_SELECTOR, posts_selector)
            # Extract the links from the elements
            blog_urls: set[str] = set()
            for post in blog_posts:
                published_on_elem = post.find_element(By.CLASS_NAME, "postedOnLabel")
                phrase = published_on_elem.text
                published_date = re.search(r"\d{2}/\d{2}/\d{4}", phrase).group()  # type: ignore
                if TimeUtils.days_between_es_dates(date, published_date) > 0:
                    link = post.find_element(
                        By.CSS_SELECTOR, ".node__links a"
                    ).get_attribute("href")
                    blog_urls.add(link)  # type: ignore
                else:
                    found_oldest = True
                    break

            return (found_oldest, blog_urls)
        except NoSuchElementException:
            logger.warning(f"Error getting Incibe blog posts {url_to_open}")
            return []  # type: ignore

    def get_blog_urls(
        self, url_to_open: str, date: str, posts_selector: str, page_num: int = 0
    ) -> tuple[bool, set[str]]:
        """
        Get the Incibe blog posts from the main page

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
            # Wait for the page elements to load
            time.sleep(5)
            # Find all the elements in the list
            blog_posts = self.driver.find_elements(By.CSS_SELECTOR, posts_selector)
            # Extract the links from the elements
            blog_urls: set[str] = set()
            for post in blog_posts:
                published_on_elem = post.find_element(By.CLASS_NAME, "postedOnLabel")
                phrase = published_on_elem.text
                published_date = re.search(r"\d{2}/\d{2}/\d{4}", phrase).group()  # type: ignore
                if TimeUtils.days_between_es_dates(date, published_date) > 0:
                    link = post.find_element(
                        By.CSS_SELECTOR, ".node__links a"
                    ).get_attribute("href")
                    blog_urls.add(link)  # type: ignore
                else:
                    found_oldest = True
                    break

            return (found_oldest, blog_urls)
        except NoSuchElementException:
            logger.warning(f"Error getting Incibe blog posts {url_to_open}")
            return []  # type: ignore

    def get_bitacora_urls(
        self, url_to_open: str, date: str, posts_selector: str, page_num: int = 0
    ) -> tuple[bool, set[str]]:
        """
        Get the Incibe bitacora posts from the main page

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
            # Wait for the page elements to load
            time.sleep(5)
            # Find all the elements in the list
            blog_posts = self.driver.find_elements(By.CSS_SELECTOR, posts_selector)
            # Extract the links from the elements
            blog_urls: set[str] = set()
            for post in blog_posts:
                published_on_elem = post.find_element(By.CLASS_NAME, "postedOnLabel")
                phrase = published_on_elem.text
                published_date = re.search(r"\d{2}/\d{2}/\d{4}", phrase).group()  # type: ignore

                is_newer = TimeUtils.days_between_es_dates(date, published_date) > 0
                all_newer |= is_newer

                if is_newer:
                    link = post.find_element(
                        By.CSS_SELECTOR, ".node__links a"
                    ).get_attribute("href")
                    blog_urls.add(link)  # type: ignore

            return (not all_newer, blog_urls)
        except NoSuchElementException:
            logger.warning(f"Error getting Incibe blog posts from {url_to_open}")
            return []  # type: ignore

    def scrap_news(self, from_days_ago: int) -> list[ScrapedNews]:
        """
        Call the methods to get the information from the Incibe page

        Args:

        from_days_ago (int): The number of days to get the information from

        Returns:

        tuple[dict[str, str]]: A tuple with a dictionary
        """

        self.driver.maximize_window()

        incibe_scrap = [
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
            {
                "url": "https://www.incibe.es/index.php/incibe-cert/alerta-temprana/avisos",
                "class": self.CLASSES["avisos"],
                "selector": "#views-bootstrap-at-avisos-page-1 > div > div",
                "scrap_function": self.get_warning_urls,
            },
        ]

        news_articles: list[ScrapedNews] = []

        for data in incibe_scrap:
            source_url = data["url"]
            class_name = data["class"]
            selector = data["selector"]
            scrap_function = data["scrap_function"]

            logger.debug(f"Getting URLs to scrap from {source_url}")

            urls_to_scrap = self.get_urls_to_scrap(
                source_url, selector, from_days_ago, scrap_function
            )

            logger.info(f"Found {len(urls_to_scrap)} URLs to scrap from {source_url}")

            # Iterate over the URLs to get the information
            for url in urls_to_scrap:
                try:
                    news_articles.append(self.get_information_by_url(url, class_name))
                except Exception as e:
                    logger.warning(f"Error al obtener la información de la URL: {e}")
            logger.info(
                f"Succesfully scraped {len(news_articles)} items from {source_url}"
            )

        self.driver.quit()  # Close the browser in a controlled manner
        return news_articles
