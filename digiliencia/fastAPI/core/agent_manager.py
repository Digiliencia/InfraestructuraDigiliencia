"""
Agent Manager for centralized agent initialization and reuse (FastAPI specific).

This module handles the creation and caching of RouterAgent instances per conversation
(session-based caching) with automatic cleanup of inactive sessions via TTL.
"""

from datetime import datetime, timedelta
from typing import Dict, Optional
from uuid import UUID
from loguru import logger

from digiliencia.agents.router_agent import RouterAgent
from digiliencia.agents.shared_memory import SharedConversationMemory
from digiliencia.configs.env import env


class ConversationSession:
    """Metadata for a conversation session with its agent."""

    def __init__(self, agent: RouterAgent, model_name: str):
        self.agent = agent
        self.model_name = model_name
        self.created_at = datetime.now()
        self.last_access = datetime.now()

    def update_activity(self):
        """Update the last access timestamp."""
        self.last_access = datetime.now()


class AgentManager:
    """
    Manager for agent instances with session-based caching.

    Each conversation (chat_id) gets its own agent instance with isolated memory.
    Inactive sessions are automatically cleaned up after a configurable timeout.
    """

    _instance: Optional["AgentManager"] = None
    _conversation_agents: Dict[UUID, ConversationSession] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AgentManager, cls).__new__(cls)
        return cls._instance

    def get_or_create_conversation_agent(
        self, chat_id: UUID, model_name: str, history: Optional[list] = None
    ) -> RouterAgent:
        """
        Get or create a RouterAgent for a specific conversation session.

        Args:
            chat_id: UUID of the conversation
            model_name: Name of the model to use
            history: Optional list of (role, content, metadata) tuples to populate memory

        Returns:
            A RouterAgent instance isolated to this conversation.
        """
        # Check if session exists and model matches
        if chat_id in self._conversation_agents:
            session = self._conversation_agents[chat_id]

            # If model changed, we need to create a new agent
            if session.model_name != model_name:
                logger.info(
                    f"Model changed for chat {chat_id}: {session.model_name} -> {model_name}. "
                    "Creating new agent."
                )
                self.cleanup_conversation_agent(chat_id)
            else:
                # Reuse existing agent
                session.update_activity()
                logger.debug(f"Reusing existing agent for chat {chat_id}")
                return session.agent

        # Create new agent with isolated memory
        logger.info(f"Creating new agent for chat {chat_id} with model {model_name}")
        memory = SharedConversationMemory()

        # Populate history if provided
        if history:
            for role, content, metadata in history:
                memory.add_message(role=role, content=content, metadata=metadata or {})

        agent = RouterAgent(model_name=model_name)
        agent._shared_memory = memory
        agent._memory = memory

        # Propagate memory to sub-agents
        if hasattr(agent, "_agents"):
            for sub_agent in agent._agents.values():
                sub_agent._shared_memory = memory

        # Store in cache
        self._conversation_agents[chat_id] = ConversationSession(agent, model_name)

        logger.info(
            f"Agent created for chat {chat_id}. Total active sessions: "
            f"{len(self._conversation_agents)}"
        )

        return agent

    def cleanup_conversation_agent(self, chat_id: UUID) -> bool:
        """
        Explicitly remove a conversation's agent from cache.

        Args:
            chat_id: UUID of the conversation to clean up

        Returns:
            True if the session was removed, False if it didn't exist
        """
        if chat_id in self._conversation_agents:
            del self._conversation_agents[chat_id]
            logger.info(
                f"Cleaned up agent for chat {chat_id}. "
                f"Remaining sessions: {len(self._conversation_agents)}"
            )
            return True
        return False

    def cleanup_inactive_sessions(self, timeout_minutes: Optional[int] = None) -> int:
        """
        Remove sessions that have been inactive for longer than the timeout.

        Args:
            timeout_minutes: Inactivity timeout in minutes (defaults to env config)

        Returns:
            Number of sessions cleaned up
        """
        if timeout_minutes is None:
            timeout_minutes = env.agent_session_timeout_minutes

        cutoff_time = datetime.now() - timedelta(minutes=timeout_minutes)

        # Find inactive sessions
        inactive_sessions = [
            chat_id
            for chat_id, session in self._conversation_agents.items()
            if session.last_access < cutoff_time
        ]

        # Remove them
        for chat_id in inactive_sessions:
            del self._conversation_agents[chat_id]

        if inactive_sessions:
            logger.info(
                f"Cleaned up {len(inactive_sessions)} inactive session(s). "
                f"Remaining: {len(self._conversation_agents)}"
            )

        return len(inactive_sessions)

    def get_session_count(self) -> int:
        """Get the number of active sessions."""
        return len(self._conversation_agents)

    def get_session_info(self, chat_id: UUID) -> Optional[Dict]:
        """Get information about a specific session."""
        if chat_id not in self._conversation_agents:
            return None

        session = self._conversation_agents[chat_id]
        return {
            "chat_id": str(chat_id),
            "model_name": session.model_name,
            "created_at": session.created_at.isoformat(),
            "last_access": session.last_access.isoformat(),
            "age_minutes": (datetime.now() - session.created_at).total_seconds() / 60,
            "idle_minutes": (datetime.now() - session.last_access).total_seconds() / 60,
        }


# Global singleton instance
agent_manager = AgentManager()
