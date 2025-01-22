from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from .env_loader import EnvLoader

class Scrap:

    def __init__(self):
        load = EnvLoader()
        self.timeout = load.webdriverwait_timeout

    def configuration(self):
        '''
        Configuration global for all sprits scrapping
        Returns:
            Driver
        '''
        opt = Options()
        #opt.add_argument("--headless") #Run the script without using a graphical interface
        #The following functions are used to improve the performance of the script
        opt.add_argument("--disable-gpu") #During execution, disable the graphics
        opt.add_argument("--disable-dev-shm-usage") #During execution, avoid sharing memory
        opt.add_argument("--no-sandbox") #Disable sandbox mode on your computer
        opt.add_argument("--disable-extensions") #Start the browser without any extensions
        
        opt.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.84 ")
        
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=opt
        )

        return driver

    def disablaled_cookie_popup(self, driver, selector):
        """
        Disables cookie pop-ups on a website.
        Args:
            driver: Selenium browser instance.
            selectors: List of selectors (XPath, CSS) that identify the accept or reject cookie buttons.
        Return:
            None
        """
        try:
            # Wait for the button to be present
            WebDriverWait(driver, self.timeout).until(EC.element_to_be_clickable((By.XPATH, selector))).click()
            print(f"Cookie popup closed with selector: {selector}")
            return
        except Exception as e:
            print("ERROR close popup cookies: " + e)

    def load_subpage(self, driver, xpath):
        '''
        Load subpage of a website 
        Args:
            driver : Selenium browser instance.
            xpath (String): xpath of a element 

        Return:
            subpage_link
        '''
        # Wait until the subpage link is visible and click on it
        subpage_link = WebDriverWait(driver, self.timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))  # Adjust the XPATH according to the link
        )
        subpage_link.click()
        
        # Wait for the subpage to load
        WebDriverWait(driver, self.timeout).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))  # Wait until the body content is loaded
        )

        return subpage_link
    
    def exist_xpath(driver, xpath):
        elementos = driver.find_elements(By.XPATH, xpath)
        return len(elementos) > 0