# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 12:39:40 2025

@author: Álvaro Prieto Álvarez
Scrapper for the World Economic Forum website. It allows to scrape the articles from the Cybersecurity topic.
"""

import locale
import random
import time
from datetime import datetime
from typing import Callable, Optional

from loguru import logger
from pydantic import HttpUrl
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from digiliencia.configs.env import Env
from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.data.scrapping.abc_scraper import AbstractScraper
from digiliencia.data.scrapping.weforum.acet_scraper import ACETScraper
from digiliencia.data.scrapping.weforum.asian_development_bank_scraper import (
    AsianDevelopmentBankScraper,
)
from digiliencia.data.scrapping.weforum.au_international_affairs_scraper import (
    AuInternationalAffairsScraper,
)
from digiliencia.data.scrapping.weforum.au_strategic_policy_institute_scraper import (
    AuStrategicInstituteScraper,
)
from digiliencia.data.scrapping.weforum.bank_england_scraper import BankEnglandScraper
from digiliencia.data.scrapping.weforum.coronell_university_scraper import (
    CoronellUniversityScraper,
)
from digiliencia.data.scrapping.weforum.dcaf_scraper import DCAFScraper
from digiliencia.data.scrapping.weforum.diw_berlin_scraper import DIWBerlinScraper
from digiliencia.data.scrapping.weforum.eco_business_scraper import EcoBusinessScraper
from digiliencia.data.scrapping.weforum.eff_scraper import EFFScraper
from digiliencia.data.scrapping.weforum.findev_gateway_scraper import (
    FindevGatewayScraper,
)
from digiliencia.data.scrapping.weforum.frontiers_digital_health_scraper import (
    FrontiersDigitalHealthScraper,
)
from digiliencia.data.scrapping.weforum.frontiers_scraper import FrontiersScraper
from digiliencia.data.scrapping.weforum.globaldata_scraper import GlobalDataScraper
from digiliencia.data.scrapping.weforum.govlab_living_library_scraper import (
    GovlabLivingLibraryScraper,
)
from digiliencia.data.scrapping.weforum.harvard_business_review_scraper import (
    HarvardBusinessReviewScraper,
)
from digiliencia.data.scrapping.weforum.iese_scraper import IESEScraper
from digiliencia.data.scrapping.weforum.institut_montaigne_scraper import (
    InstitutMontaigneScraper,
)
from digiliencia.data.scrapping.weforum.iris_scraper import IRISScraper
from digiliencia.data.scrapping.weforum.london_school_economics_scraper import (
    LondonSchoolEconomicsScraper,
)
from digiliencia.data.scrapping.weforum.nature_scraper import NatureScraper
from digiliencia.data.scrapping.weforum.next_city_scraper import NextCityScraper
from digiliencia.data.scrapping.weforum.oliver_wyman_scraper import OliverWymanScraper
from digiliencia.data.scrapping.weforum.pro_publica_scraper import ProPublicaScraper
from digiliencia.data.scrapping.weforum.quantum_insider_scraper import (
    QuantumInsiderScraper,
)
from digiliencia.data.scrapping.weforum.rand_scraper import RandScraper
from digiliencia.data.scrapping.weforum.reliefweb_scraper import ReliefwebScraper
from digiliencia.data.scrapping.weforum.science_daily_scraper import SienceDailyScraper
from digiliencia.data.scrapping.weforum.social_europe_scraper import SocialEuropeScraper
from digiliencia.data.scrapping.weforum.southern_voice_scraper import (
    SouthernVoiceScraper,
)
from digiliencia.data.scrapping.weforum.the_conversation_scraper import (
    TheConversationScraper,
)
from digiliencia.data.scrapping.weforum.trends_research_advisory_scraper import (
    TrendsResearchAdvisoryScraper,
)
from digiliencia.data.scrapping.weforum.unidir_scraper import UnidirScraper
from digiliencia.data.scrapping.weforum.war_on_the_rocks_scraper import (
    WarOnTheRocksScraper,
)
from digiliencia.data.scrapping.weforum.wired_scraper import WiredScraper
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

        # Wait for about 13 seconds
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
            By.CLASS_NAME, "TopicDetailPanel__StyledContainer-sc-f9692827-0"
        )
        self.driver.execute_script("arguments[0].scrollTo(0, 500);", aside_div)
        time.sleep(self.load_time)

        # Cambiar a artículos recientes
        self.driver.find_element(
            By.CSS_SELECTOR, "label[for='knowledge-toggle-latest']"
        ).click()
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
                By.CLASS_NAME, "ListItemBox-sc-99b5f2ba-0"
            )

            # Solo procesar los nuevos artículos (los que aún no hemos visto)
            new_articles_count = len(current_articles) - last_articles_count

            if new_articles_count > 0:
                logger.debug(f"Processing {new_articles_count} new articles")
                no_new_articles_count = 0  # Reiniciar contador de intentos

                # Procesar solo los nuevos artículos
                for article in current_articles[last_articles_count:]:
                    try:
                        # Check article date
                        age_element = article.find_element(
                            By.CLASS_NAME, "SourceLabel__StyledDate-sc-dca16eb8-4"
                        )
                        age = age_element.text

                        if (
                            "hour" not in age
                            and TimeUtils.days_between_dates(age, age_words) > 0
                        ):
                            title = article.find_element(
                                By.CLASS_NAME, "shared__StyledTitle-sc-16a1486f-1"
                            ).text
                            logger.info(f"Too old article found: '{title}' from {age}")
                            found_old_article = True
                            break

                        type_element = article.find_element(
                            By.CLASS_NAME, "shared__StyledType-sc-16a1486f-0"
                        )
                        article_type = type_element.text.lower()

                        if article_type == "publication":
                            publisher = article.find_element(
                                By.CLASS_NAME, "SourceLabel__StyledText-sc-dca16eb8-2"
                            ).text
                            title = article.find_element(
                                By.CLASS_NAME, "shared__StyledTitle-sc-16a1486f-1"
                            ).text
                            link_element = article.find_element(
                                By.CLASS_NAME,
                                "UIActionButton__StyledButton-sc-bc4b16c4-2",
                            )
                            title_attr = link_element.get_attribute("title")
                            href = link_element.get_attribute("href")

                            if (
                                title_attr == "Open"
                                and href
                                and href not in processed_urls
                            ):
                                processed_urls.add(href)  # Evitar duplicados
                                processed_articles.append(
                                    {
                                        "type": article_type,
                                        "publisher": publisher,
                                        "title": title,
                                        "url": href,
                                    }
                                )
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
                logger.debug(
                    f"No new articles found. Retrying ({no_new_articles_count}/{self.MAX_SCROLL_RELOADS})"
                )

                # Reiniciar el scroll si no se encuentran nuevos artículos después de varios intentos
                if no_new_articles_count >= self.MAX_SCROLL_RELOADS:
                    logger.warning("Max retries reached. Stopping articles discovery.")
                    break

                # Scroll hacia arriba para refrescar y luego hacia abajo para cargar nuevos
                if no_new_articles_count % 2 == 0:
                    self.driver.execute_script(
                        "arguments[0].scrollTo(0, 0);", aside_div
                    )

            # Scroll hacia abajo para cargar más artículos si es necesario
            if not found_old_article:
                self.driver.execute_script(
                    "arguments[0].scrollTo(0, arguments[0].scrollHeight);", aside_div
                )
                # Tiempo de espera aleatorio para simular comportamiento humano
                wait_time = random.uniform(self.load_time, self.load_time + 1)
                time.sleep(wait_time)

        logger.info(
            f"Articles discovery ended. Found {len(processed_articles)} articles."
        )
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

    def _scrap_WEF_story_publication(self, url: str) -> ScrapedNews:
        """Access the given URL and scrapes the publication.

        Args:
            url (str): World Economic Forum publication URL

        Raises:
            WEForumError: If the URL is not a valid WEForum stories URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page

        Returns:
            ScrapedNews with the publication information.
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

        content = content_container.text  # TODO: althoug this may contain the content, it may not be the best way to extract it, as it can also contain other elements like links, images, etc.
        return ScrapedNews(
            header=header,
            date=date,
            source="World Economic Forum",
            content=content,
            url=HttpUrl(url),
            authors=[author],
            topics=None,
        )

    def _scrap_springeropen(self, url: str) -> ScrapedNews:
        """
        Access the given URL and scrapes SpringerOpen.

        Args:
            url (str): SpringerOpen article URL

        Raises:
            WEForumError: If the URL is not a valid SpringerOpen article URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            ScrapedNews: an object with the publication information.
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

        return ScrapedNews(
            header=title,
            date=date,
            source="SpringerOpen",
            content=content,
            url=HttpUrl(url),
            authors=authors,
            topics=None,
        )

    def scrap_news(self, from_days_ago: int) -> list[ScrapedNews]:
        logger.info("Scraping WEForum")
        self.driver.maximize_window()
        self.driver.get(self.cybersecturity_topic_url)

        time.sleep(self.load_time)
        # Sign in if not already
        if not self._is_logged_in():
            self._login()

        ScrapUtils.click_element(
            self.driver, ".CallToAction__CloseButton-sc-a62859f4-7.kFxtTm"
        )
        time.sleep(self.load_time)

        articles = self._get_websites_to_scrap(from_days_ago)

        publication_scrappers = {
            # "World Economic Forum": self._scrap_WEF_story_publication,  # TODO
            "Wired": WiredScraper.scrap,
            "GlobalData": GlobalDataScraper.scrap,
            "The Quantum Insider": QuantumInsiderScraper.scrap,
            "Australian Strategic Policy Institute": AuStrategicInstituteScraper.scrap,
            "ProPublica": ProPublicaScraper.scrap,
            "The Conversation (French)": TheConversationScraper.scrap,
            "The Conversation (Spanish)": TheConversationScraper.scrap,
            "The Conversation": TheConversationScraper.scrap,
            "SpringerOpen": self._scrap_springeropen,
            "Electronic Frontier Foundation": EFFScraper.scrap,
            "Australian Institute of International Affairs": AuInternationalAffairsScraper.scrap,
            "Science Daily": SienceDailyScraper.scrap,
            "Rand Corporation": RandScraper.scrap,
            "RAND Corporation": RandScraper.scrap,
            "Eco-Business": EcoBusinessScraper.scrap,
            "Social Europe": SocialEuropeScraper.scrap,
            "African Center for Economic Transformation": ACETScraper.scrap,
            "Oliver Wyman": OliverWymanScraper.scrap,
            "IESE": IESEScraper.scrap,
            "Harvard Business Review": HarvardBusinessReviewScraper.scrap,
            "Cornell University": CoronellUniversityScraper.scrap,
            "GovLab - Living Library": GovlabLivingLibraryScraper.scrap,
            "Frontiers": FrontiersScraper.scrap,
            "Asian Development Bank": AsianDevelopmentBankScraper.scrap,
            "DIW Berlin": DIWBerlinScraper.scrap,
            "War on the Rocks": WarOnTheRocksScraper.scrap,
            "Institut Montaigne": InstitutMontaigneScraper.scrap,
            "Institut des Relations Internationales et Stratégiques": IRISScraper.scrap,
            "Geneva Centre for Security Sector Governance (DCAF)": DCAFScraper.scrap,
            "Nature": NatureScraper.scrap,
            "Next City": NextCityScraper.scrap,
            "FinDev Gateway": FindevGatewayScraper.scrap,
            "UNIDIR": UnidirScraper.scrap,
            "Frontiers in Digital Health": FrontiersDigitalHealthScraper.scrap,
            "TRENDS Research & Advisory": TrendsResearchAdvisoryScraper.scrap,
            "London School of Economics and Political Science": LondonSchoolEconomicsScraper.scrap,
            "Southern Voice": SouthernVoiceScraper.scrap,
            "ReliefWeb": ReliefwebScraper.scrap,
            "Bank of England": BankEnglandScraper.scrap,
        }

        scraped_publications: list[ScrapedNews] = []

        for article in articles:
            if article["type"] == "publication":
                scrapper_function: Optional[Callable] = publication_scrappers.get(
                    article["publisher"]
                )
                if scrapper_function:
                    try:
                        locale.setlocale(
                            locale.LC_TIME, "en_US.UTF-8"
                        )  # Change language to english

                        publication_data = scrapper_function(article["url"])
                        scraped_publications.append(publication_data)

                        locale.setlocale(
                            locale.LC_TIME, "es_ES.UTF-8"
                        )  # Change language to spanish

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
