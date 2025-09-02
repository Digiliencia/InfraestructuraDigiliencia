import sys

from loguru import logger

from digiliencia.cmd.scrap import scrap
#from digiliencia.configs.env import Env


def set_up_logging():
    logger.remove()
    logger.add(sys.stdout, level="INFO")
    logger.add("logs/execution.log", level="INFO")
    logger.add("logs/executionhistory.log", level="INFO", rotation="1 week")


if __name__ == "__main__":
    logger.info("Starting the application")
    #set_up_logging()
    #Env()
    scrap(1)
