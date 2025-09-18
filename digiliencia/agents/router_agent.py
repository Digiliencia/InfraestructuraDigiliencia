import time
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.core.tools import FunctionTool
from loguru import logger

from digiliencia.agents.conversational_agent import ConversationalAgent
from digiliencia.agents.memory_manager import MemoryManager
from digiliencia.agents.metrics_tracker import MetricsTracker
from digiliencia.agents.rag.news_agent import NewsAgent


class AgentType(Enum):
    CONVERSATIONAL = "conversational"
    NEWS = "news"


class RouterAgent:
    """Agente enrutador que delega en el LLM la decisión de qué subagente usar."""

    def __init__(
        self,
        model_name: str,
        tools: Optional[List[FunctionTool]] = None,
        verbose: bool = False,
    ):
        self.model_name = model_name
        self.verbose = verbose

        self.memory = MemoryManager()
        self.metrics = MetricsTracker()

        # Registro de agentes disponibles (fácil de ampliar)
        self.agents: Dict[AgentType, Any] = {
            AgentType.CONVERSATIONAL: ConversationalAgent(
                model_name=model_name, verbose=verbose
            ),
            AgentType.NEWS: NewsAgent(
                model_name=model_name, tools=tools, verbose=verbose
            ),
        }

        # LLM "ligero" solo para clasificación de routing
        # Reutilizamos el ConversationalAgent internamente como LLM base
        self.classifier = ConversationalAgent(model_name=model_name, verbose=verbose)

    def _classify_query(self, message: str) -> AgentType:
        """
        Usa el LLM para decidir a qué agente enrutar la query.
        """
        system_prompt = """
        You are a router that decides which specialized agent should handle the query.
        Available agents:
        - conversational: for general chit-chat, casual dialogue, greetings, or general knowledge.
        - news: for questions about cybersecurity news, threat intelligence, vulnerabilities, or security updates.

        Respond with only one word: conversational or news.
        """

        try:
            chat_messages = [
                ChatMessage(role=MessageRole.SYSTEM, content=system_prompt),
                ChatMessage(role=MessageRole.USER, content=message),
            ]
            response = self.classifier.llm.chat(chat_messages)
            decision = response.message.content.strip().lower()

            if "news" in decision:
                return AgentType.NEWS
            return AgentType.CONVERSATIONAL
        except Exception as e:
            logger.error(f"Fallo en clasificación con LLM: {e}")
            # fallback simple
            return AgentType.CONVERSATIONAL

    def send_msg(self, message: str) -> Union[str, Dict[str, Any]]:
        start = time.time()
        try:
            self.memory.add_message(MessageRole.USER, message)

            agent_type = self._classify_query(message)
            if self.verbose:
                logger.info(f"Routing query to agent: {agent_type.value}")

            agent = self.agents.get(agent_type)
            if not agent:
                raise ValueError(f"No agent available for type {agent_type}")

            response = agent.send_msg(message)
            self.memory.add_message(MessageRole.ASSISTANT, str(response))

            elapsed = time.time() - start
            self.metrics.log_request(elapsed)
            return response
        except Exception as e:
            elapsed = time.time() - start
            self.metrics.log_request(elapsed, error=True)
            logger.error(f"Error en RouterAgent: {e}")
            return {"error": str(e)}

    def get_system_summary(self) -> Dict[str, Any]:
        return {
            "router_metrics": self.metrics.report(),
            "memory_summary": self.memory.summarize(),
            "agent_summaries": {
                name.value: agent.metrics.report()
                for name, agent in self.agents.items()
                if hasattr(agent, "metrics")
            },
        }

    def reset(self):
        self.memory.reset()
        for agent in self.agents.values():
            if hasattr(agent, "clear_history"):
                agent.clear_history()
        logger.info("RouterAgent reseteado")

    # Métodos utilitarios esperados por la UI
    def get_available_tools(self) -> List[Dict[str, str]]:
        try:
            news_agent = self.agents.get(AgentType.NEWS)
            return news_agent.get_available_tools() if news_agent else []
        except Exception:
            return []

    def get_agent_metrics(self) -> Dict[str, Any]:
        return {
            "router": self.metrics.report(),
            **{
                agent_type.value: agent.metrics.report()
                for agent_type, agent in self.agents.items()
                if hasattr(agent, "metrics")
            },
        }

    def get_routing_stats(self) -> Dict[str, Any]:
        try:
            total = self.metrics.total_requests
            usage = {
                agent_type.value: f"{(agent.metrics.total_requests / max(total, 1)) * 100:.1f}%"
                for agent_type, agent in self.agents.items()
                if hasattr(agent, "metrics")
            }
            return {"total_queries": total, "agent_usage_percentage": usage}
        except Exception:
            return {"total_queries": 0, "agent_usage_percentage": {}}

    def reset_conversation(self):
        self.reset()
        for agent in self.agents.values():
            if hasattr(agent, "clear_history"):
                agent.clear_history()