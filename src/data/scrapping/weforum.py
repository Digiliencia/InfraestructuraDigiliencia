# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 12:39:40 2025

@author: Álvaro Prieto Álvarez
Scrapper for the World Economic Forum website. It allows to scrape the articles from the Cybersecurity topic.
"""

import random
import time
from datetime import datetime
from typing import Callable, Optional, Union
from urllib.parse import parse_qs, urlparse

from loguru import logger
from rich.progress import Progress
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.env_loader import EnvLoader
from utils.scrap import ScrapUtils
from utils.time import TimeUtils


class WEForumError(Exception):
    def __init__(self, message):
        self.message = message


class WEForumScrapper:
    def __init__(self):
        logger.debug("Initializing WEForumScrapper")
        EnvLoader()  # Call EnvLoader to force reading the .env file
        self.driver = ScrapUtils.get_driver()

        self.weforum_email = EnvLoader.weforum_email
        self.weforum_passwd = EnvLoader.weforum_passwd
        self.timeout = EnvLoader.webdriverwait_timeout
        self.cybersecturity_topic_url = (
            "https://intelligence.weforum.org/topics/a1Gb00000015LbsEAE"
        )
        self.home_page = "https://www.weforum.org/"
        self.stories_url = "https://www.weforum.org/stories"
        self.login_page = "https://login.weforum.org/"
        self.load_time = 2

    def _login(self):
        """Log in to the World Economic Forum website using the credentials provided in the .env file

        Raises:
            TimeoutError: If the login button is not found after 5 seconds
        """

        # Accept cookies if pop-up visible
        logger.debug("Loging in to WEForum")
        if ScrapUtils._if_element_exists(self.driver, By.ID, "CybotCookiebotDialog"):  # type: ignore
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
        """Get the links to the articles to scrape.

        Args:
            max_age_dates (int): List of dates to filter the articles

        Raises:
            ValueError: If max_age_date is less than 1 or if the article type is not recognized


        Returns:
            list: List of ditct with the type (video, publication, ...), publisher, title and url of each article
        """
        logger.debug("Getting the websites to scrap")
        if max_age_date < 1:
            logger.error("max_age_date must be greater than 0")
            raise ValueError("max_age_date must be greater than 0")

        age_words = TimeUtils.format_days_ago(max_age_date)

        aside_div = self.driver.find_element(
            By.CLASS_NAME,
            "TopicDetailPanel__StyledContainer-sc-9d1f1b4c-0",
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
            By.CLASS_NAME, "ListItemBox-sc-47508d61-0"
        )
        found_old_article: bool = False
        checked_articles: int = 0
        # Check if there is an article older than the max_age_date
        while not found_old_article:
            while checked_articles < len(articles) and not found_old_article:
                age = (
                    articles[checked_articles]
                    .find_element(
                        By.CLASS_NAME, "SourceLabel__StyledDate-sc-b4751e57-4"
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
                    By.CLASS_NAME, "ListItemBox-sc-47508d61-0"
                )
                if len(new_articles) == len(articles):
                    # No more articles to load
                    break
                articles = new_articles

        # Process each article:
        logger.debug(f"Found {len(articles)} articles to process")
        processed_articles: list = []
        for article in articles:

            type = article.find_element(
                By.CLASS_NAME, "shared__StyledType-sc-fd9f989e-0"
            ).text.lower()

            if type == "video":
                # Ignore videos by now
                pass
            elif type == "publication":
                # Get the publisher, title and link
                publisher = article.find_element(
                    By.CLASS_NAME, "SourceLabel__StyledText-sc-b4751e57-2"
                ).text
                title = article.find_element(
                    By.CLASS_NAME, "shared__StyledTitle-sc-fd9f989e-1"
                ).text
                link_element = article.find_element(
                    By.CLASS_NAME,
                    "UIActionButton__StyledButton-sc-ce337a4a-2",
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
                    logger.warning("Link not found: " + title)
                    raise WEForumError("Link not found: " + title)
            else:
                logger.warning("Unknown article type: " + type)
                raise WEForumError("Unknown article type: " + type)

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
        return ScrapUtils._if_element_exists(self.driver, By.ID, "mf_user-icon")

    def _accept_cookies_if_visible(self, accept_bttn_id: str):
        """Accepts the cookies if the pop-up is visible.

        Args:
            accept_bttn_id (str): The ID of the accept button.
        """
        logger.debug("Accepting cookies if visible")
        if ScrapUtils._if_element_exists(self.driver, By.ID, accept_bttn_id):
            accept_bttn = self.driver.find_element(By.ID, accept_bttn_id)
            if accept_bttn.is_displayed():
                accept_bttn.click()
                time.sleep(self.load_time)

    

    def _scrap_sciencedaily(self, url: str) -> dict[str, Union[str, datetime]]:
        """
        Access the given URL and scrapes Science Daily

        Args:
            url (str): Science Daily url article

        Raises:
            WEForumError: If the URL is not a valid Science Daily article URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Return:
            dict: A dictionary with the article information. Contains:
                - title: The title of the article
                - date: The article date
                - authors: The authors of the article
                - content: The content of the article
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

        data = {}
        try:
            data["title"] = self.driver.find_element(By.ID, "headline").text
            data["content"] = self.driver.find_element(By.ID, "text").text
            data["date"] = self.driver.find_element(By.ID, "date_posted").text  # Mirar el formato de la fecha
            data["authors"] = self.driver.find_element(By.XPATH, '//ol[@class="journal"]/li/text()[1]').text  

            return data      
        except WEForumError as e:
            print("ERROR NoSuchElementException: ", e)

    def _scrap_wired_story(self, url: str) -> dict[str, Union[str, datetime]]:
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
        logger.debug(f"Scraping Wired story: {url}")
        # Disable JS
        ScrapUtils.disable_js(self.driver)

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)

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
        ScrapUtils.enable_js(self.driver)  # Enable JS again
        return data

    def _scrap_WEF_story_publication(self, url: str) -> dict[str, Union[str, datetime]]:
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
        logger.debug(f"Scraping WEForum story: {url}")
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
        content_container = self.driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/section/div/div/article/div[2]/div[2]/div[2]",
        )

        data["content"] = (
            content_container.text
        )  # TODO: althoug this may contain the content, it may not be the best way to extract it, as it can also contain other elements like links, images, etc.
        return data

    def _scrap_globaldata_newsletter(self, url: str) -> dict[str, Union[str, datetime]]:
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
        logger.debug(f"Scraping GlobalData newsletter: {url}")
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

    def _scrap_the_quantum_insider(self, url: str) -> dict[str, Union[str, datetime]]:
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
        logger.debug(f"Scraping The Quantum Insider: {url}")
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
    ) -> dict[str, Union[str, datetime]]:
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
        logger.debug(f"Scraping Australian Strategic Policy Institute: {url}")
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

    def _scrap_propbublica_article(self, url: str) -> dict[str, Union[str, datetime]]:
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
        logger.debug(f"Scraping ProPublica article: {url}")
        if "https://www.propublica.org/article/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for ProPublica article scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time * 1.5)

        data = {}

        # Get the title
        data["title"] = self.driver.find_element(By.TAG_NAME, "h1").text

        # Get the date
        time_elems = self.driver.find_elements(By.TAG_NAME, "time")
        for elm in time_elems:
            if elm.get_attribute("datetime"):
                time_elem = elm
                break
        time_data = time_elem.get_attribute("datetime")
        data["date"] = datetime.strptime(time_data, "%Y-%m-%dEST%H:%M")  # type: ignore

        # Get the author
        authors_elem = self.driver.find_element(
            By.XPATH, '//*[@id="main"]/article/div[2]/div/[1]span[1]'
        )
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

    def _scrap_the_conversation(self, url: str) -> dict[str, Union[str, datetime]]:
        """
        Access the given URL and scrapes the publication.

        Args:
            url (str): The Conversation article URL

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

        data = {}

        data["title"] = self.driver.find_element(By.CSS_SELECTOR, "h1").text

        authors_section = self.driver.find_element(By.CLASS_NAME, "content-authors")
        authors_list = authors_section.find_elements(By.TAG_NAME, "li")
        data["author"] = (", ").join(
            [
                author.find_element(By.CLASS_NAME, "author-name").text
                for author in authors_list
            ]
        )

        time_elem = self.driver.find_element(By.CSS_SELECTOR, ".timestamps time")
        data["date"] = datetime.fromisoformat(time_elem.get_attribute("datetime"))  # type: ignore

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
        data["content"] = content

        return data

    def _scrap_the_atlantic(self, url: str) -> dict[str, Union[str, datetime]]:
        """
        Access the given URL and scrapes The Atlantic.

        Args:
            url (str): The Atlantic article URL

        Raises:
            WEForumError: If the URL is not a valid The Atlantic URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            dict: A dictionary with the publication information. Contains:
                - title: The title of the publication
                - date: The publication date
                - author: The author of the publication
                - content: The content of the publication
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

        data = {}

        data["title"] = self.driver.find_element(By.CSS_SELECTOR, "h1").text

        authors_line = self.driver.find_element(By.ID, "byline")
        data["author"] = (", ").join(
            [author.text for author in authors_line.find_elements(By.TAG_NAME, "a")]
        )

        time_elem = self.driver.find_element(By.TAG_NAME, "time")
        data["date"] = datetime.fromisoformat(time_elem.get_attribute("datetime"))  # type: ignore

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

        data["content"] = content

        ScrapUtils.enable_js(self.driver)  # Enable JS again

        return data

    def _scrap_springeropen(self, url: str) -> dict[str, Union[str, datetime]]:
        """
        Access the given URL and scrapes SpringerOpen.

        Args:
            url (str): SpringerOpen article URL

        Raises:
            WEForumError: If the URL is not a valid SpringerOpen article URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            dict: A dictionary with the publication information. Contains:
                - title: The title of the publication
                - date: The publication date
                - author: The author of the publication
                - content: The content of the publication
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

        data = {}

        data["title"] = self.driver.find_element(By.CSS_SELECTOR, "h1").text

        data["author"] = (", ").join(
            [
                author.text
                for author in self.driver.find_elements(
                    By.CSS_SELECTOR, "[data-author-search]"
                )
            ]
        )

        time_elem = self.driver.find_element(By.TAG_NAME, "time")
        data["date"] = datetime.fromisoformat(time_elem.get_attribute("datetime"))  # type: ignore

        content_elem = self.driver.find_element(By.CSS_SELECTOR, "main > article")
        data["content"] = content_elem.text  # TODO: improve content extraction

        return data

    def _scrap_electronic_frontier_foundation_deeplink(
        self, url: str
    ) -> dict[str, Union[str, datetime]]:
        """
        Access the given URL and scrapes Electronic Frontier Foundation deeplink.

        Args:
            url (str): Electronic Frontier Foundation deeplink URL

        Raises:
            WEForumError: If the URL is not a valid Electronic Frontier Foundation deeplink URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            dict: A dictionary with the publication information. Contains:
                - title: The title of the publication
                - date: The publication date
                - author: The author of the publication
                - content: The content of the publication
        """
        logger.debug(f"Scraping Electronic Frontier Foundation deeplink: {url}")
        if "https://www.eff.org/deeplinks/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Electronic Frontier Foundation deeplink scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        data = {}

        data["title"] = self.driver.find_element(By.CSS_SELECTOR, "h1").text

        authors_line = self.driver.find_element(By.CLASS_NAME, "byline")
        data["author"] = (", ").join(
            [author.text for author in authors_line.find_elements(By.TAG_NAME, "a")]
        )

        time_elem = self.driver.find_element(By.CLASS_NAME, "date")
        data["date"] = datetime.strptime(time_elem.text, "%B %d, %Y")  # type: ignore

        article = self.driver.find_element(By.CSS_SELECTOR, 'article[role="article"]')
        content_container = article.find_element(
            By.CSS_SELECTOR, "div.field--name-body"
        )
        data["content"] = content_container.text

        return data

    def _scrap_australian_institute_international_affairs(
        self, url: str
    ) -> dict[str, Union[str, datetime]]:
        """
        Access the given URL and scrapes Australian Institute Of International Affairs page.

        Args:
            url (str): Australian Institute Of International Affairs URL

        Raises:
            WEForumError: If the URL is not a valid Australian Institute Of International Affairs URL
            NoSuchElementException: If any of the required elements (title, date, author, content) are not found on the page.

        Returns:
            dict: A dictionary with the publication information. Contains:
                - title: The title of the publication
                - date: The publication date
                - author: The author of the publication
                - content: The content of the publication
        """
        logger.debug(f"Scraping Australian Institute Of International Affairs: {url}")
        if "https://www.internationalaffairs.org.au/" not in url:
            raise WEForumError(
                "Attempted to scrape invalid page for Australian Institute Of International Affairs scrapper"
            )

        # Access the URL
        self.driver.get(url)
        time.sleep(self.load_time)  # Reject cookies if visible

        data = {}

        data["title"] = self.driver.find_element(By.CLASS_NAME, "post-title").text

        authors_line = self.driver.find_element(By.CLASS_NAME, "author-name").text
        authors_line = authors_line.replace("By ", "")
        authors = [
            author.strip() for author in authors_line.replace(" and ", ", ").split(",")
        ]
        data["author"] = ", ".join(authors)

        time_elem = self.driver.find_element(By.CLASS_NAME, "publish-date")
        data["date"] = datetime.strptime(time_elem.text, "%d %b %Y")  # type: ignore

        content_container = self.driver.find_element(By.CLASS_NAME, "body-content")
        data["content"] = content_container.text

        return data

    def scrap(self, from_days_ago: int) -> tuple[dict[str, str]]:

        logger.info("Scraping WEForum")
        self.driver.maximize_window()
        self.driver.get(self.cybersecturity_topic_url)

        time.sleep(self.load_time)
        # Sign in if not already
        if not self._is_logged_in():
            self._login()

        ScrapUtils.click_element(
            self.driver, ".CallToAction__CloseButton-sc-7e1451ff-7.dqHIyC"
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
            "Science Daily": self._scrap_sciencedaily
        }

        scraped_publications = []

        with Progress() as progress:
            task = progress.add_task("[cyan]Scraping articles...", total=len(articles))

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
                        print(
                            f"No scrapper function found for publisher: {article['publisher']}"
                        )
                progress.advance(task)

        for publication in scraped_publications:
            # print(publication)
            pass

        self._close()
        logger.info("WEForum scraping finished")
        return None  # type: ignore
