import uuid
from typing import List, Optional

from llama_index.core.tools import FunctionTool
from llama_index.llms.ollama import Ollama
from loguru import logger

from digiliencia.agents.metrics_tracker import MetricsTracker


class BaseAgent:
    """Clase base con configuración y métricas comunes."""

    def __init__(
        self,
        model_name: str,
        tools: Optional[List[FunctionTool]] = None,
        temperature: float = 0.0,
        timeout_seconds: int = 300,
        verbose: bool = False,
    ):
        self.agent_id = str(uuid.uuid4())[:8]
        self.model_name = model_name
        self.verbose = verbose
        self.timeout_seconds = timeout_seconds

        # LLM configurado
        self.llm = Ollama(
            model=model_name, temperature=temperature, request_timeout=timeout_seconds
        )
        self.tools = tools or []

        # Métricas centralizadas
        self.metrics = MetricsTracker()

        logger.info(
            f"Inicializado {self.__class__.__name__} "
            f"(ID: {self.agent_id}) con modelo {model_name}"
        )

    def async_send_msg(self, message: str):
        """Método que deben implementar las subclases."""
        raise NotImplementedError
