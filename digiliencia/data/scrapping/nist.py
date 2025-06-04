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
from selenium.webdriver.remote.webelement import WebElement
from digiliencia.exc.nist_exec import NistExec
import time

class Nist(AbstractScraper):
    '''Scraps only the events of NIST'''

    def __init__(self):
        logger.debug("Initializing NIST")
        self.driver = ScrapUtils.get_driver()
        self.url_cybersegurity = "https://www.nist.gov/nice/ccw-events"
        self.load_time = 1

    def _button_more_info(self, col: WebElement) -> dict[str, str]:
        '''
        The method extract description and url of event. Each event have a button of more info. 

        Args:
            col

        Return:
            Description(str)
            url(str)
        '''
        try:        
            if(ScrapUtils.if_element_exists(col, By.TAG_NAME, 'a')):  # type: ignore
                col.find_element(By.TAG_NAME, 'a').click() # Click button 'more info'
                if("https://www.nist.gov/nice/ccw-events/" in self.driver.current_url):
                    url = self.driver.current_url
                    description = self.driver.find_element(By.CSS_SELECTOR, "div.views-field.views-field-webform-submission-value-1 span.field-content").text

                    self.driver.back()
                    return {"description":description, "url":url} 
                else:
                    self.driver.back()
                    return {"description":"", "url":""}
            else:
                return {"description":"", "url":""}
        except NistExec as e:
            logger.warning("")
            return {"description":"", "url":""}

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

            for fila in filas[1:]:
                elems_col = ['', '', '', '','', '', '', '']
                columnas = fila.find_elements(By.TAG_NAME, 'td')
                for index, col in enumerate(columnas):
                    if((index == 6)): # More Info Button
                        more_info = self._button_more_info(col)
                        elems_col[index] = more_info["description"]
                        elems_col[index+1] = more_info["url"]
                        time.sleep(self.load_time)
                    else:
                        elems_col[index] = col.text

                event:ScrapedEventsModel = ScrapedEventsModel(
                    type=elems_col[0],
                    header=elems_col[1],
                    organizer=elems_col[2],
                    date=datetime.strptime(elems_col[3], "%m/%d/%Y"),
                    location=elems_col[4],
                    address=elems_col[5],
                    description=elems_col[6],
                    url=elems_col[7]
                )
                news_events.append(event)
                elems_col.clear()

            if(self._is_disabled_button_next() == False):
                ScrapUtils.click_element(self.driver, ".paginate_button.next", 1)

        logger.debug(f"Number of eventes extract data: {len(news_events)}")

        return news_events
    
    def scrap_news(self, from_days_ago: int) -> Sequence[ScrapedNewsModel]:
        return super().scrap_news(from_days_ago)