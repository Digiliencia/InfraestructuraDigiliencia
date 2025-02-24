from data.scrapping.weforum import WEForumScrapper
from utils.env_loader import EnvLoader
from loguru import logger

def set_up_logging():
    logger.add("logs/execution.log", level="DEBUG")
    logger.add("logs/executionhistory.log", level="DEBUG", rotation="1 week")


if __name__ == "__main__":
    logger.info("Starting the application")
    set_up_logging()
    
    EnvLoader()
    scrapper = WEForumScrapper()
    scrapper.scrap(51)