import json
import os
import re
import time

import nest_asyncio
import streamlit as st
from loguru import logger

# Configuraciones para evitar conflictos
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["PYTORCH_DISABLE_WARN"] = "1"
try:
    nest_asyncio.apply()
except RuntimeError:
    pass

from digiliencia.agents.agent_utils import (AgentConfig,
                                            get_performance_monitor,
                                            validate_config)
from digiliencia.agents.router_agent import RouterAgent
from digiliencia.configs.env import Env


def process_think_content(content: str) -> None:
    """
    Procesa contenido con <think> en bloques colapsables.
    """
    think_pattern = r"<think>(.*?)</think>"
    matches = list(re.finditer(think_pattern, content, re.DOTALL))

    if not matches:
        st.markdown(content)
        return

    current_pos = 0
    for match in matches:
        before_think = content[current_pos : match.start()]
        if before_think.strip():
            st.markdown(before_think)

        think_content = match.group(1).strip()
        with st.expander("💭 Proceso de pensamiento", expanded=False):
            st.markdown(think_content)

        current_pos = match.end()

    after_think = content[current_pos:]
    if after_think.strip():
        st.markdown(after_think)


def render_ui():
    """Interfaz principal de RAG con agentes inteligentes."""
    try:
        env = Env()
        st.set_page_config(
            page_title="Medical Knowledge RAG System",
            page_icon="🧠",
            layout="wide",
            initial_sidebar_state="expanded",
        )

        st.title("🧠 Medical Knowledge RAG System")
        st.markdown(
            "**Enhanced AI system for medical knowledge queries and conversations**"
        )
        logger.info("Starting RAG user interface")
    except Exception as e:
        st.error(f"Error initializing UI: {e}")
        logger.error(f"UI initialization error: {e}")
        return

    # Sidebar
    with st.sidebar:
        st.header("⚙️ Configuration")

        model_name = st.selectbox(
            "Model",
            options=[env.chatbot_llm, "llama3.2:1b", "llama3.2:3b", "llama3.1:8b"],
            index=0,
            help="Select the LLM model to use",
        )

        with st.expander("Advanced Settings"):
            verbose_mode = st.checkbox("Verbose Logging", value=False)
            max_iterations = st.slider("Max Tool Iterations", 1, 10, 5)
            timeout_seconds = st.slider("Timeout (seconds)", 30, 300, 180)

        # Métricas globales
        st.header("📊 Performance Metrics")
        if st.button("Show Metrics"):
            monitor = get_performance_monitor()
            metrics = monitor.get_metrics()
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Total Requests", metrics.get("total_requests", 0))
                st.metric("Success Rate", f"{metrics.get('success_rate', 0):.1f}%")
            with col2:
                st.metric("Avg Response Time", f"{metrics.get('average_response_time', 0):.2f}s")
                st.metric("Requests/Min", metrics.get("requests_per_minute", 0))

    # Inicializar RouterAgent cacheado
    @st.cache_resource
    def get_agent_router(model_name: str, verbose: bool, max_iter: int, timeout: int):
        logger.info(f"Initializing AgentRouter with model: {model_name}")
        config = AgentConfig(
            model_name=model_name,
            verbose=verbose,
            max_iterations=max_iter,
            timeout_seconds=timeout,
        )

        validation_issues = validate_config(config)
        for issue in validation_issues:
            if issue.startswith("ERROR"):
                st.error(issue)
                logger.error(issue)
            elif issue.startswith("WARNING"):
                st.warning(issue)
                logger.warning(issue)

        return RouterAgent(model_name=model_name, verbose=verbose)

    try:
        agent_router = get_agent_router(
            model_name, verbose_mode, max_iterations, timeout_seconds
        )
        logger.info("Agent router initialized successfully")
    except Exception as e:
        st.error(f"Failed to initialize agent system: {e}")
        logger.error(f"Agent initialization failed: {e}")
        return

    # Chat
    st.header("💬 Chat Interface")
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.conversation_id = int(time.time())
        logger.debug("Initializing new chat session")

    # Render historial
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            if message["role"] == "assistant":
                process_think_content(message["content"])
            else:
                st.markdown(message["content"])
            if message["role"] == "assistant" and "metadata" in message:
                with st.expander("Response Details"):
                    st.json(message["metadata"])

    # Entrada usuario
    if user_input := st.chat_input(
        "Ask about medical conditions, treatments, or general questions..."
    ):
        st.session_state.messages.append(
            {"role": "user", "content": user_input, "timestamp": time.time()}
        )
        with st.chat_message("user"):
            st.markdown(user_input)
        logger.info(f"New user query: {user_input[:100]}...")

        with st.chat_message("assistant"):
            start_time = time.time()
            with st.spinner("Processing your query..."):
                try:
                    response = agent_router.send_msg(user_input)
                    if isinstance(response, dict) and "error" in response:
                        st.error(f"Error: {response['error']}")
                        response_content = response.get("fallback_response", str(response))
                    else:
                        response_content = str(response)
                        process_think_content(response_content)

                    processing_time = time.time() - start_time
                    monitor = get_performance_monitor()
                    monitor.record_request(
                        agent_type="router",
                        response_time=processing_time,
                        success="error" not in (response if isinstance(response, dict) else {}),
                    )

                    metadata = {
                        "processing_time": f"{processing_time:.2f}s",
                        "response_length": len(response_content),
                        "model_used": model_name,
                        "timestamp": time.time(),
                    }
                    try:
                        routing_stats = agent_router.get_routing_stats()
                        metadata["routing_info"] = {
                            "total_queries": routing_stats["total_queries"],
                            "agent_usage": routing_stats["agent_usage_percentage"],
                        }
                    except Exception as e:
                        logger.warning(f"Could not get routing stats: {e}")
                except Exception as e:
                    error_message = f"An error occurred: {e}"
                    st.error(error_message)
                    response_content = error_message
                    metadata = {"error": str(e), "processing_time": f"{time.time() - start_time:.2f}s"}
                    logger.error(f"Query failed: {e}")

        st.session_state.messages.append(
            {"role": "assistant", "content": response_content, "metadata": metadata, "timestamp": time.time()}
        )

    # Extras
    with st.expander("🛠️ Available Tools"):
        try:
            tools = agent_router.get_available_tools()
            if tools:
                for tool in tools:
                    st.write(f"**{tool['name']}**: {tool['description']}")
            else:
                st.info("No tools available or agent not initialized")
        except Exception as e:
            st.error(f"Could not retrieve tools: {e}")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🗑️ Clear Conversation"):
            st.session_state.messages = []
            try:
                agent_router.reset_conversation()
                st.success("Conversation cleared successfully")
                logger.info("Conversation cleared by user")
            except Exception as e:
                st.error(f"Error clearing conversation: {e}")
                logger.error(f"Failed to clear conversation: {e}")
            st.rerun()
    with col2:
        if st.button("📊 Show Agent Metrics"):
            try:
                metrics = agent_router.get_agent_metrics()
                st.json(metrics)
            except Exception as e:
                st.error(f"Could not retrieve agent metrics: {e}")
    with col3:
        if st.button("💾 Export Conversation"):
            if st.session_state.messages:
                conversation_data = {
                    "conversation_id": st.session_state.conversation_id,
                    "messages": st.session_state.messages,
                    "export_time": time.time(),
                }
                json_str = json.dumps(conversation_data, indent=2, default=str)
                st.download_button(
                    label="Download JSON",
                    data=json_str,
                    file_name=f"conversation_{st.session_state.conversation_id}.json",
                    mime="application/json",
                )
            else:
                st.info("No conversation to export")


if __name__ == "__main__":
    logger.info("Running RAG interface in standalone mode")
    render_ui()
