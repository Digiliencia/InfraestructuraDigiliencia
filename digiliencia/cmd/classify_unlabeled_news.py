from loguru import logger
from digiliencia.data.services.neomodel.config import configure_neomodel
from digiliencia.data.services.neomodel.news_service import NewsService
from digiliencia.data.services.neomodel.topic.topic_classification_service import (
    TopicClassificationService,
)


def main():
    try:
        configure_neomodel()

        news_service = NewsService()
        topic_class_service = TopicClassificationService()

        unlabeled_news = news_service.get_all_news_without_topics()
        logger.info(f"Found {len(unlabeled_news)} news without topics")

        processed_count = 0

        for news in unlabeled_news:
            try:
                topics = topic_class_service.classify_news_topics(news)
                if topics:
                    news_service.set_topics_relations(news, topics)
                    logger.info(
                        f"Classified news '{news.header}' into {len(topics)} topics"
                    )
                else:
                    logger.warning(f"No topics found for news '{news.header}'")
                processed_count += 1
            except Exception as e:
                logger.error(f"Error processing news '{news.header}': {e}")

        logger.success(f"Finished processing. Total processed: {processed_count}")

    except Exception as e:
        logger.exception(f"Fatal error running script: {e}")


if __name__ == "__main__":
    main()
