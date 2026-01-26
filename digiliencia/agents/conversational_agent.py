"""
Conversational Agent implementation for general cybersecurity education.

This agent handles general questions, explanations, and educational conversations
without requiring tool usage. It uses shared memory to maintain context across
all agents in the system.
"""

from typing import Optional

from llama_index.core.chat_engine import SimpleChatEngine
from loguru import logger

from digiliencia.agents.base_agent import ConversationalAgentBase
from digiliencia.agents.prompts import CONVERSATIONAL_AGENT_SYSTEM_PROMPT
from digiliencia.agents.shared_memory import SharedConversationMemory


class ConversationalAgent(ConversationalAgentBase):
    """
    Specialized agent for general cybersecurity education and conversations.

    This agent uses only the LLM's knowledge to answer questions about
    cybersecurity concepts, best practices, and provide educational guidance.

    It has access to shared memory to reference previous conversations,
    even those handled by other agents.
    """

    def __init__(
        self,
        model_name: str = "llama3.1:8b",
        temperature: float = 0.7,  # Higher temperature for more conversational responses
        verbose: bool = False,
        shared_memory: Optional[SharedConversationMemory] = None,
    ):
        """
        Initialize the Conversational Agent.

        Args:
            model_name: Name of the Ollama model to use
            temperature: LLM temperature (higher = more creative)
            verbose: Enable detailed logging
            shared_memory: Shared memory instance for cross-agent context
        """
        super().__init__(
            name="ConversationalAgent",
            description="Provides cybersecurity education and answers general questions",
            model_name=model_name,
            temperature=temperature,
            verbose=verbose,
            shared_memory=shared_memory,
        )

        # Initialize simple chat engine
        self._chat_engine = self._initialize_chat_engine()

        logger.info(
            "ConversationalAgent initialized with SimpleChatEngine and shared memory"
        )

    def _initialize_chat_engine(self) -> SimpleChatEngine:
        """
        Initialize the simple chat engine for conversations.

        Returns:
            Configured SimpleChatEngine instance
        """
        chat_engine = SimpleChatEngine.from_defaults(
            llm=self._llm,
            system_prompt=self.get_system_prompt(),
        )

        return chat_engine

    def get_system_prompt(self) -> str:
        """
        Get the system prompt for the Conversational Agent.

        Returns:
            System prompt string
        """
        return CONVERSATIONAL_AGENT_SYSTEM_PROMPT

    def process_query(self, query: str, **kwargs) -> str:
        """
        Process a general query using the chat engine with shared memory context.

        Args:
            query: User's question or conversation input
            **kwargs: Additional parameters (e.g., include_history)

        Returns:
            Agent's educational and helpful response
        """
        try:
            logger.info(f"ConversationalAgent processing query: {query[:100]}...")

            # Build prompt with conversation context from shared memory
            context = self.get_conversation_context()

            if context != "No previous conversation context.":
                # Include context in the query to the chat engine
                enhanced_query = f"""
Based on our conversation history:
{context}

Current question: {query}

Please provide a helpful response that takes into account our previous discussion if relevant."""
            else:
                enhanced_query = query

            # Get response from chat engine
            response = self._chat_engine.chat(enhanced_query)

            # Add to conversation history (this also updates shared memory)
            self.add_to_history("user", query)
            self.add_to_history("assistant", str(response))

            self.record_query(success=True)
            logger.debug("ConversationalAgent query processed successfully")

            return str(response)

        except Exception as e:
            logger.error(f"Error in ConversationalAgent.process_query: {e}")
            self.record_query(success=False)

            error_response = (
                f"I encountered an error while processing your question: {str(e)}. "
                "Could you please rephrase your question?"
            )
            # Still add error response to shared memory for context
            self._shared_memory.add_assistant_message(
                error_response, agent_name=self.name
            )
            return error_response

    def reset_conversation(self):
        """Reset the conversation history and chat engine."""
        self.clear_history()
        self._chat_engine.reset()
        logger.debug("ConversationalAgent conversation reset")

    def get_conversation_summary(self) -> str:
        """
        Get a summary of the conversation history.

        Returns:
            Formatted conversation summary
        """
        history = self.get_history()

        if not history:
            return "No conversation history available."

        summary_parts = ["Conversation Summary:\n"]

        for idx, message in enumerate(history, 1):
            role = message["role"].capitalize()
            content = message["content"]

            # Truncate long messages
            if len(content) > 200:
                content = content[:200] + "..."

            summary_parts.append(f"{idx}. {role}: {content}")

        return "\n".join(summary_parts)
