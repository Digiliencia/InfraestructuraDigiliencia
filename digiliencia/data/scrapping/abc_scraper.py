from abc import ABC, abstractmethod
from typing import Sequence

from digiliencia.data.models.news_model import ScrapedNewsModel
from digiliencia.data.models.events_model import ScrapedEventsModel


class AbstractScraper(ABC):
    """
    Abstract base class for all scrapers

    This class defines the interface for scrapers.
    """

    @abstractmethod
    def scrap_news(self, from_days_ago: int) -> Sequence[ScrapedNews]:
        """
        Scraps the class content from from_days_ago days ago.

        Parameters
        ----------
        from_days_ago : int
            The number of days ago from which to start the scraping.

        Returns
        -------
        tuple[ScrapedNewsModel]
            A tuple containing ScrapedNewsModels with the scraped data.
        """
        pass

    @abstractmethod
    def scrap_events_cybersegurity(self, from_days_ago: int) -> Sequence[ScrapedEventsModel]:
        """
        Scraps the events content from from_days_ago days ago.

        Parameters
        ----------
        from_days_ago : int
            The number of days ago from which to start the scraping.

        Returns
        -------
        tuple[ScrapedEventsModel]
            A tuple containing ScrapedEventsModel with the scraped data.
        """
        pass
