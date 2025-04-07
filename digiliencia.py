from loguru import logger

from digiliencia.data.scrapping.incibe import IncibeScraper
from digiliencia.data.scrapping.ncsc import Ncsc
from digiliencia.data.scrapping.weforum import WEForumScraper
from digiliencia.utils.env_loader import EnvLoader


def set_up_logging():
    logger.add("logs/execution.log", level="DEBUG")
    logger.add("logs/executionhistory.log", level="DEBUG", rotation="1 week")


if __name__ == "__main__":
    logger.info("Starting the application")
    set_up_logging()
    EnvLoader()
    # DBConnection().connect()
    #WEForumScraper().scrap_news(from_days_ago=1)
    #IncibeScraper().scrap_news(from_days_ago=1)
    Ncsc().scrap_news(from_days_ago=5)