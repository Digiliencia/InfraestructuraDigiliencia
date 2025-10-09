"""
Base agent architecture for the multi-agent system.

This module provides abstract base classes and interfaces for building specialized agents
in the INCIBE citizen awareness system.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from llama_index.core.llms import LLM
from llama_index.llms.ollama import Ollama
from loguru import logger


class BaseAgent(ABC):
    """
    Abstract base class for all agents in the system.
    
    All specialized agents must inherit from this class and implement
    the required abstract methods.
    """
    
    def __init__(
        self,
        name: str,
        description: str,
        model_name: str = "llama3.1:8b",
        temperature: float = 0.7,
        request_timeout: float = 600.0,  # 10 minutos para sistemas lentos
        verbose: bool = False,
    ):
        """
        Initialize the base agent.
        
        Args:
            name: Unique identifier for the agent
            description: Brief description of agent capabilities
            model_name: Name of the Ollama model to use
            temperature: LLM temperature (0.0 = deterministic, 1.0 = creative)
            request_timeout: Maximum time to wait for LLM response (default 600s = 10min)
            verbose: Enable detailed logging
        """
        self.name = name
        self.description = description
        self.model_name = model_name
        self.temperature = temperature
        self.request_timeout = request_timeout
        self.verbose = verbose
        
        # Initialize LLM
        self._llm = self._initialize_llm()
        
        # Metrics tracking
        self._total_queries = 0
        self._successful_queries = 0
        self._failed_queries = 0
        
        logger.info(f"Initialized {self.name} agent with model {model_name}")
    
    def _initialize_llm(self) -> LLM:
        """
        Initialize the Ollama LLM instance.
        
        Returns:
            Configured LLM instance
        """
        try:
            llm = Ollama(
                model=self.model_name,
                temperature=self.temperature,
                request_timeout=self.request_timeout,
            )
            logger.debug(f"LLM initialized for {self.name}")
            return llm
        except Exception as e:
            logger.error(f"Failed to initialize LLM for {self.name}: {e}")
            raise
    
    @abstractmethod
    def process_query(self, query: str, **kwargs) -> str:
        """
        Process a user query and return a response.
        
        Args:
            query: User's input query
            **kwargs: Additional parameters for processing
            
        Returns:
            Agent's response as a string
        """
        pass
    
    @abstractmethod
    def get_system_prompt(self) -> str:
        """
        Get the system prompt for this agent.
        
        Returns:
            System prompt string
        """
        pass
    
    def record_query(self, success: bool = True):
        """
        Record query metrics.
        
        Args:
            success: Whether the query was successful
        """
        self._total_queries += 1
        if success:
            self._successful_queries += 1
        else:
            self._failed_queries += 1
    
    def get_metrics(self) -> Dict[str, Any]:
        """
        Get agent performance metrics.
        
        Returns:
            Dictionary with agent metrics
        """
        success_rate = (
            (self._successful_queries / self._total_queries * 100)
            if self._total_queries > 0
            else 0.0
        )
        
        return {
            "name": self.name,
            "total_queries": self._total_queries,
            "successful_queries": self._successful_queries,
            "failed_queries": self._failed_queries,
            "success_rate": round(success_rate, 2),
        }
    
    def reset_metrics(self):
        """Reset all metrics counters."""
        self._total_queries = 0
        self._successful_queries = 0
        self._failed_queries = 0
        logger.debug(f"Metrics reset for {self.name}")
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', model='{self.model_name}')"


class ToolBasedAgent(BaseAgent):
    """
    Base class for agents that use tools to answer queries.
    
    These agents must always use their available tools to provide responses
    based on real data rather than generating responses from the LLM alone.
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._tools = []
    
    @abstractmethod
    def get_tools(self) -> List[Any]:
        """
        Get the list of tools available to this agent.
        
        Returns:
            List of tool functions or objects
        """
        pass
    
    def get_tool_descriptions(self) -> List[Dict[str, str]]:
        """
        Get descriptions of all available tools.
        
        Returns:
            List of dictionaries with tool name and description
        """
        tools = self.get_tools()
        descriptions = []
        
        for tool in tools:
            descriptions.append({
                "name": getattr(tool, "__name__", str(tool)),
                "description": getattr(tool, "__doc__", "No description available"),
            })
        
        return descriptions


class ConversationalAgentBase(BaseAgent):
    """
    Base class for conversational agents that don't require tools.
    
    These agents handle general questions and conversations using
    only the LLM's knowledge and reasoning capabilities.
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._conversation_history: List[Dict[str, str]] = []
    
    def add_to_history(self, role: str, content: str):
        """
        Add a message to the conversation history.
        
        Args:
            role: 'user' or 'assistant'
            content: Message content
        """
        self._conversation_history.append({
            "role": role,
            "content": content,
        })
    
    def clear_history(self):
        """Clear the conversation history."""
        self._conversation_history.clear()
        logger.debug(f"Conversation history cleared for {self.name}")
    
    def get_history(self) -> List[Dict[str, str]]:
        """
        Get the conversation history.
        
        Returns:
            List of conversation messages
        """
        return self._conversation_history.copy()
