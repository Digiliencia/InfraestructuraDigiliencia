from loguru import logger

# from configs.env import Env
from digiliencia.data.scrapping.cyber_canadian import CanadianScraper
from digiliencia.data.scrapping.nist import Nist

def scrap(from_days_ago: int = 5):
    logger.info("Start scraping")
    # Nist().scrap_events(0)
    CanadianScraper().scrap_news(0)
    """
    Env()
    
    news_dao = NewsDAO()
    scrapers = [WEForumScraper, IncibeScraper]
    for scraper in scrapers:
        try:
            scraped_news: List[ScrapedNewsModel] = scraper().scrap_news(from_days_ago)
            for news in scraped_news:
                try:
                    news_dao.create_from_scrap(news)
                except DAOCreateError:
                    pass
        except Exception as e:
            logger.error(f"Error scraping with {scraper.__class__.__name__}: {e}")
    """
    logger.info("Scraping finished")


if __name__ == "__main__":
    logger.info("Starting the application")
    scrap()
