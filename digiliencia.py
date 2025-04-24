from loguru import logger
from digiliencia.cmd.scrap import scrap
from digiliencia.utils.env_loader import EnvLoader


def set_up_logging():
    logger.add("logs/execution.log", level="DEBUG")
    logger.add("logs/executionhistory.log", level="DEBUG", rotation="1 week")


if __name__ == "__main__":
    logger.info("Starting the application")
    set_up_logging()
    EnvLoader()
    scrap(5)