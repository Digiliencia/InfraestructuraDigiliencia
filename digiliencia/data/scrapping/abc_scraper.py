from abc import ABC, abstractmethod

from digiliencia.data.models.news_model import ScrapedNewsModel


class AbstractScraper(ABC):
    """
    Abstract base class for all scrapers

    This class defines the interface for scrapers.
    """

    @abstractmethod
    def scrap_news(self, from_days_ago: int) -> list[ScrapedNewsModel]:
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
