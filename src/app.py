from data.scrapping.weforum import WEForumScrapper
from utils.env_loader import EnvLoader

EnvLoader()
scrapper = WEForumScrapper()
scrapper.scrap(25)