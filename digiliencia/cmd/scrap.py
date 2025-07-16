from typing import List

from loguru import logger

from digiliencia.configs.env import Env
from digiliencia.data.models.news_model import ScrapedNews
from digiliencia.data.scrapping.incibe import IncibeScraper
from digiliencia.data.scrapping.ncsc import Ncsc
from digiliencia.data.scrapping.weforum import WEForumScraper
from digiliencia.data.services.neomodel.news_service import NewsService
from digiliencia.data.services.neomodel.topic.topic_classification_service import \
    TopicClassificationService


def scrap(from_days_ago: int = 5):
    logger.info("Start scraping")
    Env()
    news_service = NewsService()
    topics_class_service = TopicClassificationService()

    scrapers = [WEForumScraper, IncibeScraper, Ncsc]
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

                    # Only classify if service is healthy
                    if True:
                        topics = topics_class_service.classify_news_topics(created_news)
                        news_service.set_topics_relations(created_news, topics)
                        logger.info(
                            f"Classified news '{created_news.header}' into {len(topics)} topics"
                        )
                    else:
                        logger.warning(
                            f"Classification service is not healthy, skipping topic classification for news '{created_news.header}'"
                        )

                except Exception as create_error:
                    logger.error(f"Error creating news: {create_error}")
        except Exception as e:
            logger.error(f"Error scraping with {scraper.__class__.__name__}: {e}")
    logger.info("Scraping finished")


if __name__ == "__main__":
    logger.info("Starting the application")
    scrap()
