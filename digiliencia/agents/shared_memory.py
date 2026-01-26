"""
Shared Memory System for Multi-Agent Architecture.

This module provides a centralized conversation memory that is shared across
all agents in the system, enabling contextual awareness and conversation continuity.
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from loguru import logger


class MessageRole(Enum):
    """Enumeration of message roles in conversation."""

    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


@dataclass
class ConversationMessage:
    """
    Represents a single message in the conversation history.

    Attributes:
        role: Who sent the message (user, assistant, system)
        content: The message content
        timestamp: When the message was sent
        agent_name: Which agent processed/sent the message (for assistant messages)
        metadata: Additional information about the message
    """

    role: MessageRole
    content: str
    timestamp: datetime = field(default_factory=datetime.now)
    agent_name: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert message to dictionary representation."""
        return {
            "role": self.role.value,
            "content": self.content,
            "timestamp": self.timestamp.isoformat(),
            "agent_name": self.agent_name,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ConversationMessage":
        """Create a message from dictionary representation."""
        return cls(
            role=MessageRole(data["role"]),
            content=data["content"],
            timestamp=datetime.fromisoformat(data["timestamp"]),
            agent_name=data.get("agent_name"),
            metadata=data.get("metadata", {}),
        )

    def __str__(self) -> str:
        agent_info = f" [{self.agent_name}]" if self.agent_name else ""
        return f"{self.role.value}{agent_info}: {self.content[:100]}..."


class SharedConversationMemory:
    """
    Centralized conversation memory shared across all agents.

    This class maintains the complete conversation history and provides
    methods for agents to access context-aware information about the
    ongoing conversation.
    """

    def __init__(self, max_history: int = 50, context_window: int = 10):
        """
        Initialize the shared memory.

        Args:
            max_history: Maximum number of messages to store
            context_window: Number of recent messages to include in context
        """
        self._messages: List[ConversationMessage] = []
        self._max_history = max_history
        self._context_window = context_window
        self._conversation_id: str = datetime.now().strftime("%Y%m%d_%H%M%S")
        self._summary: Optional[str] = None

        logger.info(
            f"SharedConversationMemory initialized with conversation_id: {self._conversation_id}"
        )

    @property
    def conversation_id(self) -> str:
        """Get the current conversation ID."""
        return self._conversation_id

    @property
    def message_count(self) -> int:
        """Get the total number of messages in history."""
        return len(self._messages)

    def add_message(
        self,
        role: MessageRole,
        content: str,
        agent_name: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> ConversationMessage:
        """
        Add a new message to the conversation history.

        Args:
            role: The role of the message sender
            content: The message content
            agent_name: Name of the agent (for assistant messages)
            metadata: Additional metadata

        Returns:
            The created ConversationMessage
        """
        message = ConversationMessage(
            role=role, content=content, agent_name=agent_name, metadata=metadata or {}
        )

        self._messages.append(message)

        # Trim history if exceeding max
        if len(self._messages) > self._max_history:
            self._messages = self._messages[-self._max_history :]
            logger.debug(
                f"Trimmed conversation history to {self._max_history} messages"
            )

        logger.debug(f"Added message to shared memory: {message}")
        return message

    def add_user_message(
        self, content: str, metadata: Optional[Dict[str, Any]] = None
    ) -> ConversationMessage:
        """Convenience method to add a user message."""
        return self.add_message(MessageRole.USER, content, metadata=metadata)

    def add_assistant_message(
        self, content: str, agent_name: str, metadata: Optional[Dict[str, Any]] = None
    ) -> ConversationMessage:
        """Convenience method to add an assistant message."""
        return self.add_message(
            MessageRole.ASSISTANT, content, agent_name=agent_name, metadata=metadata
        )

    def get_recent_messages(self, n: Optional[int] = None) -> List[ConversationMessage]:
        """
        Get the most recent n messages.

        Args:
            n: Number of messages to retrieve (defaults to context_window)

        Returns:
            List of recent messages
        """
        n = n or self._context_window
        return self._messages[-n:] if self._messages else []

    def get_all_messages(self) -> List[ConversationMessage]:
        """Get all messages in history."""
        return self._messages.copy()

    def get_context_for_agent(self, include_agent_info: bool = True) -> str:
        """
        Get formatted conversation context for agent prompts.

        This method formats recent messages into a string that can be
        included in agent prompts to provide conversation awareness.

        Args:
            include_agent_info: Whether to include which agent responded

        Returns:
            Formatted conversation context string
        """
        recent = self.get_recent_messages()

        if not recent:
            return "No previous conversation context."

        context_parts = ["=== CONVERSATION HISTORY ==="]

        for msg in recent:
            role_label = msg.role.value.upper()
            if (
                msg.role == MessageRole.ASSISTANT
                and include_agent_info
                and msg.agent_name
            ):
                role_label = f"ASSISTANT ({msg.agent_name})"

            # Truncate very long messages in context
            content = msg.content
            if len(content) > 500:
                content = content[:500] + "... [truncated]"

            context_parts.append(f"{role_label}: {content}")

        context_parts.append("=== END HISTORY ===")

        return "\n".join(context_parts)

    def get_context_as_chat_messages(self) -> List[Dict[str, str]]:
        """
        Get recent messages in chat format for LLM APIs.

        Returns:
            List of dicts with 'role' and 'content' keys
        """
        recent = self.get_recent_messages()
        return [{"role": msg.role.value, "content": msg.content} for msg in recent]

    def get_last_user_message(self) -> Optional[ConversationMessage]:
        """Get the most recent user message."""
        for msg in reversed(self._messages):
            if msg.role == MessageRole.USER:
                return msg
        return None

    def get_last_assistant_message(self) -> Optional[ConversationMessage]:
        """Get the most recent assistant message."""
        for msg in reversed(self._messages):
            if msg.role == MessageRole.ASSISTANT:
                return msg
        return None

    def get_messages_by_agent(self, agent_name: str) -> List[ConversationMessage]:
        """Get all messages from a specific agent."""
        return [msg for msg in self._messages if msg.agent_name == agent_name]

    def search_messages(self, keyword: str) -> List[ConversationMessage]:
        """
        Search messages containing a keyword.

        Args:
            keyword: Keyword to search for (case-insensitive)

        Returns:
            List of matching messages
        """
        keyword_lower = keyword.lower()
        return [msg for msg in self._messages if keyword_lower in msg.content.lower()]

    def clear(self):
        """Clear all conversation history."""
        self._messages.clear()
        self._summary = None
        self._conversation_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        logger.info("Conversation memory cleared, new conversation started")

    def export_conversation(self) -> Dict[str, Any]:
        """
        Export the entire conversation for persistence or analysis.

        Returns:
            Dictionary containing conversation data
        """
        return {
            "conversation_id": self._conversation_id,
            "message_count": len(self._messages),
            "messages": [msg.to_dict() for msg in self._messages],
            "exported_at": datetime.now().isoformat(),
        }

    def import_conversation(self, data: Dict[str, Any]):
        """
        Import a previously exported conversation.

        Args:
            data: Exported conversation data
        """
        self._conversation_id = data.get("conversation_id", self._conversation_id)
        self._messages = [
            ConversationMessage.from_dict(msg_data)
            for msg_data in data.get("messages", [])
        ]
        logger.info(f"Imported conversation with {len(self._messages)} messages")

    def get_conversation_summary_prompt(self) -> str:
        """
        Generate a prompt for LLM to summarize the conversation.

        Returns:
            Prompt string for summarization
        """
        if not self._messages:
            return ""

        messages_text = "\n".join(
            [f"{msg.role.value}: {msg.content}" for msg in self._messages]
        )

        return f"""Please provide a brief summary of the following conversation, 
highlighting the main topics discussed and any important conclusions:

{messages_text}

Summary:"""

    def __len__(self) -> int:
        return len(self._messages)

    def __repr__(self) -> str:
        return f"SharedConversationMemory(id={self._conversation_id}, messages={len(self._messages)})"


# Singleton instance for the application
_shared_memory_instance: Optional[SharedConversationMemory] = None


def get_shared_memory() -> SharedConversationMemory:
    """
    Get the singleton shared memory instance.

    Returns:
        The shared conversation memory instance
    """
    global _shared_memory_instance
    if _shared_memory_instance is None:
        _shared_memory_instance = SharedConversationMemory()
    return _shared_memory_instance


def reset_shared_memory():
    """Reset the shared memory instance."""
    global _shared_memory_instance
    if _shared_memory_instance is not None:
        _shared_memory_instance.clear()
    _shared_memory_instance = SharedConversationMemory()
    return _shared_memory_instance
