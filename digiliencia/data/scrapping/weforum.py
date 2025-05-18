# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 12:39:40 2025

@author: Álvaro Prieto Álvarez
Scrapper for the World Economic Forum website. It allows to scrape the articles from the Cybersecurity topic.
"""

import random
import time
from datetime import datetime
from typing import Callable, Optional
from urllib.parse import parse_qs, urlparse

from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from digiliencia.configs.env import Env
from digiliencia.data.models.news_model import ScrapedNewsModel
from digiliencia.data.scrapping.abc_scraper import AbstractScraper
from digiliencia.exc.WEForum_exc import WEForumError
from digiliencia.utils.scrap import ScrapUtils
from digiliencia.utils.time import TimeUtils


class WEForumScraper(AbstractScraper):
    """Scraps the World Economic Forum website for articles on the Cybersecurity topic."""

    def __init__(self):
        logger.debug("Initializing WEForumScrapper")
        _env = Env()  # Call EnvLoader to force reading the .env file
        self.driver = ScrapUtils.get_driver()

        self.weforum_email = _env.weforum_email
        self.weforum_passwd = _env.weforum_passwd
        self.timeout = _env.webdriverwait_timeout
        self.cybersecturity_topic_url = (
            "https://intelligence.weforum.org/topics/a1Gb00000015LbsEAE"
        )
        self.home_page = "https://www.weforum.org/"
        self.stories_url = "https://www.weforum.org/stories"
        self.login_page = "https://login.weforum.org/"
        self.load_time = 2
        self.MAX_SCROLL_RELOADS = 5

    def _login(self):
        """Log in to the World Economic Forum website using the credentials provided in the .env file

        Raises:
            TimeoutError: If the login button is not found after 5 seconds
        """

        # Accept cookies if pop-up visible
        logger.debug("Loging in to WEForum")
        if ScrapUtils.if_element_exists(self.driver, By.ID, "CybotCookiebotDialog"):  # type: ignore
            cookies_popup = self.driver.find_element(By.ID, "CybotCookiebotDialog")
            if cookies_popup.is_displayed():
                accept_bttn = self.driver.find_element(
                    By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"
                )
                accept_bttn.click()

        # Open new tab to login
        self.driver.execute_script(f"window.open('{self.login_page}');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((By.ID, "loginradius-login-emailid"))
        )

        # Introduce email
        email_input = self.driver.find_element(By.ID, "loginradius-login-emailid")
        email_input.send_keys(self.weforum_email)
        time.sleep(1)
        next_btn = self.driver.find_element(By.ID, "login-check-email")
        next_btn.click()

        # Wait until the log-in button is visible or timeout after 5 seconds
        submit_btn = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((By.ID, "loginradius-submit-login"))
        )
        if submit_btn is None:
            raise TimeoutError("Login button not found")

        # Introduce password
        time.sleep(self.load_time)
        passwd_input = self.driver.find_element(By.ID, "loginradius-login-password")
        passwd_input.send_keys(self.weforum_passwd)
        time.sleep(1)
        submit_btn.click()

        # Wait for about 10 seconds
        time.sleep(13)

        # Close the login tab
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.refresh()
        time.sleep(
            self.load_time * 5
        )  # As there are probably more than one redirection, wait a bit more
        time.sleep(self.load_time)

    def _get_websites_to_scrap(self, max_age_date: int = 7) -> list[dict[str, str]]:
        """
        Obtiene los sitios web a escrapear que sean más recientes que max_age_date días.
        
        Args:
            max_age_date: Número máximo de días de antigüedad para los artículos
            
        Returns:
            Lista de diccionarios con información de los artículos válidos
        
        Raises:
            ValueError: Si max_age_date es menor que 1
        """
        logger.info(f"Getting articles from {max_age_date} days ago")
        
        if max_age_date < 1:
            logger.error("max_age_date debe ser mayor que 0")
            raise ValueError("max_age_date debe ser mayor que 0")

        age_words = TimeUtils.format_days_ago(max_age_date)
        processed_articles = []
        processed_urls = set()  # Para evitar artículos duplicados
        
        # Configuración inicial
        aside_div = self.driver.find_element(
            By.CLASS_NAME, "TopicDetailPanel__StyledContainer-sc-9d1f1b4c-0"
        )
        self.driver.execute_script("arguments[0].scrollTo(0, 500);", aside_div)
        time.sleep(self.load_time)

        # Cambiar a artículos recientes
        self.driver.find_element(By.CSS_SELECTOR, "label[for='knowledge-toggle-latest']").click()
        time.sleep(self.load_time)

        latest_articles_div = self.driver.find_element(
            By.CSS_SELECTOR, "div[data-test-id='latest-knowledge-feed']"
        )

        found_old_article = False
        no_new_articles_count = 0
        last_articles_count = 0
        
        logger.debug("Starting articles scanning")
        
        while not found_old_article:
            # Obtener todos los artículos actualmente visibles
            current_articles = latest_articles_div.find_elements(
                By.CLASS_NAME, "ListItemBox-sc-47508d61-0"
            )
            
            # Solo procesar los nuevos artículos (los que aún no hemos visto)
            new_articles_count = len(current_articles) - last_articles_count
            
            if new_articles_count > 0:
                logger.debug(f"Processing {new_articles_count} new articles")
                no_new_articles_count = 0  # Reiniciar contador de intentos
                
                # Procesar solo los nuevos artículos
                for article in current_articles[last_articles_count:]:
                    try:
                        # Verificar la edad del artículo
                        age_element = article.find_element(
                            By.CLASS_NAME, "SourceLabel__StyledDate-sc-b4751e57-4"
                        )
                        age = age_element.text
                        
                        # Verificar si es demasiado antiguo
                        if "hour" not in age and TimeUtils.days_between_dates(age, age_words) > 0:
                            title = article.find_element(
                                By.CLASS_NAME, "shared__StyledTitle-sc-fd9f989e-1"
                            ).text
                            logger.info(f"Too old article found: '{title}' from {age}")
                            found_old_article = True
                            break
                        
                        # Procesar el artículo al vuelo
                        type_element = article.find_element(
                            By.CLASS_NAME, "shared__StyledType-sc-fd9f989e-0"
                        )
                        article_type = type_element.text.lower()

                        if article_type == "publication":
                            publisher = article.find_element(
                                By.CLASS_NAME, "SourceLabel__StyledText-sc-b4751e57-2"
                            ).text
                            title = article.find_element(
                                By.CLASS_NAME, "shared__StyledTitle-sc-fd9f989e-1"
                            ).text
                            link_element = article.find_element(
                                By.CLASS_NAME, "UIActionButton__StyledButton-sc-d03545d8-2"
                            )
                            title_attr = link_element.get_attribute("title")
                            href = link_element.get_attribute("href")
                            
                            if title_attr == "Open" and href and href not in processed_urls:
                                processed_urls.add(href)  # Evitar duplicados
                                processed_articles.append({
                                    "type": article_type,
                                    "publisher": publisher,
                                    "title": title,
                                    "url": href,
                                })
                        elif article_type == "video":
                            logger.debug("Ignoring article type 'video'")
                            continue
                        else:
                            logger.warning(f"Unknown article type: {article_type}")
                    except Exception as e:
                        logger.warning(f"Error processing article: {str(e)}")
                
                # Actualizar el contador de artículos vistos
                last_articles_count = len(current_articles)
            else:
                no_new_articles_count += 1
                logger.debug(f"No new articles found. Retrying ({no_new_articles_count}/{self.MAX_SCROLL_RELOADS})")
                
                # Reiniciar el scroll si no se encuentran nuevos artículos después de varios intentos
                if no_new_articles_count >= self.MAX_SCROLL_RELOADS:
                    logger.warning("Max retries reached. Stopping articles discovery.")
                    break
                
                # Scroll hacia arriba para refrescar y luego hacia abajo para cargar nuevos
                if no_new_articles_count % 2 == 0:
                    self.driver.execute_script("arguments[0].scrollTo(0, 0);", aside_div)
                
            
            # Scroll hacia abajo para cargar más artículos si es necesario
            if not found_old_article:
                self.driver.execute_script(
                    "arguments[0].scrollTo(0, arguments[0].scrollHeight);", aside_div
                )
                # Tiempo de espera aleatorio para simular comportamiento humano
                wait_time = random.uniform(self.load_time, self.load_time + 1)
                time.sleep(wait_time)
        
        logger.info(f"Articles discovery ended. Found {len(processed_articles)} articles.")
        return processed_articles

    def _close(self):
        """
        Closes the current browser window.

        This method will close the browser window that is currently controlled by the driver instance.
        """
        logger.debug("Closing the browser window")
        self.driver.close()

    def _is_logged_in(self) -> bool:
        """Being in the topic page, checks if the user is logged in.

        Returns:
            bool: True if the user is logged in, False otherwise.

        Raises:
            WEForumError: If the user is not in the topic page
        """
        if self.driver.current_url != self.cybersecturity_topic_url:
            logger.error(
                "Cannot check if logged in because browser is not in the topic page"
            )
            raise WEForumError(
                "Cannot check if logged in because browser is not in the topic page"
            )

        # If the user logo (id: mf_user-icon) exists, user is loged in
        return ScrapUtils.if_element_exists(self.driver, By.ID, "mf_user-icon")  # type: ignore

    def _accept_cookies_if_visible(self, accept_bttn_id: str):
        """Accepts the cookies if the pop-up is visible.

        Args:
            accept_bttn_id (str): The ID of the accept button.
        """
        logger.debug("Accepting cookies if visible")
        if ScrapUtils.if_element_exists(self.driver, By.ID, accept_bttn_id):  # type: ignore
            accept_bttn = self.driver.find_element(By.ID, accept_bttn_id)
            if accept_bttn.is_displayed():
                accept_bttn.click()
                time.sleep(self.load_time)

    def _scrap_rand_corporation(self, url: str) -> ScrapedNewsModel:
        """
        Access the given URL and scrapes Rand Corporation

        Args:
            url (str): Rand Corporation url article

        Raises:
            WEForumError: If the URL is not a valid Rand Corporation article URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Return:
            ScrapedNewsModel: An object with the publication information.
        """
        # Verify URL
        if "https://www.rand.org/pubs/research_reports/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Rand Corporation newsletter scrapper"
            )

        logger.debug(f"Scraping Rand Corporation story: {url}")
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)

        title = self.driver.find_element(By.ID, "RANDTitleHeadingId").text
        authors = self.driver.find_element(By.CLASS_NAME, "authors").text
        date = self.driver.find_element(
            By.CLASS_NAME, "published"
        ).text  # Mirar el formato de la fecha
        date = date[9:]

        introduction = self.driver.find_element(
            By.CLASS_NAME, "abstract-first-letter"
        ).text
        sections = self.driver.find_elements(By.TAG_NAME, "li").text  # type: ignore
        content = introduction + sections

        return ScrapedNewsModel(
            header=title,
            date=datetime.strptime(date, "%B %d, %Y"),
            source="Rand Corporation",
            content=content,
            url=url,
            authors=[authors],
            topics=None,
        )

    def _scrap_sciencedaily(self, url: str) -> ScrapedNewsModel:
        """
        Access the given URL and scrapes Science Daily

        Args:
            url (str): Science Daily url article

        Raises:
            WEForumError: If the URL is not a valid Science Daily article URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Return:
            ScrapedNewsModel: An object with the publication information.
        """
        # Verify URL
        if "https://www.sciencedaily.com/releases/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Science Daily newsletter scrapper"
            )

        logger.debug(f"Scraping Science Daily story: {url}")
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)

        title = self.driver.find_element(By.ID, "headline").text
        content = self.driver.find_element(By.ID, "text").text
        date = self.driver.find_element(
            By.ID, "date_posted"
        ).text  # Mirar el formato de la fecha
        authors = self.driver.find_element(By.ID, "source").text

        return ScrapedNewsModel(
            header=title,
            date=datetime.strptime(date, "%B %d, %Y"),
            source="Science Daily",
            content=content,
            url=url,
            authors=[authors],
            topics=None,
        )

    def _scrap_wired_story(self, url: str) -> ScrapedNewsModel:
        """Access the given URL and scrapes the publication.

        Args:
            url (str): Wired story URL

        Raises:
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNewsModel: an object with the publication information.
        """
        logger.debug(f"Scraping Wired story: {url}")
        # Disable JS
        ScrapUtils.disable_js(self.driver)

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)

        self._accept_cookies_if_visible("onetrust-accept-btn-handler")

        time_element = self.driver.find_element(By.TAG_NAME, "time")
        date_str = time_element.text
        date = datetime.strptime(
            date_str, "%b %d, %Y %I:%M %p"
        )  # TODO: take into account case like "Updated a month ago": https://www.wired.com/live/tiktok-scotus-live-coverage/

        author_element = self.driver.find_element(
            By.CSS_SELECTOR, '[data-testid="BylineName"]'
        )
        author = author_element.text

        title_element = self.driver.find_element(
            By.CSS_SELECTOR, 'h1[data-testid="ContentHeaderHed"]'
        )
        title = title_element.text

        content_elements = self.driver.find_elements(
            By.CSS_SELECTOR, "div.body__inner-container > p"
        )
        content = ""
        for element in content_elements:
            content += element.text + "\n"

        content = content
        ScrapUtils.enable_js(self.driver)  # Enable JS again
        return ScrapedNewsModel(
            header=title,
            date=date,
            source="Wired",
            content=content,
            url=url,
            authors=[author],
            topics=None,
        )

    def _scrap_WEF_story_publication(self, url: str) -> ScrapedNewsModel:
        """Access the given URL and scrapes the publication.

        Args:
            url (str): World Economic Forum publication URL

        Raises:
            WEForumError: If the URL is not a valid WEForum stories URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page

        Returns:
            ScrapedNewsModel with the publication information.
        """
        logger.debug(f"Scraping WEForum story: {url}")
        if self.stories_url not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for WEForum stories scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)

        # Get the title
        title_element = self.driver.find_element(By.TAG_NAME, "h1")
        header = title_element.text

        # Get the date
        time_element = self.driver.find_element(By.TAG_NAME, "time")
        date = datetime.fromisoformat(time_element.get_attribute("datetime"))  # type: ignore

        # Get the author
        author_div = self.driver.find_element(By.CSS_SELECTOR, "div.wef-1upaxcp")
        author = author_div.find_element(
            By.TAG_NAME, "a"
        ).text  # TODO: assess whether it is worthwhile to get the author's profile link and scrape it to.
        # TODO: fix if more than one person wrote the article (list?)

        # Get the content
        content_container = self.driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/section/div/div/article/div[2]/div[2]/div[2]",
        )

        content = (
            content_container.text
        )  # TODO: althoug this may contain the content, it may not be the best way to extract it, as it can also contain other elements like links, images, etc.
        return ScrapedNewsModel(
            header=header,
            date=date,
            source="World Economic Forum",
            content=content,
            url=url,
            authors=[author],
            topics=None,
        )

    def _scrap_globaldata_newsletter(self, url: str) -> ScrapedNewsModel:
        """Access the given URL and scrapes the publication.

        Args:
            url (str): GlobalData newsletter details URL

        Raises:
            WEForumError: If the URL is not a valid GlobalData newsletter details URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNewsModel: an object with the publication information.
        """
        logger.debug(f"Scraping GlobalData newsletter: {url}")
        # Verify URL
        if "https://www.globaldata.com/newsletter/details" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for GlobalData newsletter scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)

        # Extract date from URL parameter if available
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        newsletter_date = query_params.get("newsletterdate", [None])[0]
        if newsletter_date:
            date = datetime.strptime(newsletter_date, "%Y-%m-%d")
        else:
            raise WEForumError(
                "newsletter date not found in URL. Cannot set publication date."
            )

        title_element = self.driver.find_element(By.CSS_SELECTOR, "h2>a")
        title = title_element.text

        content_container = title_element.find_element(By.XPATH, "./../../..")
        content = content_container.text
        content = content.replace(title, "")  # Remove title from content

        return ScrapedNewsModel(
            header=title,
            date=date,
            source="GlobalData",
            content=content,
            url=url,
            authors=[],
            topics=None,
        )

    def _scrap_the_quantum_insider(self, url: str) -> ScrapedNewsModel:
        """Access the given URL and scrapes the post.

        Args:
            url (str): The Quantum Insider URL

        Raises:
            WEForumError: If the URL is not a valid The Quantum Insider URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNewsModel: an object with the publication information.
        """
        logger.debug(f"Scraping The Quantum Insider: {url}")
        if not url.startswith("https://thequantuminsider.com/"):
            raise WEForumError(
                "Attempted to scrape invalid page for The Quantum Insider scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time+1)

        # Disable JS
        ScrapUtils.disable_js(self.driver)

        # Get the title
        title = self.driver.find_element(By.CSS_SELECTOR, "h1[class='elementor-heading-title elementor-size-default']").text

        # Get the date
        date_element = self.driver.find_element(By.CSS_SELECTOR, "span time")
        date = datetime.strptime(date_element.text, "%B %d, %Y")

        # Get the author
        author = self.driver.find_element(
            By.CLASS_NAME, "elementor-post-info__item--type-author"
        ).text

        # Get the content
        content_container = self.driver.find_element(
            By.CSS_SELECTOR, "#cst-p-css .elementor-widget-container"
        )
        content = ""
        elements = content_container.find_elements(By.XPATH, "./*")
        for element in elements:
            tag = element.tag_name
            if tag == "p":
                content += element.text + "\n\n"
            elif tag == "h3":
                content += f"\n\n{element.text}\n"
            elif tag == "ul":
                for li in element.find_elements(By.TAG_NAME, "li"):
                    content += f"* {li.text}\n"
            elif tag == "ol":
                for i, li in enumerate(element.find_elements(By.TAG_NAME, "li"), 1):
                    content += f"{i}. {li.text}\n"
            elif tag == "img":
                img_link = element.get_attribute("src")
                img_alt = element.get_attribute("alt")
                content += f"![{img_alt}]({img_link})\n"

        content = content

        ScrapUtils.enable_js(self.driver)  # Enable JS again

        return ScrapedNewsModel(
            header=title,
            date=date,
            source="The Quantum Insider",
            content=content,
            url=url,
            authors=[author],
            topics=None,
        )

    def _scrap_australian_strategic_policy_institute(
        self, url: str
    ) -> ScrapedNewsModel:
        """Access the given URL and scrapes the publication.

        Args:
            url (str): Australian Strategic Policy Institute URL

        Raises:
            WEForumError: If the URL is not a valid Australian Strategic Policy Institute URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNewsModel: an object with the publication information.
        """
        logger.debug(f"Scraping Australian Strategic Policy Institute: {url}")
        if "https://www.aspistrategist.org.au/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Australian Strategic Policy Institute scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)

        # Get the title
        title = self.driver.find_element(By.CLASS_NAME, "entry-title").text

        # Get the date
        date_elem = self.driver.find_element(
            By.CSS_SELECTOR, "article > header > .meta"
        )
        date = datetime.fromisoformat(date_elem.get_attribute("datetime"))  # type: ignore

        # Get the author
        author_elems = self.driver.find_elements(
            By.CSS_SELECTOR, "article > header > .meta > .author"
        )
        authors = [author_elem.text for author_elem in author_elems]

        # Get the content
        content_div = self.driver.find_element(By.CLASS_NAME, "entry-content")
        content = ""
        for element in content_div.find_elements(By.XPATH, "./*"):
            tag = element.tag_name
            if tag == "p":
                content += element.text + "\n\n"
            elif tag == "h3":
                content += f"{element.text}\n"
            elif tag == "ul":
                for li in element.find_elements(By.TAG_NAME, "li"):
                    content += f"* {li.text}\n"
            elif tag == "ol":
                for i, li in enumerate(element.find_elements(By.TAG_NAME, "li"), 1):
                    content += f"{i}. {li.text}\n"
            elif tag == "img":
                img_link = element.get_attribute("src")
                img_alt = element.get_attribute("alt")
                content += f"![{img_alt}]({img_link})\n"

        content = content
        return ScrapedNewsModel(
            header=title,
            date=date,
            source="Australian Strategic Policy Institute",
            content=content,
            url=url,
            authors=authors,
            topics=None,
        )

    def _scrap_propbublica_article(self, url: str) -> ScrapedNewsModel:
        """Access the given URL and scrapes the publication.

        Args:
            url (str): ProPublica article URL

        Raises:
            WEForumError: If the URL is not a valid ProPublica article URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNewsModel: an object with the publication information.
        """
        logger.debug(f"Scraping ProPublica article: {url}")
        if "https://www.propublica.org/article/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for ProPublica article scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time * 1.5)

        # Get the title
        title = self.driver.find_element(By.TAG_NAME, "h1").text

        # Get the date
        time_elems = self.driver.find_elements(By.TAG_NAME, "time")
        for elm in time_elems:
            if elm.get_attribute("datetime"):
                time_elem = elm
                break
        time_data = time_elem.get_attribute("datetime")  # type: ignore
        date = datetime.strptime(time_data, "%Y-%m-%dEST%H:%M")  # type: ignore

        # Get the author
        authors_elem = self.driver.find_element(
            By.XPATH, '//*[@id="main"]/article/div[2]/div/[1]span[1]'
        )
        authors = []
        for elem in authors_elem.find_elements(By.XPATH, ".//p"):
            if elem.tag_name in ["span", "a"]:
                authors.append(elem.text)

        # Get the content
        content_div = self.driver.find_element(By.CLASS_NAME, "article-body")
        content = ""
        for p in content_div.find_elements(By.TAG_NAME, "p"):
            content += p.text + "\n\n"

        return ScrapedNewsModel(
            header=title,
            date=date,
            source="ProPublica",
            content=content,
            url=url,
            authors=authors,
            topics=None,
        )

    def _scrap_the_conversation(self, url: str) -> ScrapedNewsModel:
        """
        Access the given URL and scrapes the publication.

        Args:
            url (str): The Conversation article URL

        Raises:
            WEForumError: If the URL is not a valid The Conversation URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNewsModel: an object with the publication information.
        """
        logger.debug(f"Scraping The Conversation article: {url}")
        if "https://theconversation.com/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for The Conversation article scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)

        # Deny cookies if visible
        ScrapUtils.click_element(self.driver, ".didomi-continue-without-agreeing", 1)

        title = self.driver.find_element(By.CSS_SELECTOR, "h1").text

        authors_section = self.driver.find_element(By.CLASS_NAME, "content-authors")
        authors_list = authors_section.find_elements(By.TAG_NAME, "li")
        authors = [
            author.find_element(By.CLASS_NAME, "author-name").text
            for author in authors_list
        ]

        time_elem = self.driver.find_element(By.CSS_SELECTOR, ".timestamps time")
        date = datetime.fromisoformat(time_elem.get_attribute("datetime"))  # type: ignore

        content_elem = self.driver.find_element(By.CLASS_NAME, "entry-content")
        content = ""
        for element in content_elem.find_elements(By.XPATH, "./*"):
            if (
                element.tag_name == "h1"
                or element.tag_name == "h2"
                or element.tag_name == "h3"
            ):
                content += f"\n\n{element.text}\n"
            elif element.tag_name == "p":
                prev_sibling = element.find_elements(
                    By.XPATH, "preceding-sibling::*[1]"
                )
                next_sibling = element.find_elements(
                    By.XPATH, "following-sibling::*[1]"
                )
                if prev_sibling and next_sibling:
                    prev_sibling = prev_sibling[0]
                    next_sibling = next_sibling[0]
                    if prev_sibling.tag_name == "hr" and next_sibling.tag_name == "hr":
                        continue
                content += element.text + "\n\n"

        return ScrapedNewsModel(
            header=title,
            date=date,
            source="The Conversation",
            content=content,
            url=url,
            authors=authors,
            topics=None,
        )

    def _scrap_the_atlantic(self, url: str) -> ScrapedNewsModel:
        """
        Access the given URL and scrapes The Atlantic.

        Args:
            url (str): The Atlantic article URL

        Raises:
            WEForumError: If the URL is not a valid The Atlantic URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNewsModel: an object with the publication information.
        """
        logger.debug(f"Scraping The Atlantic article: {url}")
        if "https://www.theatlantic.com" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for The Atlantic article scrapper"
            )

        # Disable JS
        ScrapUtils.disable_js(self.driver)

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)

        title = self.driver.find_element(By.CSS_SELECTOR, "h1").text

        authors_line = self.driver.find_element(By.ID, "byline")
        authors = [
            author.text for author in authors_line.find_elements(By.TAG_NAME, "a")
        ]

        time_elem = self.driver.find_element(By.TAG_NAME, "time")
        date = datetime.fromisoformat(time_elem.get_attribute("datetime"))  # type: ignore

        content_elem = self.driver.find_element(
            By.CLASS_NAME, "ArticleBody_root__2gF81"
        )
        content = ""
        for element in content_elem.find_elements(By.XPATH, "./*"):
            if (
                element.tag_name == "p"
                and element.get_attribute("data-view-action") is not None
            ):
                continue
            else:
                content += element.text + "\n\n"

        ScrapUtils.enable_js(self.driver)  # Enable JS again

        return ScrapedNewsModel(
            header=title,
            date=date,
            source="The Atlantic",
            content=content,
            url=url,
            authors=authors,
            topics=None,
        )

    def _scrap_springeropen(self, url: str) -> ScrapedNewsModel:
        """
        Access the given URL and scrapes SpringerOpen.

        Args:
            url (str): SpringerOpen article URL

        Raises:
            WEForumError: If the URL is not a valid SpringerOpen article URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNewsModel: an object with the publication information.
        """
        logger.debug(f"Scraping SpringerOpen article: {url}")
        if "springeropen.com/articles" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for SpringerOpen article scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)

        ScrapUtils.click_element(
            self.driver, "[data-cc-action=reject]"
        )  # Reject cookies if visible

        title = self.driver.find_element(By.CSS_SELECTOR, "h1").text

        authors = [
            author.text
            for author in self.driver.find_elements(
                By.CSS_SELECTOR, "[data-author-search]"
            )
        ]

        time_elem = self.driver.find_element(By.TAG_NAME, "time")
        date = datetime.fromisoformat(time_elem.get_attribute("datetime"))  # type: ignore

        content_elem = self.driver.find_element(By.CSS_SELECTOR, "main > article")
        content = content_elem.text  # TODO: improve content extraction

        return ScrapedNewsModel(
            header=title,
            date=date,
            source="SpringerOpen",
            content=content,
            url=url,
            authors=authors,
            topics=None,
        )

    def _scrap_electronic_frontier_foundation_deeplink(
        self, url: str
    ) -> ScrapedNewsModel:
        """
        Access the given URL and scrapes Electronic Frontier Foundation deeplink.

        Args:
            url (str): Electronic Frontier Foundation deeplink URL

        Raises:
            WEForumError: If the URL is not a valid Electronic Frontier Foundation deeplink URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNewsModel: an object with the publication information.
        """
        logger.debug(f"Scraping Electronic Frontier Foundation deeplink: {url}")
        if "https://www.eff.org/deeplinks/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Electronic Frontier Foundation deeplink scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(By.CSS_SELECTOR, "h1").text

        authors_line = self.driver.find_element(By.CLASS_NAME, "byline")
        authors = [
            author.text for author in authors_line.find_elements(By.TAG_NAME, "a")
        ]

        time_elem = self.driver.find_element(By.CLASS_NAME, "date")
        date = datetime.strptime(time_elem.text, "%B %d, %Y")  # type: ignore

        article = self.driver.find_element(By.CSS_SELECTOR, 'article[role="article"]')
        content_container = article.find_element(
            By.CSS_SELECTOR, "div.field--name-body"
        )
        content = content_container.text

        return ScrapedNewsModel(
            header=title,
            date=date,
            source="Electronic Frontier Foundation",
            content=content,
            url=url,
            authors=authors,
            topics=None,
        )

    def _scrap_australian_institute_international_affairs(
        self, url: str
    ) -> ScrapedNewsModel:
        """
        Access the given URL and scrapes Australian Institute Of International Affairs page.

        Args:
            url (str): Australian Institute Of International Affairs URL

        Raises:
            WEForumError: If the URL is not a valid Australian Institute Of International Affairs URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNewsModel: an object with the publication information.
        """
        logger.debug(f"Scraping Australian Institute Of International Affairs: {url}")
        if "https://www.internationalaffairs.org.au/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Australian Institute Of International Affairs scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(By.CLASS_NAME, "post-title").text

        authors_line = self.driver.find_element(By.CLASS_NAME, "author-name").text
        authors_line = authors_line.replace("By ", "")
        authors = [
            author.strip() for author in authors_line.replace(" and ", ", ").split(",")
        ]
        author = ", ".join(authors)

        time_elem = self.driver.find_element(By.CLASS_NAME, "publish-date")
        date = datetime.strptime(time_elem.text, "%d %b %Y")  # type: ignore

        content_container = self.driver.find_elements(By.CSS_SELECTOR, "div.body-content p")
        content = [
            contents.text for contents in content_container
        ]
        content = ''.join(content)

        return ScrapedNewsModel(
            header=title,
            date=date,
            source="Australian Institute Of International Affairs",
            content=content,
            url=url,
            authors=[author],
            topics=None,
        )

    ''''''

    def _scrap_eco_bussiness(
        self, url: str
    ) -> ScrapedNewsModel:
        '''
        Access the given URL and scrapes Eco-bussiness.

        Args:
            url (str): Eco-bussiness URL

        Raises:
            WEForumError: If the URL is not a valid Eco-bussiness URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNewsModel: an object with the publication information.
        '''
        logger.debug(f"Eco-bussiness: {url}")
        if "https://www.eco-business.com" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Eco-bussiness scrapper"
            )
        
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(By.ID, "ebStoryHeadline").text

        author_line = self.driver.find_element(By.CLASS_NAME, "eb-article__byline__author").text
        author_line = author_line.replace("By", "")
        authors = author_line.rsplit(",", 1)
        author = authors[0].strip()

        time_elem = self.driver.find_element(By.CSS_SELECTOR, "time.eb-article__byline__publish-date").text
        date = datetime.strptime(time_elem, "%B %d, %Y")  # type: ignore

        content_container = self.driver.find_elements(By.CSS_SELECTOR, "section.eb-article__body-content p")
        content = [
            contents.text for contents in content_container
        ]
        content = ''.join(content)

        return ScrapedNewsModel(
            header=title,
            date=date,
            source="Eco-bussiness",
            content=content,
            url=url,
            authors=[author],
            topics=None,
        )


    def _scrap_social_europe(
        self, url: str
    ) -> ScrapedNewsModel:
        '''
        Access the given URL and scrapes Social Europe.

        Args:
            url (str): The Social Europe article URL

        Raises:
            WEForumError: If the URL is not a valid Social Europe URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNewsModel: an object with the publication information.
        '''
        logger.debug(f"Scraping Social Europe article: {url}")
        if "https://www.socialeurope.eu/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for The Atlantic article scrapper"
            )

        ScrapUtils.disable_js(self.driver) # Disable JS
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(By.CLASS_NAME, "entry-title").text

        authors_line = self.driver.find_element(By.CLASS_NAME, "entry-author").text
        authors_line = authors_line.replace(",", " ").replace("and", " ")
        authors = [
            authors_line.strip()
        ]
        author = "".join(authors)

        time_elem = self.driver.find_element(By.CLASS_NAME, "entry-time").text
        date_without_suffix = TimeUtils.format_suffix_date(time_elem)

        date = datetime.strptime(date_without_suffix, "%d %B %Y")  # type: ignore
        
        content_container = self.driver.find_element(By.CLASS_NAME, "entry-content")
        content = content_container.text

        ScrapUtils.enable_js(self.driver)  # Enable JS again

        return ScrapedNewsModel(
            header=title,
            date=date,
            source="Australian Institute Of International Affairs",
            content=content,
            url=url,
            authors=[author],
            topics=None,
        )
    

    def _scrap_african_center_economic_transformation(
        self, url: str
    ) -> ScrapedNewsModel:
        '''
        Access the given URL and scrapes African Center Economic Transformation.

        Args:
            url (str): The African Center Economic Transformation article URL

        Raises:
            WEForumError: If the URL is not a valid Social Europe URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNewsModel: an object with the publication information.
        '''
        logger.debug(f"Scraping African Center Economic Transformation article: {url}")
        if "https://acetforafrica.org/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for African Center Economic Transformation article scrapper"
            )
        
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(By.CSS_SELECTOR, "div.et_pb_text_inner h1").text
        author = self.driver.find_element(By.CSS_SELECTOR, "div.dmach-postmeta-item-containter p span").text
        time_elem = self.driver.find_element(By.CSS_SELECTOR, "div.et_pb_module.et_pb_text.et_pb_text_3_tb_body.et_pb_text_align_left.et_pb_bg_layout_light div.et_pb_text_inner").text
        date_ft = time_elem.replace(",", "")
        date = datetime.strptime(date_ft, "%b %d %Y")  # type: ignore
        content_container = self.driver.find_elements(By.CSS_SELECTOR, "div.et_pb_module.et_pb_post_content.et_pb_post_content_0_tb_body p")
        content = [
            contents.text for contents in content_container
        ]
        content = ''.join(content)

        return ScrapedNewsModel(
            header=title,
            date=date,
            source="Australian Institute Of International Affairs",
            content=content,
            url=url,
            authors=[author],
            topics=None,
        )

    # TODO mirar si se scrapea noticias y sponsor
    def _scrap_oliver_wyman(
        self, url: str
    ) -> ScrapedNewsModel:
        '''
        Access the given URL and scrapes Oliver Wyman.

        Args:
            url (str): Oliver Wyman article URL

        Raises:
            WEForumError: If the URL is not a valid Social Europe URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNewsModel: an object with the publication information.
        '''
        logger.debug(f"Scraping Oliver Wyman article: {url}")
        if "https://www.oliverwyman.com/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Oliver Wyman article scrapper"
            )
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(By.CSS_SELECTOR, "div.text-primary.text-primary--subheading").text
        author_elem = self.driver.find_element(By.CSS_SELECTOR, "div.authors.text-secondary.text-secondary--description__small").text
        author = ''.join(author_elem.replace("By ", ""))

        date = datetime.now() # article´s website without date

        contents_container = self.driver.find_element(By.CSS_SELECTOR, "div.text-secondary")
        content = contents_container.text

        return ScrapedNewsModel(
            header=title,
            date=date,
            source="Oliver Wyman",
            content=content,
            url=url,
            authors=[author],
            topics=None,
        )

    def _scrap_iese(
        self, url: str
    ) -> ScrapedNewsModel:
        '''
        Access the given URL and scrapes IESE.

        Args:
            url (str): IESE article URL

        Raises:
            WEForumError: If the URL is not a valid Social Europe URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNewsModel: an object with the publication information.
        '''
        logger.debug(f"Scraping IESE article: {url}")
        if "https://www.iese.edu/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for IESE article scrapper"
            )

        # TODO check popup
        ScrapUtils.disable_js(self.driver) # Disable JS
        
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(By.CLASS_NAME, "title").text

        time_elem = self.driver.find_element(By.CLASS_NAME, "small-txt").text
        date_ft = time_elem.replace(",", "")
        date = datetime.strptime(date_ft, "%b %d %Y")  # type: ignore

        authors_elem = self.driver.find_element(By.XPATH, '//div[@class="content description-subHeader"]/p[1]').text
        author = authors_elem.replace("By", "")

        content_container = self.driver.find_elements(By.XPATH, '//div[@class="content description-subHeader"]/p')
        content = [
            contents.text for contents in content_container
        ]
        content = ''.join(content)

        ScrapUtils.enable_js(self.driver)  # Enable JS again

        return ScrapedNewsModel(
            header=title,
            date=date,
            source="IESE",
            content=content,
            url=url,
            authors=[author],
            topics=None,
        )

    # TODO Refactor function 
    def _scrap_harvard_business_review(
        self, url: str
    ) -> ScrapedNewsModel:
        '''
        Access the given URL and scrapes Harvard Business Review.

        Args:
            url (str): Harvard Business Review article URL

        Raises:
            WEForumError: If the URL is not a valid Social Europe URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNewsModel: an object with the publication information.
        '''
        logger.debug(f"Scraping Harvard Business Review article: {url}")
        if "https://hbr.org/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Harvard Business Review article scrapper"
            )

        # TODO check popup
        ScrapUtils.disable_js(self.driver) # Disable JS

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        if "https://hbr.org/podcast/" in url:
            title = self.driver.find_element(By.CSS_SELECTOR, "h1.podcast-post__banner-title.podcast__h2").text

            time_elem = self.driver.find_element(By.CSS_SELECTOR, "span[class='podcast-details__date publication-date text-gray']").text
            date_ft = time_elem.replace(",", "")
            date = datetime.strptime(date_ft, "%b %d %Y")  # type: ignore

            content_container = self.driver.find_elements(By.CSS_SELECTOR, "section[id='details-section'] p")
            content = [
                contents.text for contents in content_container
            ]
            content = ''.join(content)

            author = 'HBR'

            topic = self.driver.find_element(By.CSS_SELECTOR, "a[class='topic--large']").text

        elif "https://hbr.org/sponsored/" in url:
            title = self.driver.find_element(By.CSS_SELECTOR, "h1[class=sponsored-article-hed]").text

            time_elem = self.driver.find_element(By.CLASS_NAME, "publication-date").text
            date_ft = time_elem.replace(",", "")
            date = datetime.strptime(date_ft, "%b %d %Y")  # type: ignore

            content_container = self.driver.find_elements(By.CSS_SELECTOR, "content p")
            content = [
                contents.text for contents in content_container
            ]
            content = ''.join(content)

            author = ''

            topic = '' # There is not topic
        else:
            title = self.driver.find_element(By.CSS_SELECTOR, "div.Title_standard__x_GEq.Title_standard__x_GEq").text

            time_elem = self.driver.find_element(By.CSS_SELECTOR, "div.PublicationDate_standard__rpflO.PublicationDate_non-magazine-date-container__Ln4Wl").text
            date_ft = time_elem.replace(",", "")
            date = datetime.strptime(date_ft, "%b %d %Y")  # type: ignore

            content_container = self.driver.find_elements(By.CSS_SELECTOR, "div.Standard_content__mghDk p")
            content = [
                contents.text for contents in content_container
            ]
            content = ''.join(content)

            author = ''

            topic = self.driver.find_element(By.CSS_SELECTOR, "div.MainTopicLink_container__L7tHy.MainTopicLink_standard__WcK3Y").text

        ScrapUtils.enable_js(self.driver)  # Enable JS again

        return ScrapedNewsModel(
            header=title,
            date=date,
            source="Harvard Business Review",
            content=content,
            url=url,
            authors=[author],
            topics=[topic],
        )

    def _scrap_coronell_university(
        self, url: str
    ) -> ScrapedNewsModel:
        '''
        Access the given URL and scrapes Cornell University.

        Args:
            url (str): Cornell University article URL.

        Raises:
            WEForumError: If the URL is not a valid Social Europe URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNewsModel: an object with the publication information.
        '''
        logger.debug(f"Scraping Cornell University article: {url}")
        if "https://news.cornell.edu/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Cornell University article scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(By.CSS_SELECTOR, "header.expanded.stories h1").text

        time_elem = self.driver.find_element(By.CSS_SELECTOR, "span.byline time").text
        date_ft = time_elem.replace(",", "")
        date = datetime.strptime(date_ft, "%b %d %Y")  # type: ignore

        author = self.driver.find_element(By.CSS_SELECTOR, "h2.byline span").text

        content_container = self.driver.find_elements(By.CSS_SELECTOR, "div.field__item p")
        content = [
            contents.text for contents in content_container
        ]
        content = ''.join(content)

        return ScrapedNewsModel(
            header=title,
            date=date,
            source="Cornell University",
            content=content,
            url=url,
            authors=[author],
            topics=None,
        )

    def _scrap_govlab_living_library(
        self, url: str
    ) -> ScrapedNewsModel:
        '''
        Access the given URL and scrapes GovLab - Living Library.

        Args:
            url (str): GovLab - Living Library article URL.

        Raises:
            WEForumError: If the URL is not a valid Social Europe URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNewsModel: an object with the publication information.
        '''
        logger.debug(f"Scraping GovLab - Living Library article: {url}")
        if "https://thelivinglib.org/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for GovLab - Living Library article scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(By.CSS_SELECTOR, "h1.entry-title").text

        time_elem = self.driver.find_element(By.CSS_SELECTOR, "time.entry-date.published").text
        date_ft = time_elem.replace(",", "")
        date = datetime.strptime(date_ft, "%b %d %Y")  # type: ignore

        author = self.driver.find_element(By.CSS_SELECTOR, "span.author.vcard").text

        content_container = self.driver.find_elements(By.CSS_SELECTOR, "div.entry-content p")
        content = [
            contents.text for contents in content_container
        ]
        content = ''.join(content)

        return ScrapedNewsModel(
            header=title,
            date=date,
            source="GovLab - Living Library",
            content=content,
            url=url,
            authors=[author],
            topics=None,
        )

    def _scrap_fronteirs(
        self, url: str
    ) -> ScrapedNewsModel:
        '''
        Access the given URL and scrapes Frontiers.

        Args:
            url (str): Frontiers article URL.

        Raises:
            WEForumError: If the URL is not a valid Social Europe URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNewsModel: an object with the publication information.
        '''
        logger.debug(f"Scraping Frontiers article: {url}")
        if "https://www.frontiersin.org/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Frontiers article scrapper"
            )
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        title = self.driver.find_element(By.CSS_SELECTOR, "div.JournalAbstract__titleWrapper h1").text

        time_elem = self.driver.find_element(By.XPATH, '//p[@class="ArticleLayoutHeader__info__journalDate"]/span[2]').text
        date_ft = time_elem.replace(", ", "")
        date = datetime.strptime(date_ft, "%d %B %Y")  # type: ignore

        authors_group = self.driver.find_elements(By.CLASS_NAME, "authors")
        author = [
            authors.text for authors in authors_group
        ]
        author = ''.join(author)

        content_container = self.driver.find_element(By.CLASS_NAME, "JournalFullText")
        content = content_container.text

        return ScrapedNewsModel(
            header=title,
            date=date,
            source="GovLab - Living Library",
            content=content,
            url=url,
            authors=[author],
            topics=None,
        )

    ''''''

    def scrap_news(self, from_days_ago: int) -> list[ScrapedNewsModel]:
        logger.info("Scraping WEForum")
        self.driver.maximize_window()
        self.driver.get(self.cybersecturity_topic_url)

        time.sleep(self.load_time)
        # Sign in if not already
        if not self._is_logged_in():
            self._login()

        ScrapUtils.click_element(
            self.driver, ".CallToAction__CloseButton-sc-9356e940-7.fOhVSD"
        )
        time.sleep(self.load_time)

        articles = self._get_websites_to_scrap(from_days_ago)

        publicaion_scrappers = {
            "World Economic Forum": self._scrap_WEF_story_publication,
            "Wired": self._scrap_wired_story,
            "GlobalData": self._scrap_globaldata_newsletter,
            "The Quantum Insider": self._scrap_the_quantum_insider,
            "Australian Strategic Policy Institute": self._scrap_australian_strategic_policy_institute,
            "ProPublica": self._scrap_propbublica_article,
            "The Conversation (French)": self._scrap_the_conversation,
            "The Conversation (Spanish)": self._scrap_the_conversation,
            "The Conversation": self._scrap_the_conversation,
            "The Atlantic": self._scrap_the_atlantic,
            "SpringerOpen": self._scrap_springeropen,
            "Electronic Frontier Foundation": self._scrap_electronic_frontier_foundation_deeplink,
            "Australian Institute of International Affairs": self._scrap_australian_institute_international_affairs,
            "Science Daily": self._scrap_sciencedaily,
            "Rand Corporation": self._scrap_rand_corporation,
            "Eco-Business": self._scrap_eco_bussiness,
            "Social Europe": self._scrap_social_europe,
            "African Center for Economic Transformation": self._scrap_african_center_economic_transformation,
            "Oliver Wyman": self._scrap_oliver_wyman,
            "IESE": self._scrap_iese,
            "Harvard Business Review": self._scrap_harvard_business_review,
            "Cornell University": self._scrap_coronell_university,
            "GovLab - Living Library": self._scrap_govlab_living_library,
            "Frontiers": self._scrap_fronteirs
        }

        scraped_publications: list[ScrapedNewsModel] = []

        #with Progress() as progress:
        #    task = progress.add_task("[cyan]Scraping articles...", total=len(articles))

        for article in articles:
            if article["type"] == "publication":
                scrapper_function: Optional[Callable] = publicaion_scrappers.get(
                    article["publisher"]
                )
                if scrapper_function:
                    try:
                        publication_data = scrapper_function(article["url"])
                        scraped_publications.append(publication_data)
                    except Exception as e:
                        logger.error(f"Error scraping {article['url']}:\n {e}")
                else:
                    logger.warning(
                        f"No scrapper function found for publisher: {article['publisher']}"
                    )
        #        progress.advance(task)

        self._close()
        logger.info("WEForum scraping finished")
        return scraped_publications
'''
WEB SITES NOT SCRAP

Eco-Business CHECK
Social Europe CHECK OKEY
African Center for Economic Transformation CHECK
Oliver Wyman CHECK
IESE CHECK  OKEY
Harvard Business Review CHECK
Cornell University CHECK    OKEY
GovLab - Living Library CHECK   OKEY
Frontiers CHECK
Institut des Relations Internationales et Stratégiques TODO
Institut Montaigne TODO
DIW Berlin TODO
Asian Development Bank TODO
Wharton School of the University of Pennsylvania TODO
International Telecommunication Union TODO
War on the Rocks TODO
Istituto Affari Internazionali TODO
Geneva Centre for Security Sector Governance (DCAF) TODO
TRENDS Research & Advisory TODO
'''