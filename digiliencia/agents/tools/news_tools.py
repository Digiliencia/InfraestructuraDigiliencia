from typing import List, Optional

from digiliencia.data.services.neomodel.news_service import NewsService
from digiliencia.enums.related_fields import is_valid_related_field
from digiliencia.enums.topics import Topics


def get_news(
    limit: int = 10,
    topic: Optional[str] = None,
    related_field: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    organization: Optional[str] = None,
) -> str:
    """
    Retrieves news from the database based on various filters.
    
    This is a wrapper function compatible with llama-index FunctionTool.
    Returns a formatted string with news information instead of News objects.

    Args:
        limit: Maximum number of news items to retrieve (default: 10, max: 50).
        topic: Filter by a specific topic name (e.g., "Cybersecurity", "AI").
        related_field: Filter by a specific related field name.
        start_date: Start date for filtering news in format YYYY-MM-DD (inclusive).
        end_date: End date for filtering news in format YYYY-MM-DD (inclusive).
        organization: Filter by organization name.

    Returns:
        Formatted string with news information including titles, dates, URLs, and summaries.
    """
    # Validate and limit
    limit = min(limit, 50)  # Prevent excessive results
    
    # Convert string parameters to enum types if provided
    topic_enum = None
    if topic:
        try:
            # Try to find matching topic enum
            for topic_item in Topics:
                if topic_item.value.lower() == topic.lower() or topic_item.name.lower() == topic.lower():
                    topic_enum = topic_item
                    break
        except Exception:
            pass  # If no match, topic_enum stays None
    
    # For related_field, pass the string directly - NewsService will handle it
    # Just validate it exists
    validated_field = None
    if related_field and is_valid_related_field(related_field):
        validated_field = related_field
    
    news_service = NewsService()
    
    # Call the service with proper types
    # We'll pass related_field as the raw string since NewsService expects it
    try:
        news_results = news_service.get(
            limit=limit,
            topic=topic_enum,
            related_field=validated_field,  # type: ignore
            start_date=start_date,
            end_date=end_date,
            organization=organization,
        )
    except Exception as e:
        return f"Error retrieving news: {str(e)}"
    
    # Format results as string for LLM consumption
    return _format_news_results(news_results)


def search_by_content(
    content: str,
    limit: int = 10,   
) -> str:
    """
    Searches for news items containing similar content using embeddings.
    
    This is a wrapper function compatible with llama-index FunctionTool.
    Returns a formatted string with news information instead of News objects.

    Args:
        content: The content to search for within news items.
        limit: Maximum number of news items to retrieve (default: 10, max: 50).

    Returns:
        Formatted string with news information including titles, dates, URLs, and summaries.
    """
    # Validate and limit
    limit = min(limit, 50)  # Prevent excessive results
    
    news_service = NewsService()
    
    try:
        news_results = news_service.search_by_content(content=content, limit=limit)
    except Exception as e:
        return f"Error searching news: {str(e)}"
    
    # Format results as string for LLM consumption
    return _format_news_results(news_results)


def _format_news_results(news_results: List) -> str:
    """
    Format news results as a structured string for LLM consumption.
    
    Args:
        news_results: List of News objects
        
    Returns:
        Formatted string with news information
    """
    if not news_results:
        return "No news found matching the criteria."
    
    formatted = f"Found {len(news_results)} news articles:\n\n"
    
    for i, news in enumerate(news_results, 1):
        # Access properties as strings (neomodel StringProperty)
        header = str(news.header) if hasattr(news, 'header') else "No title"
        date = str(news.date) if hasattr(news, 'date') else "No date"
        url = str(news.url) if hasattr(news, 'url') else "No URL"
        
        formatted += f"{i}. {header}\n"
        formatted += f"   Date: {date}\n"
        formatted += f"   URL: {url}\n"
        
        # Add content preview (first 200 chars)
        if hasattr(news, 'content') and news.content:
            content_str = str(news.content)
            formatted += f"   Content: {content_str}\n"
        
        # Add metadata if available
        metadata_parts = []
        
        # Try to get agency from relationship
        try:
            if hasattr(news, 'published_by'):
                agency = news.published_by.single()
                if agency and hasattr(agency, 'name'):
                    metadata_parts.append(f"Agency: {agency.name}")
        except Exception:
            pass
        
        # Try to get topics from relationship
        try:
            if hasattr(news, 'topics'):
                topics = news.topics.all()
                if topics:
                    topic_names = [str(t.name) for t in topics if hasattr(t, 'name')]
                    if topic_names:
                        metadata_parts.append(f"Topics: {', '.join(topic_names)}")
        except Exception:
            pass
        
        # Try to get fields from relationship
        try:
            if hasattr(news, 'fields'):
                fields = news.fields.all()
                if fields:
                    field_names = [str(f.name) for f in fields if hasattr(f, 'name')]
                    if field_names:
                        metadata_parts.append(f"Fields: {', '.join(field_names)}")
        except Exception:
            pass
        
        if metadata_parts:
            formatted += f"   {' | '.join(metadata_parts)}\n"
        
        formatted += "\n"
    
    return formatted