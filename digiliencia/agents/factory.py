"""
Agent factory for creating and managing agent instances.

This module provides a centralized factory pattern for agent creation,
ensuring consistent configuration and initialization.
"""

from enum import Enum
from typing import Optional

from loguru import logger

from digiliencia.agents.base_agent import BaseAgent
from digiliencia.agents.conversational_agent import ConversationalAgent
from digiliencia.agents.rag.news_agent import NewsAgent
from digiliencia.agents.router_agent import RouterAgent


class AgentRole(Enum):
    """Enumeration of available agent roles."""
    ROUTER = "router"
    NEWS = "news"
    CONVERSATIONAL = "conversational"


class AgentFactory:
    """
    Factory class for creating agent instances.
    
    Provides a centralized, consistent way to create agents with
    appropriate configuration and error handling.
    """
    
    @staticmethod
    def create_agent(
        role: AgentRole,
        model_name: str = "llama3.1:8b",
        temperature: Optional[float] = None,
        verbose: bool = False,
    ) -> Optional[BaseAgent]:
        """
        Create an agent of the specified role.
        
        Args:
            role: The role/type of agent to create
            model_name: Name of the Ollama model to use
            temperature: LLM temperature (None = use role-specific default)
            verbose: Enable verbose logging
            
        Returns:
            Initialized agent instance or None if creation fails
        """
        try:
            logger.info(f"Creating {role.value} agent with model {model_name}")
            
            if role == AgentRole.ROUTER:
                temp = temperature if temperature is not None else 0.1
                agent = RouterAgent(
                    model_name=model_name,
                    temperature=temp,
                    verbose=verbose,
                )
            
            elif role == AgentRole.NEWS:
                temp = temperature if temperature is not None else 0.3
                agent = NewsAgent(
                    model_name=model_name,
                    temperature=temp,
                    verbose=verbose,
                )
            
            elif role == AgentRole.CONVERSATIONAL:
                temp = temperature if temperature is not None else 0.7
                agent = ConversationalAgent(
                    model_name=model_name,
                    temperature=temp,
                    verbose=verbose,
                )
            
            else:
                logger.error(f"Unknown agent role: {role}")
                return None
            
            logger.info(f"Successfully created {role.value} agent")
            return agent
            
        except Exception as e:
            logger.error(f"Failed to create {role.value} agent: {e}")
            return None
    
    @staticmethod
    def create_router_agent(
        model_name: str = "llama3.1:8b",
        verbose: bool = False,
    ) -> Optional[RouterAgent]:
        """
        Convenience method to create a router agent.
        
        Args:
            model_name: Name of the Ollama model to use
            verbose: Enable verbose logging
            
        Returns:
            RouterAgent instance or None if creation fails
        """
        agent = AgentFactory.create_agent(
            role=AgentRole.ROUTER,
            model_name=model_name,
            verbose=verbose,
        )
        return agent if isinstance(agent, RouterAgent) else None
    
    @staticmethod
    def create_news_agent(
        model_name: str = "llama3.1:8b",
        verbose: bool = False,
    ) -> Optional[NewsAgent]:
        """
        Convenience method to create a news agent.
        
        Args:
            model_name: Name of the Ollama model to use
            verbose: Enable verbose logging
            
        Returns:
            NewsAgent instance or None if creation fails
        """
        agent = AgentFactory.create_agent(
            role=AgentRole.NEWS,
            model_name=model_name,
            verbose=verbose,
        )
        return agent if isinstance(agent, NewsAgent) else None
    
    @staticmethod
    def create_conversational_agent(
        model_name: str = "llama3.1:8b",
        verbose: bool = False,
    ) -> Optional[ConversationalAgent]:
        """
        Convenience method to create a conversational agent.
        
        Args:
            model_name: Name of the Ollama model to use
            verbose: Enable verbose logging
            
        Returns:
            ConversationalAgent instance or None if creation fails
        """
        agent = AgentFactory.create_agent(
            role=AgentRole.CONVERSATIONAL,
            model_name=model_name,
            verbose=verbose,
        )
        return agent if isinstance(agent, ConversationalAgent) else None
