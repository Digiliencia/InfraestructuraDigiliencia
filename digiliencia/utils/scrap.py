from loguru import logger
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from digiliencia.configs.env import Env


class ScrapUtils:
    def __init__(self):
        self.timeout = Env().webdriverwait_timeout

    @staticmethod
    def get_driver() -> WebDriver:
        """
        Configuration global for all sprits scrapping

        Returns:
            Driver
        """
        logger.debug("Creating Selenium driver")
        options = Options()
        options.add_argument(
            "user-agent="
            + "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50"  # TODO to .env
        )
        options.add_argument("--disable-blink-features=AutomationControlled")
        # Recommended options for containers/headless
        options.add_argument("--headless=new")  # Use modern headless mode
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
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
        service = Service(ChromeDriverManager().install())
        driver = WebDriver(service=service, options=options)
        driver.implicitly_wait(Env().implicit_wait)
        return driver

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
            logger.debug(f"{css_selector} elem not found")
            return False

    @staticmethod
    def if_element_exists(driver: WebDriver, by: By, element: str) -> bool:
        """
        Checks if an element exists on the web page.
        Args:
            by: The type of locator (e.g., By.ID, By.XPATH, etc.).
            element (str): The locator value of the element to find.
        Returns:
            bool: True if the element is found, False otherwise.
        """

        try:
            driver.find_element(by, element)  # type: ignore
        except NoSuchElementException:
            return False
        return True

    @staticmethod
    def disable_js(driver: WebDriver) -> None:
        """
        Disables JavaScript in the given driver.

        Args:
            driver: Selenium browser instance.

        Returns:
            None
        """
        logger.debug("Disabling JavaScript in driver")
        driver.execute_cdp_cmd("Emulation.setScriptExecutionDisabled", {"value": True})

    @staticmethod
    def enable_js(driver: WebDriver) -> None:
        """
        Enables JavaScript in the given driver.

        Args:
            driver: Selenium browser instance.

        Returns:
            None
        """
        logger.debug("Enabling JavaScript in driver")
        driver.execute_cdp_cmd("Emulation.setScriptExecutionDisabled", {"value": False})
