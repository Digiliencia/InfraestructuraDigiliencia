from abc import ABC, abstractmethod

class AbstractScraper(ABC):
    """
    Abstract base class for all scrapers
    
    This class defines the interface for scrapers.
    """
    
    @abstractmethod
    def scrap(self, from_days_ago: int) -> tuple[dict[str, str]]:
        """
        Scraps the class content from from_days_ago days ago.
        
        Parameters
        ----------
        from_days_ago : int
            The number of days ago from which to start the scraping.
        
        Returns
        -------
        tuple[dict[str, str]]
            A tuple containing the scraped data.
        """
        pass