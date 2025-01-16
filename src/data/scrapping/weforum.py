import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.env_loader import EnvLoader
from utils.time import TimeUtils


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

    def _get_links_to_scrape(self, max_age_date: int = 7) -> list:
        """Get the links to the articles to scrape

        Args:
            max_age_dates (int): List of dates to filter the articles

        Returns:
            list: List of links to the articles to scrape
        """

        if max_age_date < 1:
            raise ValueError("max_age_date must be greater than 0")

        age_words = TimeUtils.age_format_date(max_age_date)

        # TODO: continue

    def close(self):
        self.driver.close()
