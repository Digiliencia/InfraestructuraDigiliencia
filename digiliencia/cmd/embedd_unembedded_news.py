from loguru import logger

from digiliencia.data.services.neomodel.config import configure_neomodel
from digiliencia.data.services.neomodel.news_service import NewsService


def main():
    try:
        configure_neomodel()

        news_service = NewsService()
        news_service.generate_embeddings_for_all_news()
    except Exception as e:
        logger.exception(f"Fatal error running script: {e}")


if __name__ == "__main__":
    main()
