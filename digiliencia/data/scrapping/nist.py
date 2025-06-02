# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 10:08:33 2025

@author: Carlos Prieto
Web scrapping: https://www.nist.gov/nice/ccw-events
"""
from datetime import datetime
from typing import Sequence
from digiliencia.data.models.news_model import ScrapedNewsModel
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
        ''' Give maximum number of events on a page '''
        elem_show_line = self.driver.find_element(By.CLASS_NAME, "dataTables_info").text
        show_line_str = elem_show_line.split()
        return int(show_line_str[3])
    
    def _get_all_events(self) -> int:
        ''' Give all events of website '''
        elem_show_line = self.driver.find_element(By.CLASS_NAME, "dataTables_info").text
        show_line_str = elem_show_line.split()
        return int(show_line_str[5])

    def scrap_events(self, from_days_ago: int = 0) -> list[ScrapedEventsModel]:
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

        if from_days_ago < 0:
            logger.error("from_days_ago must be greater than 0")
            raise ValueError("from_days_ago must be greater than 0")

        self.driver.get(self.url_cybersegurity)
        news_events: list[ScrapedEventsModel] = []       

        num_rows = self._get_max_num_events_of_page()

        logger.info(f"All Events to scarp website: {self._get_all_events()}")
        logger.info(f"Number of rows: {num_rows} of table")

        while(self._is_disabled_button_next() == False):

            tabla = self.driver.find_element(By.XPATH, '//table')
            filas = tabla.find_elements(By.TAG_NAME, 'tr')

            for fila in filas:
                elems_col = ['', '', '', '','', '', '']
                columnas = fila.find_elements(By.TAG_NAME, 'td')
                for index, col in enumerate(columnas):
                    if((index == 6) or (index == 7)): # More Info Button
                        self._button_more_info()
                    else:
                        elems_col[index] = col.text

                logger.debug(f"Scrap title: {elems_col[1]}")

                event:ScrapedEventsModel = ScrapedEventsModel(
                    type=elems_col[0],
                    header=elems_col[1],
                    organizer=elems_col[2],
                    date=datetime.now(), #datetime.strptime(elems_col[3], "%m/%d/%Y"),
                    location=elems_col[4],
                    address=elems_col[5],
                    description="",
                    url=""
                )
                news_events.append(event)
                elems_col.clear()

            if(self._is_disabled_button_next() == False):
                ScrapUtils.click_element(self.driver, ".paginate_button.next", 1)

        return news_events
    
    def scrap_news(self, from_days_ago: int) -> Sequence[ScrapedNewsModel]:
        return super().scrap_news(from_days_ago)
