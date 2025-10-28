"""
News Agent implementation using llama-index.

This agent specializes in retrieving and presenting cybersecurity news
from the database using the available tools.
"""

import asyncio
from typing import List, Optional

from llama_index.core.agent.workflow import ReActAgent
from llama_index.core.tools import FunctionTool
from loguru import logger

from digiliencia.agents.base_agent import ToolBasedAgent
from digiliencia.agents.prompts import NEWS_AGENT_SYSTEM_PROMPT
from digiliencia.agents.tools.news_tools import get_news, search_by_content
from digiliencia.data.models.neomodel.news import News
from digiliencia.enums.related_fields import RelatedFields
from digiliencia.enums.topics import Topics


class NewsAgent(ToolBasedAgent):
    """
    Specialized agent for handling news-related queries.
    
    This agent ALWAYS uses the provided tools to retrieve real news data
    from the database. It never generates fake or hallucinated information.
    """
    
    def __init__(
        self,
        model_name: str = "llama3.1:8b",
        temperature: float = 0.3,  # Lower temperature for factual responses
        verbose: bool = False,
    ):
        """
        Initialize the News Agent.
        
        Args:
            model_name: Name of the Ollama model to use
            temperature: LLM temperature (lower = more deterministic)
            verbose: Enable detailed logging
        """
        super().__init__(
            name="NewsAgent",
            description="Retrieves and presents cybersecurity news using database queries",
            model_name=model_name,
            temperature=temperature,
            verbose=verbose,
        )
        
        # Initialize llama-index agent with tools
        self._agent = self._initialize_agent()
        
        logger.info("NewsAgent initialized with ReAct agent and tools")
    
    def _initialize_agent(self) -> ReActAgent:
        """
        Initialize the ReAct agent with news retrieval tools.
        
        The agent is configured to ALWAYS use tools for answering queries,
        ensuring factual, database-backed responses.
        
        Returns:
            Configured ReActAgent instance
        """
        tools = self.get_tools()
        
        # Enhanced system prompt to enforce tool usage
        system_prompt = (
            f"{self.get_system_prompt()}\n\n"
            "CRITICAL INSTRUCTION: You MUST use the available tools to answer every query. "
            "Do NOT provide answers without using tools first. "
            "If you don't have enough information after using tools, ask the user for clarification "
            "or suggest refining their query. "
            "NEVER generate or invent information that doesn't come from the tools."
        )
        
        # Create the agent with tools
        agent = ReActAgent(
            name="NewsAgent",
            description="Retrieves and presents cybersecurity news using database queries",
            system_prompt=system_prompt,
            tools=tools,
            llm=self._llm,
            verbose=self.verbose,
            timeout=self.request_timeout,
        )
        
        return agent
    
    def get_tools(self) -> List[FunctionTool]:
        """
        Get the news retrieval tools wrapped for llama-index.
        
        Returns:
            List of FunctionTool instances
        """
        # Wrap the get_news function
        get_news_tool = FunctionTool.from_defaults(
            fn=self._get_news_wrapper,
            name="get_news",
            description=(
                "Retrieves cybersecurity news from the database with optional filters. "
                "Use this tool to get news articles based on specific criteria. "
                "Parameters: "
                "- limit (int): Maximum number of news items (default 10, max 50) "
                "- topic (str): Filter by topic (e.g., 'RANSOMWARE', 'PHISHING', 'VULNERABILITIES') "
                "- related_field (str): Filter by field (e.g., 'HEALTHCARE', 'FINANCE', 'GOVERNMENT') "
                "- start_date (str): Start date in YYYY-MM-DD format "
                "- end_date (str): End date in YYYY-MM-DD format "
                "- organization (str): Filter by organization name "
                "Returns: List of news articles with title, content, date, and metadata"
            ),
        )
        
        # Wrap the search_by_content function
        search_content_tool = FunctionTool.from_defaults(
            fn=self._search_by_content_wrapper,
            name="search_by_content",
            description=(
                "Searches for news using semantic similarity to the provided content. "
                "Use this tool when you need to find news related to specific concepts, "
                "keywords, or descriptions. This uses embeddings for intelligent matching. "
                "Parameters: "
                "- content (str): The text to search for (e.g., 'zero-day exploits in browsers') "
                "- limit (int): Maximum number of results (default 10, max 50) "
                "Returns: List of news articles semantically similar to the search content"
            ),
        )
        
        return [get_news_tool, search_content_tool]
    
    def _get_news_wrapper(
        self,
        limit: int = 10,
        topic: Optional[str] = None,
        related_field: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        organization: Optional[str] = None,
    ) -> str:
        """
        Wrapper for get_news that returns formatted string results.
        
        Args:
            limit: Maximum number of news items
            topic: Filter by topic
            related_field: Filter by related field
            start_date: Start date (YYYY-MM-DD)
            end_date: End date (YYYY-MM-DD)
            organization: Organization name
            
        Returns:
            Formatted string with news results
        """
        try:
            # Convert string to enum values
            topic_enum = self._parse_enum(topic, Topics) if topic else None
            field_enum = self._parse_enum(related_field, RelatedFields) if related_field else None
            
            # Ensure limit is reasonable
            limit = min(max(1, limit), 50)
            
            news_list = get_news(
                limit=limit,
                topic=topic_enum,
                related_field=field_enum,
                start_date=start_date,
                end_date=end_date,
                organization=organization,
            )
            
            return self._format_news_results(news_list)
            
        except Exception as e:
            logger.error(f"Error in get_news_wrapper: {e}")
            return f"Error retrieving news: {str(e)}"
    
    def _parse_enum(self, value: str, enum_class):
        """
        Parse string value to enum instance.
        
        Args:
            value: String value to parse
            enum_class: Enum class to parse into
            
        Returns:
            Enum instance or None
        """
        if not value:
            return None
        
        # Try to get enum by name
        try:
            return getattr(enum_class, value.upper())
        except AttributeError:
            pass
        
        # Try to match by value
        for item in enum_class:
            if hasattr(item, 'value') and item.value.upper() == value.upper():
                return item
        
        return None
    
    def _search_by_content_wrapper(
        self,
        content: str,
        limit: int = 10,
    ) -> str:
        """
        Wrapper for search_by_content that returns formatted string results.
        
        Args:
            content: Search query text
            limit: Maximum number of results
            
        Returns:
            Formatted string with search results
        """
        try:
            # Ensure limit is reasonable
            limit = min(max(1, limit), 50)
            
            news_list = search_by_content(content=content, limit=limit)
            
            return self._format_news_results(news_list)
            
        except Exception as e:
            logger.error(f"Error in search_by_content_wrapper: {e}")
            return f"Error searching news: {str(e)}"
    
    def _format_news_results(self, news_list: List[News]) -> str:
        """
        Format news results into a readable string.
        
        Args:
            news_list: List of News objects
            
        Returns:
            Formatted string representation
        """
        if not news_list:
            return "No news articles found matching the criteria."
        
        result_parts = [f"Found {len(news_list)} news article(s):\n"]
        
        for idx, news in enumerate(news_list, 1):
            result_parts.append(f"\n--- Article {idx} ---")
            
            # Use 'header' instead of 'title' (correct attribute name in News model)
            if hasattr(news, 'header'):
                result_parts.append(f"Title: {news.header}")
            
            if hasattr(news, 'date'):
                result_parts.append(f"Date: {news.date}")
            
            # Get organization from relationship (published_by)
            try:
                # Access the relationship and get the single connected node
                org_rel = getattr(news, 'published_by', None)
                if org_rel:
                    org = org_rel.single()
                    if org and hasattr(org, 'name'):
                        result_parts.append(f"Organization: {org.name}")
            except Exception as e:
                logger.debug(f"Could not retrieve organization: {e}")
            
            # Get topics from relationship
            try:
                topics_rel = getattr(news, 'topics', None)
                if topics_rel:
                    topics = list(topics_rel.all())
                    if topics:
                        topic_names = [getattr(t, 'name', str(t)) for t in topics]
                        result_parts.append(f"Topics: {', '.join(topic_names)}")
            except Exception as e:
                logger.debug(f"Could not retrieve topics: {e}")
            
            # Get related fields from relationship
            try:
                fields_rel = getattr(news, 'fields', None)
                if fields_rel:
                    fields = list(fields_rel.all())
                    if fields:
                        field_names = [getattr(f, 'name', str(f)) for f in fields]
                        result_parts.append(f"Related Fields: {', '.join(field_names)}")
            except Exception as e:
                logger.debug(f"Could not retrieve fields: {e}")
            
            # Truncate content if too long
            if hasattr(news, 'content'):
                content_str = str(news.content)
                if len(content_str) > 500:
                    content_str = content_str[:500] + "..."
                result_parts.append(f"Content: {content_str}")
            
            if hasattr(news, 'url') and news.url:
                result_parts.append(f"URL: {news.url}")
        
        return "\n".join(result_parts)
    
    def get_system_prompt(self) -> str:
        """
        Get the system prompt for the News Agent.
        
        Returns:
            System prompt string
        """
        return NEWS_AGENT_SYSTEM_PROMPT
    
    async def _async_process_query(self, query: str) -> str:
        """
        Async helper to process query with the agent.
        
        The agent will use its tools to retrieve real news data before responding.
        
        Args:
            query: User's news query
            
        Returns:
            Agent's response based on tool-retrieved data
        """
        # Run the agent with the user query
        # The system prompt is already configured in the agent initialization
        handler = self._agent.run(user_msg=query)
        result = await handler
        
        # The result is a Context object, extract the response
        # Check different possible return formats
        if isinstance(result, dict):
            # If it's a dict, try to get 'response' key
            return str(result.get("response", result))
        elif hasattr(result, "response"):
            # If it has a 'response' attribute
            return str(result.response)
        else:
            # Otherwise, convert the whole result to string
            return str(result)
    
    def process_query(self, query: str, **kwargs) -> str:
        """
        Process a news-related query using the ReAct agent with tools.
        
        The agent will automatically use the available tools (get_news, search_by_content)
        to retrieve real news data from the database before formulating a response.
        Multiple tool calls may be made if needed to fully answer the query.
        
        Args:
            query: User's news query
            **kwargs: Additional parameters
            
        Returns:
            Agent's response based on retrieved news from tools
        """
        try:
            logger.info(f"NewsAgent processing query with tools: {query[:100]}...")
            
            # Run the async query processing synchronously
            try:
                # Try to get existing event loop
                loop = asyncio.get_event_loop()
                if loop.is_running():
                    # If loop is running (e.g., in Streamlit), use nest_asyncio
                    import nest_asyncio
                    nest_asyncio.apply()
                    response = loop.run_until_complete(self._async_process_query(query))
                else:
                    response = loop.run_until_complete(self._async_process_query(query))
            except RuntimeError:
                # No event loop exists, create a new one
                response = asyncio.run(self._async_process_query(query))
            
            self.record_query(success=True)
            logger.debug("NewsAgent query processed successfully with tools")
            
            return str(response)
            
        except Exception as e:
            logger.error(f"Error in NewsAgent.process_query: {e}")
            self.record_query(success=False)
            
            return (
                f"I encountered an error while retrieving news: {str(e)}. "
                "Please try rephrasing your query or contact support if the issue persists."
            )
    
    def reset_conversation(self):
        """Reset the agent's conversation state."""
        # Reinitialize the agent
        self._agent = self._initialize_agent()
        logger.debug("NewsAgent conversation reset")
