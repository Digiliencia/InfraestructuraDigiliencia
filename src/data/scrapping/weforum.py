# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 12:39:40 2025

@author: Álvaro Prieto Álvarez
Scrapper for the World Economic Forum website. It allows to scrape the articles from the Cybersecurity topic.
"""

from typing import Callable, Optional
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from utils.env_loader import EnvLoader
from utils.time import TimeUtils
from utils.scrap import ScrapUtils
import time
import random
from datetime import datetime
from urllib.parse import urlparse, parse_qs


class WEForumError(Exception):
    def __init__(self, message):
        self.message = message


class WEForumScrapper:
    def __init__(self):
        EnvLoader()  # Call EnvLoader to force reading the .env file
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

        self.weforum_email = EnvLoader.weforum_email
        self.weforum_passwd = EnvLoader.weforum_passwd
        self.timeout = EnvLoader.webdriverwait_timeout
        self.cybersecturity_topic_url = (
            "https://intelligence.weforum.org/topics/a1Gb00000015LbsEAE"
        )
        self.home_page = "https://www.weforum.org/"
        self.stories_url = "https://www.weforum.org/stories"
        self.load_time = 2
        self.login_page = "https://login.weforum.org/"

        self.scrapUtils = ScrapUtils()

    def _login(self):
        """Log in to the World Economic Forum website using the credentials provided in the .env file

        Raises:
            TimeoutError: If the login button is not found after 5 seconds
        """

        # Accept cookies if pop-up visible
        if self.scrapUtils._if_element_exists(self.driver, By.ID, "CybotCookiebotDialog"):  # type: ignore
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
        next_bttn = self.driver.find_element(By.ID, "login-check-email")
        next_bttn.click()

        # Wait until the log-in button is visible or timeout after 5 seconds
        submit_bttn = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((By.ID, "loginradius-submit-login"))
        )
        if submit_bttn is None:
            raise TimeoutError("Login button not found")

        # Introduce password
        time.sleep(self.load_time)
        passwd_input = self.driver.find_element(By.ID, "loginradius-login-password")
        passwd_input.send_keys(self.weforum_passwd)
        time.sleep(1)
        submit_bttn.click()

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
        """Get the links to the articles to scrape.

        Args:
            max_age_dates (int): List of dates to filter the articles

        Raises:
            ValueError: If max_age_date is less than 1 or if the article type is not recognized


        Returns:
            list: List of ditct with the type (video, publication, ...), publisher, title and url of each article
        """

        if max_age_date < 1:
            raise ValueError("max_age_date must be greater than 0")

        age_words = TimeUtils.format_days_ago(max_age_date)

        aside_div = self.driver.find_element(
            By.CSS_SELECTOR,
            "div.TopicDetailPanel__StyledContainer-sc-5e58f9d5-0.jZMWga",
        )
        self.driver.execute_script("arguments[0].scrollTo(0, 500);", aside_div)
        time.sleep(self.load_time)
        latest_label = self.driver.find_element(
            By.CSS_SELECTOR, "label[for='knowledge-toggle-latest']"
        )
        latest_label.click()  # Click on the label as the button is not clickable
        time.sleep(self.load_time)

        latest_articles_div = self.driver.find_element(
            By.CSS_SELECTOR, "div[data-test-id='latest-knowledge-feed']"
        )  # Div containing articles, placed just under the articles search bar
        articles = latest_articles_div.find_elements(
            By.CSS_SELECTOR, ".ListItemBox-sc-47508d61-0.gLXmsV"
        )
        found_old_article: bool = False
        checked_articles: int = 0
        # Check if there is an article older than the max_age_date
        while not found_old_article:
            while checked_articles < len(articles) and not found_old_article:
                age = (
                    articles[checked_articles]
                    .find_element(
                        By.CSS_SELECTOR, ".SourceLabel__StyledDate-sc-b4751e57-4.ejkvkk"
                    )
                    .text
                )
                if (
                    "hour" not in age
                    and TimeUtils.days_between_dates(age, age_words) > 0
                ):
                    # An article written before the max_age_date was found
                    found_old_article = True

                    # Remove the rest of articles
                    articles = articles[:checked_articles]
                checked_articles += 1

            # If no old enough article was found, scroll down to load more articles
            if not found_old_article:
                self.driver.execute_script(
                    "arguments[0].scrollTo(0, arguments[0].scrollHeight);", aside_div
                )
                time.sleep(random.uniform(self.load_time, self.load_time + 2))
                new_articles = latest_articles_div.find_elements(
                    By.CSS_SELECTOR, ".ListItemBox-sc-47508d61-0.gLXmsV"
                )
                if len(new_articles) == len(articles):
                    # No more articles to load
                    break
                articles = new_articles

        # Process each article:
        processed_articles: list = []
        for article in articles:

            type = article.find_element(
                By.CSS_SELECTOR, ".shared__StyledType-sc-fd9f989e-0.lhiwEc"
            ).text.lower()

            if type == "video":
                # Ignore videos by now
                pass
            elif type == "publication":
                # Get the publisher, title and link
                publisher = article.find_element(
                    By.CSS_SELECTOR, ".SourceLabel__StyledText-sc-b4751e57-2.fzCMaX"
                ).text
                title = article.find_element(
                    By.CSS_SELECTOR, ".shared__StyledTitle-sc-fd9f989e-1.hOLaLK"
                ).text
                link_element = article.find_element(
                    By.CSS_SELECTOR,
                    ".UIActionButton__StyledButton-sc-384a1b53-2.jLISFv",
                )
                link = (
                    link_element.get_attribute("href")
                    if link_element.get_attribute("title") == "Open"
                    else None
                )
                if link:
                    processed_articles.append(
                        {
                            "type": type,
                            "publisher": publisher,
                            "title": title,
                            "url": link,
                        }
                    )
                else:
                    raise WEForumError("Link not found: " + title)
            else:
                raise WEForumError("Unknown article type: " + type)

        return processed_articles

    def _close(self):
        """
        Closes the current browser window.

        This method will close the browser window that is currently controlled by the driver instance.
        """
        self.driver.close()

    def _is_logged_in(self) -> bool:
        """Being in the topic page, checks if the user is logged in.

        Returns:
            bool: True if the user is logged in, False otherwise.

        Raises:
            WEForumError: If the user is not in the topic page
        """
        if self.driver.current_url != self.cybersecturity_topic_url:
            raise WEForumError(
                "Cannot check if logged in because browser is not in the topic page"
            )

        # If the user logo (id: mf_user-icon) exists, user is loged in
        return self.scrapUtils._if_element_exists(self.driver, By.ID, "mf_user-icon")

    def _accept_cookies_if_visible(self, accept_bttn_id: str):
        """Accepts the cookies if the pop-up is visible.

        Args:
            accept_bttn_id (str): The ID of the accept button.
        """
        if self.scrapUtils._if_element_exists(self.driver, By.ID, accept_bttn_id):
            accept_bttn = self.driver.find_element(By.ID, accept_bttn_id)
            if accept_bttn.is_displayed():
                accept_bttn.click()
        time.sleep(self.load_time)

    def _scrap_wired_story(self, url: str) -> dict[str, str | datetime]:
        """Access the given URL and scrapes the publication.

        Args:
            url (str): Wired story URL

        Raises:
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            dict: A dictionary with the publication information. Contains:
                - title: The title of the publication
                - date: The publication date
                - author: The author of the publication
                - content: The content of the publication
        """
        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)

        # TODO: check if login, as it is not free to access the content

        self._accept_cookies_if_visible("onetrust-accept-btn-handler")

        data = {}
        time_element = self.driver.find_element(By.TAG_NAME, "time")
        date_str = time_element.text
        data["date"] = datetime.strptime(
            date_str, "%b %d, %Y %I:%M %p"
        )  # TODO: take into account case like "Updated a month ago": https://www.wired.com/live/tiktok-scotus-live-coverage/

        author_element = self.driver.find_element(
            By.CSS_SELECTOR, '[data-testid="BylineName"]'
        )
        data["author"] = author_element.text

        title_element = self.driver.find_element(
            By.CSS_SELECTOR, 'h1[data-testid="ContentHeaderHed"]'
        )
        data["title"] = title_element.text

        content_elements = self.driver.find_elements(
            By.CSS_SELECTOR, "div.body__inner-container > p"
        )
        content = ""
        for element in content_elements:
            content += element.text + "\n"

        data["content"] = content

        return data

    def _scrap_WEF_story_publication(self, url: str) -> dict[str, str | datetime]:
        """Access the given URL and scrapes the publication.

        Args:
            url (str): World Economic Forum publication URL

        Raises:
            WEForumError: If the URL is not a valid WEForum stories URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page

        Returns:
            dict: A dictionary with the publication information. Contains:
                - title: The title of the publication
                - date: The publication date
                - author: The author of the publication
                - content: The content of the publication
        """
        if self.stories_url not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for WEForum stories scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)

        data = {}

        # Get the title
        title_element = self.driver.find_element(By.TAG_NAME, "h1")
        data["title"] = title_element.text

        # Get the date
        time_element = self.driver.find_element(By.TAG_NAME, "time")
        data["time"] = datetime.fromisoformat(time_element.get_attribute("datetime"))

        # Get the author
        author_div = self.driver.find_element(By.CSS_SELECTOR, "div.wef-1upaxcp")
        data["author"] = author_div.find_element(
            By.TAG_NAME, "a"
        ).text  # TODO: assess whether it is worthwhile to get the author's profile link and scrape it to.
        # TODO: fix if more than one person wrote the article (list?)

        # Get the content
        classes: dict = {
            "main_section_div": "wef-1a11yf0",  # Includes inside a div with information
            # about the context of the article and a "wef-0" with the main content and a last
            # one with license and other info (like footer).
            "paragraphs": "wef-zw4tnc",
            "related_readings": "wef-1mv5kk8",
            "videos": "wef-hwdz70",
            "podcasts": "wef-1bs0642",
            "subtitles": "wef-1qmtbdn",
            "discover_more": "wef-1r70254",
            "imgs": "wef-ha4kjk",
            "bullet_point_paragraphs": "wef-aa063t",
            "main_bullet_points": "wef-1anm32a",
        }

        """ For getting the main section div containing the rest of divs
        I first search for a normal paragraph, then I go up to the parent (containing the p)
        and after the parent, which will contain every div with
        the classes specified before.
        """
        any_p = self.driver.find_element(By.CLASS_NAME, classes["paragraphs"])
        p_div = any_p.find_element(By.XPATH, "../../..")
        divs = p_div.find_elements(By.XPATH, "./div")
        content = ""

        for div in divs:
            cl = div.get_attribute("class")
            if cl == classes["paragraphs"]:
                content += div.text + "\n"
            elif cl == classes["subtitles"]:
                content += f"\n\n{div.text}\n"
            elif cl == classes["bullet_point_paragraphs"]:
                for li in div.find_elements(By.TAG_NAME, "li"):
                    content += f"\t- {li.text}\n"
            elif cl == classes["main_bullet_points"]:
                for li in div.find_elements(By.TAG_NAME, "li"):
                    content += f"\t- {li.text}\n"
            elif cl == classes["imgs"]:
                img = div.find_element(By.TAG_NAME, "img")
                img_link = img.get_attribute("src")
                img_alt = img.get_attribute("alt")
                content += f"![{img_alt}]({img_link})\n"

        data["content"] = content
        return data

    def _scrap_globaldata_newsletter(self, url: str) -> dict[str, str | datetime]:
        """Access the given URL and scrapes the publication.

        Args:
            url (str): GlobalData newsletter details URL

        Raises:
            WEForumError: If the URL is not a valid GlobalData newsletter details URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            dict: A dictionary with the publication information. Contains:
                - title: The title of the publication
                - date: The publication date
                - author: The author of the publication
                - content: The content of the publication
        """
        # Verify URL
        if "https://www.globaldata.com/newsletter/details" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for GlobalData newsletter scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)

        data = {}

        # Extract date from URL parameter if available
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        newsletter_date = query_params.get("newsletterdate", [None])[0]
        if newsletter_date:
            data["date"] = datetime.strptime(newsletter_date, "%Y-%m-%d")
        else:
            raise WEForumError(
                "newsletter date not found in URL. Cannot set publication date."
            )

        data["author"] = "GlobalData"

        title_element = self.driver.find_element(By.CSS_SELECTOR, "h2>a")
        data["title"] = title_element.text

        content_container = title_element.find_element(By.XPATH, "./../../..")
        content = content_container.text
        data["content"] = content.replace(
            data["title"], ""
        )  # Remove title from content

        return data

    def _scrap_the_conversation(self, url: str) -> dict[str, str | datetime]:
        """Access the given URL and scrapes the publication.

        Args:
            url (str): The Conversation publication URL

        Raises:
            WEForumError: If the URL is not a valid The Conversation URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            dict: A dictionary with the publication information. Contains:
                - title: The title of the publication
                - date: The publication date
                - author: The author of the publication
                - content: The content of the publication
        """
        if "https://theconversation.com/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for The Conversation scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)

        data = {}

        # Get the title
        article = self.driver.find_element(By.ID, "article")
        title_element = article.find_element(By.TAG_NAME, "h1")
        data["title"] = title_element.text

        # Get the date
        time_element = article.find_element(
            By.CSS_SELECTOR, "figure div.timestamps > time"
        )
        data["date"] = datetime.fromisoformat(time_element.get_attribute("datetime"))

        # Get the author
        author_elements = article.find_elements(
            By.CSS_SELECTOR, "section.content-authors span.nobr"
        )
        data["author"] = ", ".join(
            [author_element.text for author_element in author_elements]
        )

        # Get the content
        container = article.find_element(By.CLASS_NAME, "content-body")
        ct = container.text
        data["content"] = ct

        return data

    def _scrap_the_quantum_insider(self, url: str) -> dict[str, str | datetime]:
        """Access the given URL and scrapes the post.

        Args:
            url (str): The Quantum Insider URL

        Raises:
            WEForumError: If the URL is not a valid The Quantum Insider URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            dict: A dictionary with the publication information. Contains:
                - title: The title of the publication
                - date: The publication date
                - author: The author of the publication
                - content: The content of the publication
        """
        if not url.startswith("https://thequantuminsider.com/"):
            raise WEForumError(
                "Attempted to scrape invalid page for The Quantum Insider scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)

        data = {}

        # Get the title
        data["title"] = self.driver.find_element(By.TAG_NAME, "h1").text

        # Get the date
        date_element = self.driver.find_element(By.TAG_NAME, "time")
        data["date"] = datetime.strptime(date_element.text, "%B %d, %Y")

        # Get the author
        data["author"] = self.driver.find_element(
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

        data["content"] = content
        return data

    def _scrap_australian_strategic_policy_institute(
        self, url: str
    ) -> dict[str, str | datetime]:
        """Access the given URL and scrapes the publication.

        Args:
            url (str): Australian Strategic Policy Institute URL

        Raises:
            WEForumError: If the URL is not a valid Australian Strategic Policy Institute URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            dict: A dictionary with the publication information. Contains:
                - title: The title of the publication
                - date: The publication date
                - author: The author of the publication
                - content: The content of the publication
        """
        if "https://www.aspistrategist.org.au/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Australian Strategic Policy Institute scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)

        data = {}

        # Get the title
        data["title"] = self.driver.find_element(By.CLASS_NAME, "entry-title").text

        # Get the date
        date_elem = self.driver.find_element(
            By.CSS_SELECTOR, "article > header > .meta"
        )
        data["date"] = datetime.fromisoformat(date_elem.get_attribute("datetime"))

        # Get the author
        author_elems = self.driver.find_elements(
            By.CSS_SELECTOR, "article > header > .meta > .author"
        )
        data["author"] = ", ".join([author_elem.text for author_elem in author_elems])

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

        data["content"] = content
        return data

    def _scrap_propbublica_article(self, url: str) -> dict[str, str | datetime]:
        """Access the given URL and scrapes the publication.

        Args:
            url (str): ProPublica article URL

        Raises:
            WEForumError: If the URL is not a valid ProPublica article URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            dict: A dictionary with the publication information. Contains:
                - title: The title of the publication
                - date: The publication date
                - author: The author of the publication
                - content: The content of the publication
        """
        if "https://www.propublica.org/article/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for ProPublica article scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)

        data = {}

        # Get the title
        data["title"] = self.driver.find_element(By.TAG_NAME, "h1").text

        # Get the date
        time_container = self.driver.find_element(
            By.CSS_SELECTOR, "time.article-meta-1__pubdate"
        )
        time_elem = time_container.find_element(By.TAG_NAME, "time")
        data["date"] = datetime.strptime(
            time_elem.get_attribute("datetime"), "%Y-%m-%dEST%H:%M"
        )

        # Get the author
        authors_elem = self.driver.find_element(By.CLASS_NAME, "article-meta-1__byline")
        authors = []
        for elem in authors_elem.find_elements(By.XPATH, ".//p"):
            if elem.tag_name in ["span", "a"]:
                authors.append(elem.text)
        data["author"] = ", ".join(authors)

        # Get the content
        content_div = self.driver.find_element(By.CLASS_NAME, "article-body")
        data["content"] = ""
        for p in content_div.find_elements(By.TAG_NAME, "p"):
            data["content"] += p.text + "\n\n"

        return data

    def scrap(self, from_days_ago: int) -> tuple[dict[str, str]]:
        self.driver.maximize_window()
        self.driver.get(self.cybersecturity_topic_url)

        time.sleep(self.load_time)
        # Sign in if not already
        if not self._is_logged_in():
            self._login()

        articles = self._get_websites_to_scrap(from_days_ago)

        publicaion_scrappers = {
            "World Economic Forum": self._scrap_WEF_story_publication,
            "Wired": self._scrap_wired_story,
            "GlobalData": self._scrap_globaldata_newsletter,
            "The Quantum Insider": self._scrap_the_quantum_insider,
            "Australian Strategic Policy Institute": self._scrap_australian_strategic_policy_institute,
            "ProPublica": self._scrap_propbublica_article,
        }

        scraped_publications = []

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
                        print(f"Error scraping {article['url']}:\n {e}")
                else:
                    print(
                        f"No scrapper function found for publisher: {article['publisher']}"
                    )

        for publication in scraped_publications:
            # print(publication)
            pass

        return None  # type: ignore
