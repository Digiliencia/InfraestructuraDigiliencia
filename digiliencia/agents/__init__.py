"""
Multi-agent system for INCIBE citizen awareness platform.

This package provides a modular, LLM-based multi-agent architecture for handling
cybersecurity queries, news retrieval, and educational conversations.
"""

from digiliencia.agents.agent_utils import (AgentConfig, PerformanceMonitor,
                                            get_performance_monitor,
                                            validate_config)
from digiliencia.agents.base_agent import (BaseAgent, ConversationalAgentBase,
                                           ToolBasedAgent)
from digiliencia.agents.conversational_agent import ConversationalAgent
from digiliencia.agents.factory import AgentFactory, AgentRole
from digiliencia.agents.news_agent import NewsAgent
from digiliencia.agents.router_agent import RouterAgent

__all__ = [
    # Base classes
    "BaseAgent",
    "ToolBasedAgent",
    "ConversationalAgentBase",
    # Specialized agents
    "RouterAgent",
    "NewsAgent",
    "ConversationalAgent",
    # Factory and utilities
    "AgentFactory",
    "AgentRole",
    "AgentConfig",
    "PerformanceMonitor",
    "get_performance_monitor",
    "validate_config",
]

__version__ = "1.0.0"
