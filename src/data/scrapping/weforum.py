import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.env_loader import EnvLoader


class WEForumScrapper:
    def __init__(self):
        self.driver = selenium.webdriver.Chrome()
        self.weforum_email = EnvLoader.weforum_email
        self.weforum_passwd = EnvLoader.weforum_passwd
        self.timeout = EnvLoader.webdriverwait_timeout

    def _login(self):
        original_url = self.driver.current_url
        self.driver.get("https://www.weforum.org/")
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

    def close(self):
        self.driver.close()
