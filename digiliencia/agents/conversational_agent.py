import time
from typing import Any, Dict, List, Optional

from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.core.tools import FunctionTool
from loguru import logger

from digiliencia.agents.base_agent import BaseAgent
from digiliencia.agents.memory_manager import MemoryManager


class ConversationalAgent(BaseAgent):
    """Agente especializado en mantener conversaciones con memoria contextual."""

    def __init__(
        self,
        model_name: str,
        tools: Optional[List[FunctionTool]] = None,
        temperature: float = 0.2,
        verbose: bool = False,
        memory_token_limit: int = 10000,
        max_history_messages: int = 20,
    ):
        super().__init__(model_name, tools, temperature, verbose=verbose)
        self.memory = MemoryManager(
            token_limit=memory_token_limit, max_messages=max_history_messages
        )
        self.conversation_turns = 0

    def async_send_msg(self, message: str) -> str:
        start_time = time.time()
        self.conversation_turns += 1

        try:
            # Guardar mensaje usuario
            self.memory.add_message(MessageRole.USER, message)

            # Recuperar historial
            chat_history = self.memory.get_history()

            if self.verbose:
                for msg in chat_history[-3:]:
                    logger.debug(f"{msg.role.value}: {msg.content[:60]}")  # type: ignore

            # Llamada al LLM
            response = self.llm.chat(chat_history)
            response_content = response.message.content or "No se generó respuesta."

            # Guardar respuesta
            self.memory.add_message(MessageRole.ASSISTANT, response_content)

            elapsed = time.time() - start_time
            self.metrics.log_request(elapsed)

            return response_content

        except Exception as e:
            elapsed = time.time() - start_time
            self.metrics.log_request(elapsed, error=True)
            logger.error(f"Error en ConversationalAgent: {e}")
            return "Ocurrió un error procesando tu mensaje."

    # Interfaz síncrona estándar para compatibilidad con Streamlit y RouterAgent
    def send_msg(self, message: str) -> str:
        """Wrapper síncrono (mismo comportamiento que async_send_msg)."""
        return self.async_send_msg(message)

    def get_summary(self) -> Dict[str, Any]:
        return {
            "turns": self.conversation_turns,
            "memory": self.memory.summarize(),
            "metrics": self.metrics.report(),
        }

    def clear_history(self):
        self.memory.reset()
        self.conversation_turns = 0
