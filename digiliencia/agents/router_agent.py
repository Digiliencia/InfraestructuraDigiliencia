"""
Router Agent implementation for intelligent query routing.

This agent acts as an orchestrator, analyzing user queries and routing them
to the appropriate specialized agent. It maintains shared memory across all agents.
"""

from enum import Enum
from typing import Any, Dict, Optional

from loguru import logger

from digiliencia.agents.base_agent import BaseAgent
from digiliencia.agents.conversational_agent import ConversationalAgent
from digiliencia.agents.prompts import ROUTER_SYSTEM_PROMPT
from digiliencia.agents.rag.news_agent import NewsAgent
from digiliencia.agents.shared_memory import (
    SharedConversationMemory,
    get_shared_memory,
    reset_shared_memory,
)


class AgentType(Enum):
    """Enumeration of available agent types."""

    NEWS_AGENT = "NEWS_AGENT"
    CONVERSATIONAL_AGENT = "CONVERSATIONAL_AGENT"


class RouterAgent(BaseAgent):
    """
    Orchestrator agent that routes queries to specialized agents.

    This agent uses an LLM to intelligently determine which specialized
    agent should handle each user query, then delegates the work.

    The RouterAgent manages shared memory and ensures all agents have
    access to the same conversation context.
    """

    def __init__(
        self,
        model_name: str = "llama3.1:8b",
        temperature: float = 0.1,  # Very low temperature for consistent routing
        verbose: bool = False,
        shared_memory: Optional[SharedConversationMemory] = None,
    ):
        """
        Initialize the Router Agent.

        Args:
            model_name: Name of the Ollama model to use
            temperature: LLM temperature (very low for deterministic routing)
            verbose: Enable detailed logging
            shared_memory: Shared memory instance (creates new if None)
        """
        # Initialize shared memory first
        self._memory = shared_memory or get_shared_memory()

        super().__init__(
            name="RouterAgent",
            description="Routes user queries to appropriate specialized agents",
            model_name=model_name,
            temperature=temperature,
            verbose=verbose,
            shared_memory=self._memory,
        )

        # Initialize specialized agents with shared memory
        self._agents: Dict[AgentType, BaseAgent] = {}
        self._initialize_agents(model_name, verbose)

        # Routing statistics
        self._routing_stats: Dict[str, int] = {
            agent_type.value: 0 for agent_type in AgentType
        }

        # Track last agent used for context
        self._last_agent_used: Optional[AgentType] = None

        logger.info("RouterAgent initialized with specialized agents and shared memory")

    def _initialize_agents(self, model_name: str, verbose: bool):
        """
        Initialize all specialized agents with shared memory.

        Args:
            model_name: Model name to use for agents
            verbose: Verbose flag for agents
        """
        try:
            self._agents[AgentType.NEWS_AGENT] = NewsAgent(
                model_name=model_name,
                verbose=verbose,
                shared_memory=self._memory,
            )
            logger.debug("NewsAgent initialized with shared memory")
        except Exception as e:
            logger.error(f"Failed to initialize NewsAgent: {e}")

        try:
            self._agents[AgentType.CONVERSATIONAL_AGENT] = ConversationalAgent(
                model_name=model_name,
                verbose=verbose,
                shared_memory=self._memory,
            )
            logger.debug("ConversationalAgent initialized with shared memory")
        except Exception as e:
            logger.error(f"Failed to initialize ConversationalAgent: {e}")

    def get_system_prompt(self) -> str:
        """
        Get the system prompt for routing decisions.

        Returns:
            System prompt string
        """
        return ROUTER_SYSTEM_PROMPT

    def _route_query(self, query: str) -> AgentType:
        """
        Determine which agent should handle the query.

        Uses conversation context to make better routing decisions.

        Args:
            query: User's input query

        Returns:
            Selected AgentType
        """
        try:
            # Include conversation context for better routing
            context = self._memory.get_context_for_agent(include_agent_info=True)

            # Create routing prompt with context
            if context != "No previous conversation context.":
                routing_prompt = f"""{self.get_system_prompt()}

{context}

Consider the conversation history above when routing. If the user is following up on a previous topic, 
route to the same type of agent unless the query clearly requires a different one.

User Query: {query}

Selected Agent:"""
            else:
                routing_prompt = f"{self.get_system_prompt()}\n\nUser Query: {query}\n\nSelected Agent:"

            # Get LLM decision
            response = self._llm.complete(routing_prompt)
            decision = str(response).strip().upper()

            # Remove any "think" or reasoning text, keep only the last line/word
            if "\n" in decision:
                decision = decision.splitlines()[-1].strip()
            elif " " in decision:
                decision = decision.split()[-1].strip()

            logger.debug(f"LLM routing decision: {decision}")

            # Parse the decision
            if "NEWS_AGENT" in decision or "NEWS" in decision:
                return AgentType.NEWS_AGENT
            elif "CONVERSATIONAL_AGENT" in decision or "CONVERSATIONAL" in decision:
                return AgentType.CONVERSATIONAL_AGENT
            else:
                # Default to conversational for ambiguous cases
                logger.warning(
                    f"Ambiguous routing decision: {decision}. Defaulting to CONVERSATIONAL_AGENT"
                )
                return AgentType.CONVERSATIONAL_AGENT

        except Exception as e:
            logger.error(f"Error during query routing: {e}")
            # Default to conversational agent on error
            return AgentType.CONVERSATIONAL_AGENT

    def process_query(self, query: str, **kwargs) -> str:
        """
        Route the query to the appropriate agent and return the response.

        This method adds the user message to shared memory before processing
        and ensures the response is also stored in shared memory.

        Args:
            query: User's input query
            **kwargs: Additional parameters

        Returns:
            Response from the specialized agent
        """
        try:
            logger.info(f"RouterAgent received query: {query[:100]}...")

            # Add user message to shared memory
            self._memory.add_user_message(query)

            # Determine which agent to use
            selected_agent_type = self._route_query(query)

            # Update routing statistics
            self._routing_stats[selected_agent_type.value] += 1
            self._last_agent_used = selected_agent_type

            # Get the selected agent
            selected_agent = self._agents.get(selected_agent_type)

            if not selected_agent:
                logger.error(f"Agent {selected_agent_type} not available")
                error_response = "I'm sorry, but the requested service is currently unavailable. Please try again later."
                self._memory.add_assistant_message(error_response, agent_name=self.name)
                return error_response

            logger.info(f"Query routed to: {selected_agent_type.value}")

            # Process with the selected agent
            response = selected_agent.process_query(query, **kwargs)

            # The agent should have added its response to shared memory,
            # but we ensure it here for agents that might not
            # (This is handled in the agent's add_to_history method)

            self.record_query(success=True)
            logger.debug("RouterAgent query completed successfully")

            return response

        except Exception as e:
            logger.error(f"Error in RouterAgent.process_query: {e}")
            self.record_query(success=False)

            error_response = (
                f"I encountered an error while processing your request: {str(e)}. "
                "Please try again or rephrase your question."
            )
            self._memory.add_assistant_message(error_response, agent_name=self.name)
            return error_response

    def send_msg(self, message: str) -> str:
        """
        Alias for process_query for backwards compatibility.

        Args:
            message: User's message

        Returns:
            Agent's response
        """
        return self.process_query(message)

    def get_routing_stats(self) -> Dict[str, Any]:
        """
        Get routing statistics.

        Returns:
            Dictionary with routing statistics
        """
        total_queries = sum(self._routing_stats.values())

        percentages = {}
        for agent_type, count in self._routing_stats.items():
            percentages[agent_type] = (
                round((count / total_queries * 100), 2) if total_queries > 0 else 0.0
            )

        return {
            "total_queries": total_queries,
            "agent_usage_count": self._routing_stats.copy(),
            "agent_usage_percentage": percentages,
        }

    def get_agent_metrics(self) -> Dict[str, Any]:
        """
        Get metrics from all agents.

        Returns:
            Dictionary with metrics from all agents
        """
        metrics = {
            "router": self.get_metrics(),
            "routing_stats": self.get_routing_stats(),
            "agents": {},
            "memory": {
                "conversation_id": self._memory.conversation_id,
                "message_count": self._memory.message_count,
            },
        }

        for agent_type, agent in self._agents.items():
            metrics["agents"][agent_type.value] = agent.get_metrics()

        return metrics

    def get_conversation_history(self) -> list:
        """
        Get the full conversation history from shared memory.

        Returns:
            List of conversation messages
        """
        return [msg.to_dict() for msg in self._memory.get_all_messages()]

    def clear_conversation(self):
        """
        Clear the conversation history and reset shared memory.
        """
        reset_shared_memory()
        self._memory = get_shared_memory()

        # Update memory reference in all agents
        for agent in self._agents.values():
            agent._shared_memory = self._memory

        logger.info("Conversation history cleared for all agents")

    def get_last_agent_used(self) -> Optional[str]:
        """Get the name of the last agent that handled a query."""
        return self._last_agent_used.value if self._last_agent_used else None
