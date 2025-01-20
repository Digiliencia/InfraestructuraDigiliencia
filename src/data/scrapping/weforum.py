import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.env_loader import EnvLoader
from utils.time import TimeUtils
import time

class WEForumError(Exception):
    def __init__(self, message):
        self.message = message


class WEForumScrapper:
    def __init__(self):
        self.driver = selenium.webdriver.Chrome()
        self.weforum_email = EnvLoader.weforum_email
        self.weforum_passwd = EnvLoader.weforum_passwd
        self.timeout = EnvLoader.webdriverwait_timeout
        self.cybersecturity_topic_url = (
            "https://intelligence.weforum.org/topics/a1Gb00000015LbsEAE"
        )
        self.home_page = "https://www.weforum.org/"
        self.load_time = 2

    def _login(self):
        """Log in to the World Economic Forum website using the credentials provided in the .env file

        Raises:
            TimeoutError: If the login button is not found after 5 seconds
        """

        # TODO: Implement login within the original url if possible and available
        original_url = self.driver.current_url
        self.driver.get(self.home_page)
        sign_in_bttn = self.driver.getElementById("navbar_sign_in")
        sign_in_bttn.click()

        # Accept cookies if pop-up visible
        cookies_popup = self.driver.getElementById("CybotCookiebotDialog")
        if cookies_popup.is_displayed():
            accept_bttn = self.driver.getElementById(
                "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"
            )
            accept_bttn.click()

        # Introduce email
        email_input = self.driver.getElementById("loginradius-login-emailid")
        email_input.send_keys(self.weforum_email)
        next_bttn = self.driver.getElementById("login-check-email")
        next_bttn.click()

        # Wait until the log-in button is visible or timeout after 5 seconds
        submit_bttn = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((By.ID, "loginradius-submit-login"))
        )
        if submit_bttn is None:
            raise TimeoutError("Login button not found")

        # Introduce password
        passwd_input = self.driver.getElementById("loginradius-login-password")
        passwd_input.send_keys(self.weforum_passwd)
        submit_bttn.click()

        # Return to the original page
        self.driver.get(original_url)

    def _get_links_to_scrape(self, max_age_date: int = 7) -> list[tuple[str, str, str]]:
        """Get the links to the articles to scrape

        Args:
            max_age_dates (int): List of dates to filter the articles
            
        Raises:
            ValueError: If max_age_date is less than 1
            

        Returns:
            list: List of tuples with the publisher, title and link of the articles
        """

        if max_age_date < 1:
            raise ValueError("max_age_date must be greater than 0")

        age_words = TimeUtils.age_format_date(max_age_date)

        # TODO: continue

        articles = self.driver.find_elements_by_class_name("sc-bLmarx dQpFdR")
        found_old_article: bool = False
        checked_articles: int = 0
        # Check if there is an article older than the max_age_date
        while not found_old_article:
            while checked_articles < len(articles) and not found_old_article:
                age = (
                    articles[checked_articles]
                    .find_element_by_class_name("sc-ibMKnd eSUXyy")
                    .text
                )
                if TimeUtils.days_between_dates(age, max_age_date) < 0:
                    # An article written before the max_age_date was found
                    found_old_article = True

                    # Remove the rest of articles
                    articles = articles[:checked_articles]
                checked_articles += 1

            # If no old enough article was found, scroll down to load more articles
            if not found_old_article:
                self.driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);"
                )
                time.sleep(self.load_time)
                new_articles = self.driver.find_elements_by_class_name(
                    "sc-bLmarx dQpFdR"
                )
                if len(new_articles) == len(articles):
                    # No more articles to load
                    break
                articles = new_articles

        # Process each article:
        processed_articles: list = []
        for article in articles:
            publisher = article.find_element_by_class_name("sc-cUnzlc egQVKE").text
            title = article.find_element_by_class_name("sc-ePJuOI eFVjkQ").text
            link_element = article.find_element_by_class_name("sc-hqKjEI cDxNTg")
            link = link_element.get_attribute("href") if link_element.get_attribute("title") == "Open" else None
            if link:
                processed_articles.append((publisher, title, link))
            else:
                raise WEForumError("Link not found: " + title)
        return processed_articles



    def close(self):
        self.driver.close()
