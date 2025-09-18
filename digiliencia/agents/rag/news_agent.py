import asyncio
import time
from enum import Enum
from typing import Dict, List, Optional, Union

from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.core.tools import FunctionTool
from loguru import logger

from digiliencia.agents.base_agent import BaseAgent
from digiliencia.agents.tools import news_tools


class QueryType(Enum):
    """Types of queries that can be handled."""
    SIMPLE_SEARCH = "simple_search"
    COMPLEX_ANALYSIS = "complex_analysis"
    RELATIONSHIP_EXPLORATION = "relationship_exploration"
    MEDICAL_LOOKUP = "medical_lookup"
    GENERAL_QUESTION = "general_question"


class NewsAgent(BaseAgent):
    """
    Modern agent that leverages native LLM tool calling capabilities.
    Uses LLM-based decisions for tool usage instead of hardcoded patterns.
    """

    def __init__(
        self,
        model_name: str,
        tools: Optional[List[FunctionTool]] = None,
        temperature: float = 0,
        verbose: bool = False,
        max_iterations: int = 5,
        timeout_seconds: int = 180,
    ):
        super().__init__(
            model_name=model_name,
            tools=tools,
            temperature=temperature,
            verbose=verbose,
            timeout_seconds=timeout_seconds,
        )
        self.max_iterations = max_iterations

        # Load tools if not provided
        if not tools:
            self.tools = self._load_news_tools()
            logger.info(f"Loaded {len(self.tools)} tools from news_tools module")
        else:
            logger.info(f"Using {len(self.tools)} provided tools")

        # Setup function-calling agent
        self._setup_agent_worker()

    def _load_news_tools(self) -> List[FunctionTool]:
        """Load all available tools from the news_tools module."""
        tools = []
        tool_functions = [
            attr for attr in dir(news_tools)
            if callable(getattr(news_tools, attr)) and not attr.startswith("_")
        ]
        for func_name in tool_functions:
            try:
                func = getattr(news_tools, func_name)
                tool = FunctionTool.from_defaults(fn=func)
                tools.append(tool)
                logger.debug(f"Loaded tool: {func_name}")
            except Exception as e:
                logger.warning(f"Failed to load tool {func_name}: {e}")
        return tools

    def _setup_agent_worker(self):
        """Setup the function calling agent worker."""
        try:
            self.agent_workflow = AgentWorkflow.from_tools_or_functions(
                tools_or_functions=[tool for tool in self.tools],
                llm=self.llm,
                system_prompt="You are a function-calling medical assistant.",
                verbose=self.verbose,
                timeout=self.timeout_seconds,
            )
            self.agent = self.agent_workflow
            logger.info(
                f"Function calling agent successfully initialized with max_iterations={self.max_iterations}"
            )
        except Exception as e:
            logger.error(f"Failed to setup AgentWorkflow: {e}")
            self.agent_workflow = None
            self.agent = None
            logger.warning("Falling back to simple mode without function calling")

    def _should_use_tools(self, message: str) -> bool:
        """Ask the LLM if tools are required."""
        logger.debug("Using LLM to determine if tools are needed")
        tool_decision_prompt = f"""
        Decide if this query requires medical tools:
        "{message}"

        Respond with only YES or NO.
        """
        try:
            response = self.llm.complete(tool_decision_prompt)
            decision = response.text.strip().upper()
            return "YES" in decision
        except Exception as e:
            logger.error(f"Error in LLM tool decision: {e}")
            # Fallback heuristic
            keywords = ["symptom", "treatment", "disease", "drug", "diagnosis", "search"]
            return any(k in message.lower() for k in keywords)

    async def async_send_msg(self, message: str) -> str:
        """Async handler for incoming messages."""
        start_time = time.time()
        try:
            enhanced_message = self._get_enhanced_system_prompt(message)
            if not self.agent_workflow:
                logger.debug("No workflow; using fallback chat")
                chat_messages = [ChatMessage(role=MessageRole.USER, content=message)]
                response = await self.llm.achat(chat_messages)
                result = response.message.content or str(response)
            else:
                out = await self.agent_workflow.run(user_msg=enhanced_message)
                result = str(out) if out else "No response generated."
            elapsed = time.time() - start_time
            self.metrics.log_request(elapsed)
            return result
        except Exception as e:
            elapsed = time.time() - start_time
            self.metrics.log_request(elapsed, error=True)
            return f"Error in async_send_msg: {e}"

    def send_msg(self, message: str) -> str:
        """Sync wrapper to handle queries."""
        start_time = time.time()
        try:
            logger.info(f"Processing query: {message[:100]}...")
            should_use_tools = self._should_use_tools(message)
            if should_use_tools and self.agent_workflow:
                enhanced_message = self._get_enhanced_system_prompt(message)
                out = self._run_workflow_sync(enhanced_message)
                result = str(out) if out else "No response generated."
            else:
                logger.debug("Using simple chat path")
                chat_messages = [ChatMessage(role=MessageRole.USER, content=message)]
                response = self.llm.chat(chat_messages)
                result = response.message.content or "No response generated."
            elapsed = time.time() - start_time
            self.metrics.log_request(elapsed)
            return result
        except Exception as e:
            elapsed = time.time() - start_time
            self.metrics.log_request(elapsed, error=True)
            return f"Error processing query: {e}"

    def _run_workflow_sync(self, user_msg: str):
        """Run workflow from sync code."""
        if not self.agent_workflow:
            raise RuntimeError("No agent_workflow available.")
        # Manejo seguro del event loop (compatible con Streamlit/Jupyter)
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        try:
            import nest_asyncio  # type: ignore

            nest_asyncio.apply()
        except Exception:
            # Si nest_asyncio no está disponible, seguimos igualmente
            pass

        return loop.run_until_complete(self.agent_workflow.run(user_msg=user_msg))

    def get_available_tools(self) -> List[Dict[str, str]]:
        return [
            {"name": tool.metadata.name, "description": tool.metadata.description or ""}
            for tool in self.tools
        ] # type: ignore

    def _get_enhanced_system_prompt(self, user_message: str) -> str:
        return f"""
        You are a medical assistant with {len(self.tools)} tools.
        Strategically use up to {self.max_iterations} tool calls.
        Query: {user_message}
        """
