from loguru import logger

from digiliencia.data.scrapping.weforum import WEForumScraper


def scrap(from_days_ago: int = 365):
    logger.info("Start scraping")
    WEForumScraper().scrap_news(from_days_ago)
    """
    Env()
    news_service = NewsService()
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
                    news_service.create_from_scraped_data(validated_data)
                except Exception as create_error:
                    logger.error(f"Error creating news: {create_error}")
        except Exception as e:
            logger.error(f"Error scraping with {scraper.__class__.__name__}: {e}")
    """
    logger.info("Scraping finished")


if __name__ == "__main__":
    logger.info("Starting the application")
    scrap()
