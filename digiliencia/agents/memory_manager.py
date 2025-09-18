import time
from typing import List

from llama_index.core.llms import ChatMessage, MessageRole
from loguru import logger


class MemoryManager:
    """Gestiona la memoria de la conversación y el historial de interacciones."""

    def __init__(self, token_limit: int = 10000, max_messages: int = 50):
        self.token_limit = token_limit
        self.max_messages = max_messages
        self.history: List[ChatMessage] = []
        self.topics_discussed = set()
        self.last_interaction = None

    def add_message(self, role: MessageRole, content: str):
        """Añade un mensaje al historial."""
        self.history.append(ChatMessage(role=role, content=content))
        self.last_interaction = time.time()

        # Limitar longitud
        if len(self.history) > self.max_messages:
            self.history = self.history[-self.max_messages :]

        logger.debug(f"Memoria actualizada: {len(self.history)} mensajes")

    def get_history(self) -> List[ChatMessage]:
        return self.history

    def summarize(self) -> dict:
        """Resumen de la conversación."""
        return {
            "messages": len(self.history),
            "topics": list(self.topics_discussed),
            "last_interaction": self.last_interaction,
        }

    def reset(self):
        self.history.clear()
        self.topics_discussed.clear()
        self.last_interaction = None
        logger.info("Memoria de conversación reseteada")
