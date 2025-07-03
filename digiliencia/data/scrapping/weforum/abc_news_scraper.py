from abc import ABC, abstractmethod

from selenium.webdriver.chrome.webdriver import WebDriver

from digiliencia.data.models.news_model import ScrapedNews


class AbstractNewsScraper(ABC):
    def __init__(self, driver: WebDriver, load_time: int = 2):
        self.driver = driver
        self.load_time = load_time

    @abstractmethod
    def scrap(self, url: str) -> ScrapedNews:
        """
        Scraps the content of a single page.

        Parameters
        ----------
        url : str
            The URL of the page to be scraped.

        Returns
        -------
        ScrapedNews
            An instance of ScrapedNews containing the scraped data.
        """
        pass
