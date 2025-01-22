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


class IncibeScraper:
    def __init__(self):
        """
        Initialize the IncibeScraper class
        """
        self.scrap = Scrap()
        self.driver = self.scrap.configuration()

    def openIncibeBlog(self):
        try:
            self.driver.get("https://www.incibe.es/incibe-cert/blog")
            self.disable_cookie_popup()  # Cierra el popup de cookies
            print("Incibe blog page opened")
        except Exception as e:
            print(f"Error opening Incibe blog page: {e}")
    
    def disable_cookie_popup(self):
        """
        Close the cookie popup if it exists
        """
        try:
            # Busca el botón de "Rechazar cookies"
            cookie_button = self.driver.find_element(By.XPATH, '//div[@class="cookie-buttons"]/button[@data-testid="cookie-button-reject"]')
            cookie_button.click()
            print("Popup de cookies cerrado")
        except NoSuchElementException:
            print("No se encontró el popup de cookies, continuando...")




# Main execution
if __name__ == "__main__":
    scraper = IncibeScraper()  # Create an instance of IncibeScraper
    scraper.openIncibeBlog()   # Call the method
    input("Presiona Enter para cerrar el navegador...")  # Mantén la página abierta
    scraper.driver.quit()      # Cierra el navegador de forma controlada

