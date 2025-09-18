from typing import Optional

from digiliencia.data.models.neomodel.news import News
from digiliencia.data.services.neomodel.news_service import NewsService
from digiliencia.enums.related_fields import RelatedFields
from digiliencia.enums.topics import Topics


def get_news(
    limit: int = 10,
    topic: Optional[Topics] = None,
    related_field: Optional[RelatedFields] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    organization: Optional[str] = None,
) -> list[News]:
    """
    Retrieves news from the database based on various filters.

    Args:
        limit (int): Maximum number of news items to retrieve.
        topic (Optional[Topics]): Filter by a specific topic.
        related_field (Optional[RelatedFields]): Filter by a specific related field.
        start_date (Optional[str]): Start date for filtering news (inclusive).
        end_date (Optional[str]): End date for filtering news (inclusive).
        organization (Optional[str]): Filter by organization name.

    Returns:
        List of news items matching the criteria.
    """

    news_service = NewsService()
    return news_service.get(
        limit=limit,
        topic=topic,
        related_field=related_field,
        start_date=start_date,
        end_date=end_date,
        organization=organization,
    )
