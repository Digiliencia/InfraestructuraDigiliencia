from loguru import logger

from digiliencia.data.services.neomodel.config import configure_neomodel
from digiliencia.data.services.neomodel.news_service import NewsService
from digiliencia.configs.env import env


def main():
    try:
        configure_neomodel()

        news_service = NewsService()
        # 1) Crear chunks para noticias sin chunks
        created_news = news_service.generate_chunks_for_all_news(
            limit=None,
            only_missing=True,
            chunk_size=800,
            overlap=100,
            include_header=True,
            batch_size=30,
        )
        logger.info(f"News chunked: {created_news}")

        # 2) Generar embeddings para cada chunk sin embedding
        updated_chunks = news_service.generate_embeddings_for_missing_chunks(
            model_name=env.em,
            limit=None,
            batch_size=30,
        )
        logger.info(f"Chunks embedded: {updated_chunks}")
    except Exception as e:
        logger.exception(f"Fatal error running script: {e}")


if __name__ == "__main__":
    main()
