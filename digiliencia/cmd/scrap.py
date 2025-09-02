from typing import List

from loguru import logger

"""from digiliencia.configs.env import Env
from digiliencia.data.models.news_model import ScrapedNews

from configs.env import Env
from digiliencia.data.scrapping.cyber_canadian import CanadianScraper
from digiliencia.data.scrapping.incibe import IncibeScraper
from digiliencia.data.scrapping.ncsc import Ncsc
from digiliencia.data.scrapping.weforum import WEForumScraper
from digiliencia.data.services.neomodel.field.field_classification_service import (
    FieldClassificationService,
)
from digiliencia.data.services.neomodel.news_service import NewsService
from digiliencia.data.services.neomodel.topic.topic_classification_service import (
    TopicClassificationService,
)"""
from digiliencia.data.scrapping.america_cyber_agency import AmericaCyberAgencyScraper
from digiliencia.data.scrapping.cyber_canadian import CanadianScraper

def scrap(from_days_ago: int = 5):
    logger.info("Start scraping")
    # Nist().scrap_events(0)
    CanadianScraper().scrap_news(100)
    #AmericaCyberAgencyScraper().scrap_news(100)    
    """
    Env()

    news_service = NewsService()
    topics_class_service = TopicClassificationService()
    fields_class_service = FieldClassificationService()

    scrapers = [CanadianScraper, WEForumScraper, IncibeScraper, Ncsc]
    for scraper in scrapers:
        try:
            scraped_news: List[ScrapedNews] = scraper().scrap_news(from_days_ago)
            for news in scraped_news:
                try:
                    # Convert ScrapedNews to ScrapedNews for validation
                    validated_data = ScrapedNews(
                        header=news.header,
                        date=news.date,
                        source=news.source,
                        content=news.content,
                        url=news.url,
                        authors=news.authors,
                        topics=news.topics,
                    )
                    created_news = news_service.create_from_scraped_data(validated_data)

                    # Classify news into topics
                    topics = topics_class_service.classify_news_topics(created_news)
                    news_service.set_topics_relations(created_news, topics)
                    logger.info(
                        f"Classified news '{created_news.header}' into {len(topics)} topics"
                    )

                    # Classify news into fields
                    fields = fields_class_service.classify_news_fields(created_news)
                    news_service.set_fields_relations(created_news, fields)
                    logger.info(
                        f"Classified news '{created_news.header}' into {len(fields)} fields"
                    )

                except Exception as create_error:
                    logger.error(f"Error creating news: {create_error}")
        except Exception as e:
            logger.error(f"Error scraping with {scraper.__class__.__name__}: {e}")
    """
    logger.info("Scraping finished")


if __name__ == "__main__":
    logger.info("Starting the application")
    scrap(8)
