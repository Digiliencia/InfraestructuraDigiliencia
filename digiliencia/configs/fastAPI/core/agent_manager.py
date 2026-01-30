"""
Agent Manager for centralized agent initialization and reuse (FastAPI specific).

This module handles the creation and caching of RouterAgent instances
and provides utilities for safely switching conversation contexts.
"""

from typing import Dict, Optional
from loguru import logger

from digiliencia.agents.router_agent import RouterAgent
from digiliencia.agents.shared_memory import SharedConversationMemory
from digiliencia.configs.env import env


class AgentManager:
    """
    Manager for agent instances to ensure they are initialized once and reused.
    """

    _instance: Optional["AgentManager"] = None
    _agents: Dict[str, RouterAgent] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AgentManager, cls).__new__(cls)
        return cls._instance

    def get_agent(self, model_name: Optional[str] = None) -> RouterAgent:
        """
        Get or create a RouterAgent for the specified model.

        Args:
            model_name: Name of the model to use (defaults to env.chatbot_llm)

        Returns:
            A pre-initialized RouterAgent instance.
        """
        name = model_name or env.chatbot_llm
        
        if name not in self._agents:
            logger.info(f"Initializing new RouterAgent for model: {name}")
            self._agents[name] = RouterAgent(model_name=name)
        
        return self._agents[name]

    def set_agent_context(self, agent: RouterAgent, memory: SharedConversationMemory):
        """
        Safely update the conversation memory for a RouterAgent and all its
        specialized sub-agents without modifying the agent files.
        """
        # Update RouterAgent's memory references
        agent._shared_memory = memory
        agent._memory = memory
        
        # Propagate to all specialized sub-agents (NewsAgent, ConversationalAgent)
        if hasattr(agent, '_agents'):
            for sub_agent in agent._agents.values():
                sub_agent._shared_memory = memory
        
        logger.debug(f"RouterAgent context switched to memory: {memory.conversation_id}")

    def pre_initialize(self):
        """
        Pre-initialize the default agent.
        """
        default_model = env.chatbot_llm
        logger.info(f"Pre-initializing default agent ({default_model})...")
        self.get_agent(default_model)


# Global singleton instance
agent_manager = AgentManager()
