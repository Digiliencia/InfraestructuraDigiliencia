from digiliencia.data.scrapping.incibe import IncibeScraper
from digiliencia.data.scrapping.ncsc import Ncsc
from digiliencia.data.scrapping.weforum import WEForumScraper
from digiliencia.utils.env_loader import EnvLoader
from digiliencia.data.daos.news_dao import NewsDAO
from digiliencia.exc.dao_create_exc import DAOCreateError
from loguru import logger


def scrap(from_days_ago: int = 5):
    logger.info("Start scraping")
    EnvLoader()
    news_dao = NewsDAO()
    scrapers = [WEForumScraper, IncibeScraper, Ncsc]
    for scraper in scrapers:
        try:
            scraped_news = scraper().scrap_news(from_days_ago)
            for news in scraped_news:
                try:
                    news_dao.create_from_scrap(news)
                except DAOCreateError as e:
                    pass
        except Exception as e:
            logger.error(f"Error scraping with {scraper.__class__.__name__}: {e}")
    logger.info("Scraping finished")


if __name__ == "__main__":
    logger.info("Starting the application")
    EnvLoader()
    scrap()
