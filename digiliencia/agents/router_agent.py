import time
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from llama_index.core.llms import MessageRole
from llama_index.core.tools import FunctionTool
from loguru import logger

from digiliencia.agents.conversational_agent import ConversationalAgent
from digiliencia.agents.memory_manager import MemoryManager
from digiliencia.agents.metrics_tracker import MetricsTracker
from digiliencia.agents.rag.news_agent import NewsAgent


class AgentType(Enum):
    CONVERSATIONAL = "conversational"
    TOOL_CALLING = "tool_calling"


class RouterAgent:
    """Agente enrutador que usa memoria global y decide qué subagente usar."""

    def __init__(
        self,
        model_name: str,
        tools: Optional[List[FunctionTool]] = None,
        verbose: bool = False,
    ):
        self.memory = MemoryManager()
        self.metrics = MetricsTracker()

        self.conversational_agent = ConversationalAgent(
            model_name=model_name, verbose=verbose
        )
        self.tool_calling_agent = NewsAgent(
            model_name=model_name, tools=tools, verbose=verbose
        )

    def _classify_query(self, message: str) -> AgentType:
        """Clasifica la query en conversacional o de búsqueda."""
        keywords = [
            "treatment", "symptom", "disease", "medication",
            "diagnosis", "therapy", "condition", "medical",
            "health", "drug", "medicine", "pain", "dosage"
        ]
        if any(k in message.lower() for k in keywords):
            return AgentType.TOOL_CALLING
        return AgentType.CONVERSATIONAL

    def send_msg(self, message: str) -> Union[str, Dict[str, Any]]:
        start = time.time()
        try:
            self.memory.add_message(MessageRole.USER, message)
            agent_type = self._classify_query(message)

            if agent_type == AgentType.CONVERSATIONAL:
                response = self.conversational_agent.send_msg(message)
            else:
                # NewsAgent expone send_msg síncrono que internamente maneja tools/async
                response = self.tool_calling_agent.send_msg(message)

            self.memory.add_message(MessageRole.ASSISTANT, str(response))

            elapsed = time.time() - start
            self.metrics.log_request(elapsed)

            return response # type: ignore
        except Exception as e:
            elapsed = time.time() - start
            self.metrics.log_request(elapsed, error=True)
            logger.error(f"Error en RouterAgent: {e}")
            return {"error": str(e)}

    def get_system_summary(self) -> Dict[str, Any]:
        return {
            "router_metrics": self.metrics.report(),
            "memory_summary": self.memory.summarize(),
            "conversational_summary": self.conversational_agent.get_summary(),
        }

    def reset(self):
        self.memory.reset()
        self.conversational_agent.clear_history()
        logger.info("RouterAgent reseteado")

    # Métodos utilitarios esperados por la UI
    def get_available_tools(self) -> List[Dict[str, str]]:
        try:
            return self.tool_calling_agent.get_available_tools()
        except Exception:
            return []

    def get_agent_metrics(self) -> Dict[str, Any]:
        return {
            "router": self.metrics.report(),
            "conversational": self.conversational_agent.metrics.report(),
            "tool_calling": self.tool_calling_agent.metrics.report(),
        }

    def get_routing_stats(self) -> Dict[str, Any]:
        # Sencillo resumen basado en memoria y contadores
        try:
            total = self.metrics.total_requests
            # No llevamos contador por tipo; aproximamos con totals de subagentes
            conv_total = self.conversational_agent.metrics.total_requests
            tool_total = self.tool_calling_agent.metrics.total_requests
            agent_usage = {
                "conversational": f"{(conv_total / max(total, 1)) * 100:.1f}%",
                "tool_calling": f"{(tool_total / max(total, 1)) * 100:.1f}%",
            }
            return {
                "total_queries": total,
                "agent_usage_percentage": agent_usage,
            }
        except Exception:
            return {"total_queries": 0, "agent_usage_percentage": {}}

    def reset_conversation(self):
        self.reset()
