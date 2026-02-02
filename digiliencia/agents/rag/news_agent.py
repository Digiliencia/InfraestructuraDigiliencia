"""
News Agent implementation using llama-index.

This agent specializes in retrieving and presenting cybersecurity news
from the database using the available tools. It has access to shared memory
for conversation context across all agents.
"""

import asyncio
from typing import List, Optional

from llama_index.core import Settings, VectorStoreIndex
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool, QueryEngineTool
from llama_index.llms.ollama import Ollama
from llama_index.vector_stores.neo4jvector import Neo4jVectorStore
from loguru import logger

import digiliencia.agents.tools.news_tools as news_tools
from digiliencia.agents.base_agent import BaseAgent
from digiliencia.agents.prompts import NEWS_AGENT_SYSTEM_PROMPT
from digiliencia.agents.shared_memory import SharedConversationMemory
from digiliencia.configs.env import Env
from digiliencia.utils.embeddings import CustomAPIEmbedding


class NewsAgent(BaseAgent):
    """
    Specialized agent for handling news-related queries.

    This agent uses shared memory to maintain context with other agents
    in the system, enabling coherent multi-agent conversations.
    """

    def __init__(
        self,
        model_name: str,
        temperature: float = 0.0,  # Lower temperature for factual responses
        verbose: bool = True,
        shared_memory: Optional[SharedConversationMemory] = None,
    ):
        """
        Initialize the News Agent.

        Args:
            model_name: Name of the Ollama model to use
            temperature: LLM temperature (lower = more deterministic)
            verbose: Enable detailed logging
            shared_memory: Shared memory for cross-agent context
        """
        super().__init__(
            name="NewsAgent",
            description="Retrieves and presents cybersecurity news using database queries",
            model_name=model_name,
            temperature=temperature,
            verbose=True,
            shared_memory=shared_memory,
        )

        # Configure custom embeddings BEFORE initializing the agent
        # This prevents llama-index from trying to use OpenAI embeddings
        env = Env()
        embed_model = CustomAPIEmbedding(
            api_url=env.embeddings_service,
            embed_batch_size=16,
            timeout=60 * 7,
            embedding_dimension=env.embeddings_dimension,
            provider=env.embeddings_provider,
            model=env.embeddings_model,
        )

        # Configure Settings globally to prevent OpenAI fallback
        Settings.embed_model = embed_model
        Settings.llm = Ollama(
            model=model_name, temperature=temperature, request_timeout=7 * 60
        )

        logger.info(f"Configured custom embeddings API at: {Env().embeddings_service}")
        logger.info(f"Configured Ollama LLM: {model_name}")

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

        # Create the agent with tools
        llm = Ollama(
            model=self.model_name, temperature=self.temperature, request_timeout=7 * 60
        )
        agent = ReActAgent(
            tools=tools,
            llm=llm,
            verbose=True,
            max_iterations=15,
        )

        return agent

    def get_tools(self) -> List[FunctionTool]:
        """
        Get the news retrieval tools wrapped for llama-index.

        Returns:
            List of FunctionTool instances
        """
        # Create query engine tool for semantic search over news chunks
        query_engine = self._get_query_engine()
        query_engine_tool = QueryEngineTool.from_defaults(
            query_engine=query_engine,
            name="semantic_news_search",
            description=(
                "Performs semantic search over cybersecurity news articles. "
                "Returns relevant news chunks with full context including: "
                "news title, publication date, source agency, authors, topics, and related fields. "
                "Use this tool to find news articles related to specific cybersecurity concepts, "
                "technologies, threats, or events."
            ),
        )

        tools = [
            FunctionTool.from_defaults(fn=news_tools.get_news),
            query_engine_tool,
        ]

        return tools

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

        # Extract the response from the result
        # Handle different return formats from llama-index
        return self._extract_response_text(result)

    def _extract_response_text(self, result) -> str:
        """
        Extract only the final answer text from llama-index response.

        Filters out thinking/reasoning blocks to return only the user-facing response.
        Handles ChatMessage with multiple blocks (llama-index >= 0.14).
        """
        if isinstance(result, dict):
            return str(result.get("response", result))

        if hasattr(result, "response"):
            response = result.response
        else:
            response = result

        # Handle ChatMessage with blocks attribute (llama-index >= 0.14)
        if hasattr(response, "blocks"):
            text_parts = []
            for block in response.blocks:
                # Get block type - skip thinking/reasoning blocks
                block_type = getattr(block, "block_type", None)
                if block_type in ("thinking", "reasoning", "thought"):
                    continue  # Skip thinking blocks - only return final answer

                # Extract text from TextBlock or similar
                if hasattr(block, "text"):
                    text_parts.append(block.text)
                elif hasattr(block, "content") and isinstance(block.content, str):
                    text_parts.append(block.content)
                elif isinstance(block, str):
                    text_parts.append(block)

            return "\n".join(text_parts) if text_parts else "No response generated."

        # Handle content attribute
        if hasattr(response, "content"):
            content = response.content
            if isinstance(content, str):
                return content
            if hasattr(content, "blocks"):
                return self._extract_response_text(content)
            return str(content)

        # Handle message attribute (some llama-index versions)
        if hasattr(response, "message"):
            return self._extract_response_text(response.message)

        # Try to get text directly
        try:
            return str(response)
        except ValueError as e:
            if "multiple blocks" in str(e) and hasattr(response, "blocks"):
                return self._extract_response_text({"response": response})
            raise

    def process_query(self, query: str, **kwargs) -> str:
        """
        Process a news-related query using the ReAct agent with tools.

        The agent will automatically use the available tools (get_news, search_by_content)
        to retrieve real news data from the database before formulating a response.
        Multiple tool calls may be made if needed to fully answer the query.

        Uses shared memory to provide conversation context.

        Args:
            query: User's news query
            **kwargs: Additional parameters

        Returns:
            Agent's response based on retrieved news from tools
        """
        try:
            logger.info(f"NewsAgent processing query with tools: {query[:100]}...")

            # Get conversation context from shared memory
            context = self.get_conversation_context()

            # Enhance query with context if available
            if context != "No previous conversation context.":
                enhanced_query = f"""
Conversation context for reference:
{context}

Current query: {query}

Please answer the current query, using the conversation context if it helps provide a more relevant response.
If the user refers to something from the conversation history, acknowledge it."""
            else:
                enhanced_query = query

            # Run the async query processing synchronously
            try:
                # Try to get existing event loop
                loop = asyncio.get_event_loop()
                if loop.is_running():
                    # If loop is running (e.g., in Streamlit), use nest_asyncio
                    import nest_asyncio

                    nest_asyncio.apply()
                    response = loop.run_until_complete(
                        self._async_process_query(enhanced_query)
                    )
                else:
                    response = loop.run_until_complete(
                        self._async_process_query(enhanced_query)
                    )
            except RuntimeError:
                # No event loop exists, create a new one
                response = asyncio.run(self._async_process_query(enhanced_query))

            # Add response to shared memory
            self._shared_memory.add_assistant_message(
                str(response), agent_name=self.name
            )

            self.record_query(success=True)
            logger.debug("NewsAgent query processed successfully with tools")

            return str(response)

        except Exception as e:
            logger.error(f"Error in NewsAgent.process_query: {e}")
            self.record_query(success=False)

            error_response = (
                f"I encountered an error while retrieving news: {str(e)}. "
                "Please try rephrasing your query or contact support if the issue persists."
            )
            self._shared_memory.add_assistant_message(
                error_response, agent_name=self.name
            )
            return error_response

    def reset_conversation(self):
        """Reset the agent's conversation state."""
        # Reinitialize the agent
        self._agent = self._initialize_agent()
        logger.debug("NewsAgent conversation reset")

    def _get_query_engine(self):
        if not hasattr(self, "_query_engine"):
            # Custom Cypher query to retrieve chunk with full news context
            retrieval_query = """
            MATCH (chunk:Chunk)<-[:HAS_CHUNK]-(news:News)
            OPTIONAL MATCH (news)-[:PUBLISHED_BY]->(agency:NewsAgency)
            OPTIONAL MATCH (news)-[:WRITTEN_BY]->(author:Author)
            OPTIONAL MATCH (news)-[:COVERS]->(topic:Topic)
            OPTIONAL MATCH (news)-[:RELATED_TO]->(field:Field)
            WITH chunk, news, agency, 
                 collect(DISTINCT author.name) AS authors,
                 collect(DISTINCT topic.name) AS topics,
                 collect(DISTINCT field.name) AS fields,
                 score
            RETURN 
                chunk.text AS text,
                score,
                chunk.uid AS id,
                {
                    _node_type: labels(chunk)[0],
                    _node_content: chunk.text,
                    chunk_index: chunk.index,
                    chunk_kind: chunk.kind,
                    news_uid: news.uid,
                    news_header: news.header,
                    news_date: toString(news.date),
                    news_url: news.url,
                    news_content_preview: substring(news.content, 0, 200),
                    agency_name: agency.name,
                    authors: authors,
                    topics: topics,
                    fields: fields
                } AS metadata
            """

            store = Neo4jVectorStore(
                username=Env().neo4j_username,
                password=Env().neo4j_password,
                url=Env().neo4j_url,
                embedding_dimension=Env().embeddings_dimension,
                index_name="chunk_embedding_idx",
                hybrid_search=True,
                retrieval_query=retrieval_query,
            )

            # Create VectorStoreIndex - will use Settings.embed_model configured in __init__
            self._query_engine = VectorStoreIndex.from_vector_store(
                store
            ).as_query_engine()

        return self._query_engine
