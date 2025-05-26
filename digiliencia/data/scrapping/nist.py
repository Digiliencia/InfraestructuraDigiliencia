# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 10:08:33 2025

@author: Carlos Prieto
Web scrapping: https://www.nist.gov/nice/ccw-events
"""

from digiliencia.data.scrapping.abc_scraper import AbstractScraper
from digiliencia.data.models.events_model import ScrapedEventsModel
from digiliencia.utils.scrap import ScrapUtils
from loguru import logger
from selenium.webdriver.common.by import By

class Nist(AbstractScraper):
    '''Scraps only the events of NIST'''

    def __init__(self):
        logger.debug("Initializing NIST")
        self.driver = ScrapUtils.get_driver()
        self.url_cybersegurity = "https://www.nist.gov/nice/ccw-events"

    def _button_more_info(self, pos:int = 0) -> dict[str, str]:
        '''
        The method extract description and url of event. Each event have a button of more info. 

        Args:
            pos(int) default 0, position of the event in the table

        Return:
            Description(str)
            url(str)
        '''

        # Si aparece popup cliclarlo 

        # Si pertenece a la pagina de NIST. Entonces:
        #   Extraer description y url
        # En caso de no ser de la pagina NIST. Entonces:
        #   Extraer directamente el contenido de la pagina y asignar la url del sitio web

        return {}

    def _is_disabled_button_next(self) -> bool:
        '''
        Return:
            True: button next is disabled.
            False: button next is not disabled.
        '''
        disabled_button_next = ".paginate_button.next.disabled"
        return ScrapUtils.if_element_exists(self.driver, By.CSS_SELECTOR, disabled_button_next) # type: ignore
    
    def _get_max_num_events_of_page(self) -> int:
        '''
        Give maximum number of events on a page.

        '''
        elem_show_line = self.driver.find_element(By.CLASS_NAME, "dataTables_info").text
        show_line_str = elem_show_line.split()
        return int(show_line_str[3])

    def scrap_events_cybersegurity(self, from_days_ago: int = 0) -> list[ScrapedEventsModel]:
        '''
        Access the cybersegurity section of the NIST website and extract information of events.
        
        Args:
            from_days_ago (int): The number of days to get the information of all events by default is 0

        Raise:
            ValueError: if from_days_ago is less than 0.
        
        Returns:
            list[ScrapedEventsModel]: all events of website
        '''
        logger.info(f"Getting events from {from_days_ago} days ago")

        if from_days_ago < 1:
            logger.error("from_days_ago must be greater than 0")
            raise ValueError("from_days_ago must be greater than 0")

        self.driver.get(self.url_cybersegurity)

        while(self._is_disabled_button_next() == False):
            elems_table = self.driver.find_elements(By.CSS_SELECTOR, "tbody tr td")
            for pos in elems_table:
                # swicht pos 
                pass

        news_events: list[ScrapedEventsModel] = []



        return news_events
