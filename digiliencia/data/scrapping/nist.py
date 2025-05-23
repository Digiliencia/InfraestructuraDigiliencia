# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 10:08:33 2025

@author: Carlos Prieto
Web scrapping: https://www.nist.gov/nice/ccw-events
"""

from digiliencia.data.scrapping.abc_scraper import AbstractScraper
from digiliencia.data.models.news_model import ScrapedNewsModel
from digiliencia.utils.scrap import ScrapUtils
from loguru import logger
from digiliencia.utils.time import TimeUtils

class Nist(AbstractScraper):
    def __init__(self):
        self.driver = ScrapUtils.get_driver()

    def scrap_news(self, from_days_ago: int) #-> list[ScrapedNewsModel]:
        '''
        '''
        pass
