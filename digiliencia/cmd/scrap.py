from typing import List

# from digiliencia.configs.env import Env
from digiliencia.data.models.news_model import ScrapedNewsModel

# from digiliencia.data.scrapping.incibe import IncibeScraper
# from digiliencia.data.scrapping.ncsc import Ncsc
from digiliencia.data.scrapping.weforum import WEForumScraper
from digiliencia.exc.dao_create_exc import DAOCreateError


def scrap(from_days_ago: int = 5):
    logger.info("Start scraping")
    # Env()
    # news_dao = NewsDAO()
    scrapers = [WEForumScraper]  # , IncibeScraper, Ncsc]
    for scraper in scrapers:
        try:
            scraped_news: List[ScrapedNews] = scraper().scrap_news(from_days_ago)
            for news in scraped_news:
                try:
                    # news_dao.create_from_scrap(news)
                    print("LLEGO ", news)
                except DAOCreateError:
                    pass
        except Exception as e:
            logger.error(f"Error scraping with {scraper.__class__.__name__}: {e}")
    logger.info("Scraping finished")


if __name__ == "__main__":
    logger.info("Starting the application")
    scrap(8)
