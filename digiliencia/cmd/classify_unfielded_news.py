from loguru import logger

from digiliencia.data.services.neomodel.config import configure_neomodel
from digiliencia.data.services.neomodel.field.field_classification_service import (
    FieldClassificationService,
)
from digiliencia.data.services.neomodel.news_service import NewsService


def main():
    try:
        configure_neomodel()

        news_service = NewsService()
        field_class_service = FieldClassificationService()

        unlabeled_news = news_service.get_all_news_without_fields()
        logger.info(f"Found {len(unlabeled_news)} news without related fields")

        processed_count = 0

        for news in unlabeled_news:
            try:
                logger.info(
                    f"Processing news {processed_count + 1}/{len(unlabeled_news)}: {news.header}"
                )
                fields = field_class_service.classify_news_fields(news)
                if fields:
                    news_service.set_fields_relations(news, fields)
                    logger.info(
                        f"Classified news '{news.header}' into {len(fields)} fields"
                    )
                else:
                    logger.warning(f"No fields found for news '{news.header}'")
                processed_count += 1
            except Exception as e:
                logger.error(f"Error processing news '{news.header}': {e}")

        logger.success(f"Finished processing. Total processed: {processed_count}")

    except Exception as e:
        logger.exception(f"Fatal error running script: {e}")


if __name__ == "__main__":
    main()
