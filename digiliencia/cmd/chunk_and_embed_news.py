from loguru import logger

from digiliencia.configs.env import env
from digiliencia.data.services.neomodel.config import configure_neomodel
from digiliencia.data.services.neomodel.news_service import NewsService


def main():
    try:
        configure_neomodel()
        service = NewsService()
        processed = service.generate_chunks_for_all_news(
            limit=None,
            only_missing=True,
            chunk_size= env.news_chunk_size,
            overlap=env.news_chunk_overlap,
            include_header=True,
            batch_size=16,
        )
        logger.info(f"Processed news with chunking: {processed}")
    except Exception as e:
        logger.exception(f"Fatal error running chunking: {e}")


if __name__ == "__main__":
    main()
