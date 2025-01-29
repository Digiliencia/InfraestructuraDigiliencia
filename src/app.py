from data.scrapping.incibe import IncibeScraper
from utils.env_loader import EnvLoader

EnvLoader()
scrapper = IncibeScraper()
scrapper.scrapper(10)