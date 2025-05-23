# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 10:08:33 2025

@author: Carlos Prieto
Web scrapping: https://www.nist.gov/nice/ccw-events
"""

from digiliencia.data.scrapping.abc_scraper import AbstractScraper
from digiliencia.data.models.events_model import ScrapedEventsModel
from digiliencia.utils.scrap import ScrapUtils

class Nist(AbstractScraper):
    def __init__(self):
        self.driver = ScrapUtils.get_driver()

    def _button_more_info(self, pos:int = 0) -> list[str, str]:
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

        return ['', '']

    def scrap_events(self, from_days_ago: int) -> list[ScrapedEventsModel]:
        '''
        Access the cybersegurity section of the NIST website and extract information of events.
        
        Args:
            from_days_ago (int): The number of days to get the information of all events

        Returns:
            list[ScrapedEventsModel]: all events of website
        '''
        pass
