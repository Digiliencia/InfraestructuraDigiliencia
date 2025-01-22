# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 10:08:33 2025

@author: Esteban Peña Salazar
Web scrapping: https://www.incibe.es/
"""

# Importing the necessary libraries
import sys
import os

# Add the parent directory (src) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from utils.scrap import Scrap

scrap = Scrap()

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


class IncibeScraper:
    def _disablaled_cookie_popup(self, driver, selector):
        """
        Deactivates the cookies popup in a website.
        :param driver: Instance of the Selenium browser.
        :param selector: XPath or CSS selector to identify the accept/reject cookies buttons.
        """
        try:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, selector))).click()
            print(f"Pop up from cookies closed by selector: {selector}")
        except Exception as e:
            print(f"ERROR closing popup cookies: {str(e)}")

    def _configuration(self):
        """
        Configures and returns the Selenium WebDriver.
        """
        opt = Options()
        opt.add_argument("--disable-gpu")
        opt.add_argument("--disable-dev-shm-usage")
        opt.add_argument("--no-sandbox")
        opt.add_argument("--disable-extensions")
        opt.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.84"
        )

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=opt
        )
        return driver

    def start_scrapping(self):
        """
        Main method to start the scraping process.
        """
        driver = None
        try:
            url_website = "https://www.incibe.es/incibe-cert/blog"
            driver = self._configuration()
            driver.get(url_website)
            print(driver.title)

            # Close the cookies popup
            self._disablaled_cookie_popup(driver, '//div[@class="cookie-buttons"]/button[@data-testid="cookie-button-reject"]')

            # Placeholder for further scraping logic
            print("Scraping logic here...")

        except Exception as e:
            print(f"ERROR: {str(e)}")

        finally:
            if driver:
                driver.quit()


# Run the scraper
if __name__ == "__main__":
    scraper = IncibeScraper()
    scraper.start_scrapping()

'''