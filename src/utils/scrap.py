from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from utils.env_loader import EnvLoader


class ScrapUtils:

    def __init__(self):
        self.timeout = 1

    @staticmethod
    def get_driver() -> WebDriver:
        """
        Configuration global for all sprits scrapping

        Returns:
            Driver
        """
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

        return WebDriver(options=options)

    @staticmethod
    def click_element(driver: WebDriver, css_selector: str, timeout: int = 2) -> bool:
        """
        Tries to click an element on a website by searching for it by a CSS selector. Waits for the element to be clickable for a given time. If the element is not found, it continues without raising an exception.

        Args:
            driver: Selenium browser instance.
            css_selector: CSS selector of the element.
            timeout: Time in seconds to wait for the element to be clickable.

        Returns:
            True if the element was clicked, False otherwise.
        """
        try:
            # Wait for the 'Rechazar todas' button to be clickable
            wait = WebDriverWait(driver, timeout)
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
            )
            cookie_button.click()
            return True
        except TimeoutException:
            print(f"{css_selector} elem not found")
            return False

    @staticmethod
    def if_element_exists(driver: WebDriver, by: By, element: str) -> bool:
        """
        Check if an element exists on the web page.
        Args:
            by: The type of locator (e.g., By.ID, By.XPATH, etc.).
            element (str): The locator value of the element to find.
        Returns:
            bool: True if the element is found, False otherwise.
        """

        try:
            driver.find_element(by, element)
        except NoSuchElementException:
            return False
        return True