"""
Digiliencia Cybersecurity Chatbot - Traditional Streamlit UI

A streamlit-based chatbot interface for the INCIBE multi-agent system
with shared conversation memory across all agents.
"""

import json
import os
import re
import time
from datetime import datetime

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

from digiliencia.agents.agent_utils import (
    AgentConfig,
    get_performance_monitor,
    validate_config,
)
from digiliencia.agents.router_agent import RouterAgent
from digiliencia.agents.shared_memory import get_shared_memory, reset_shared_memory
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


def get_agent_emoji(agent_name: str) -> str:
    """Get emoji for agent type."""
    if not agent_name:
        return "🤖"
    if "News" in agent_name or "NEWS" in agent_name:
        return "📰"
    elif "Conversational" in agent_name or "CONVERSATIONAL" in agent_name:
        return "💬"
    return "🔀"


def render_ui():
    """Interfaz principal del sistema multi-agente."""
    try:
        env = Env()
        st.set_page_config(
            page_title="Digiliencia - Asistente de Ciberseguridad",
            page_icon="🛡️",
            layout="wide",
            initial_sidebar_state="expanded",
        )

        logger.info("Starting Digiliencia interface")
    except Exception as e:
        st.error(f"Error initializing UI: {e}")
        logger.error(f"UI initialization error: {e}")
        return

    # Header
    st.title("🛡️ Digiliencia")
    st.caption("Sistema de Inteligencia en Ciberseguridad con IA Multi-Agente")

    # Initialize shared memory reference in session state
    if "shared_memory" not in st.session_state:
        st.session_state.shared_memory = get_shared_memory()

    # Sidebar
    with st.sidebar:
        st.header("⚙️ Configuración")

        model_name = st.selectbox(
            "Modelo LLM",
            options=[
                env.chatbot_llm,
                "llama3.2:1b",
                "llama3.2:3b",
                "llama3.1:8b",
                "qwen2.5:7b",
            ],
            index=0,
            help="Selecciona el modelo de lenguaje",
        )

        with st.expander("Configuración Avanzada"):
            verbose_mode = st.checkbox("Modo Verbose", value=False)
            max_iterations = st.slider("Iteraciones Máximas", 1, 10, 5)
            timeout_seconds = st.slider("Timeout (segundos)", 30, 300, 180)

        st.divider()

        # Memory status
        st.header("🧠 Memoria Compartida")
        memory = st.session_state.shared_memory

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Mensajes", memory.message_count)
        with col2:
            st.metric("ID", memory.conversation_id[-6:])

        if st.button("🗑️ Limpiar Conversación", use_container_width=True):
            st.session_state.shared_memory = reset_shared_memory()
            if "messages" in st.session_state:
                st.session_state.messages = []
            if "agent_router" in st.session_state:
                del st.session_state.agent_router
            st.rerun()

        st.divider()

        # Agent info
        st.header("🤖 Agentes")
        st.markdown("""
        - **📰 NewsAgent**: Busca noticias de ciberseguridad
        - **💬 ConversationalAgent**: Responde preguntas generales
        - **🔀 RouterAgent**: Enruta al agente apropiado
        """)

        st.divider()

        # Metrics
        st.header("📊 Métricas")
        if st.button("Mostrar Métricas", use_container_width=True):
            monitor = get_performance_monitor()
            metrics = monitor.get_metrics()
            st.json(metrics)

    # Initialize RouterAgent - NO usar cache_resource para que comparta memoria
    if "agent_router" not in st.session_state:
        with st.spinner("Inicializando agentes..."):
            try:
                logger.info(f"Initializing AgentRouter with model: {model_name}")
                config = AgentConfig(
                    model_name=model_name,
                    verbose=verbose_mode,
                    max_iterations=max_iterations,
                    timeout_seconds=timeout_seconds,
                )

                validation_issues = validate_config(config)
                for issue in validation_issues:
                    if issue.startswith("ERROR"):
                        st.error(issue)
                    elif issue.startswith("WARNING"):
                        st.warning(issue)

                st.session_state.agent_router = RouterAgent(
                    model_name=model_name,
                    verbose=verbose_mode,
                    shared_memory=st.session_state.shared_memory,
                )
                logger.info("Agent router initialized successfully")
            except Exception as e:
                st.error(f"Error al inicializar el sistema de agentes: {e}")
                logger.error(f"Agent initialization failed: {e}")
                return

    agent_router = st.session_state.agent_router

    # Status bar
    status_col1, status_col2, status_col3 = st.columns(3)
    with status_col1:
        st.info(
            f"📝 **Memoria:** {st.session_state.shared_memory.message_count} mensajes"
        )
    with status_col2:
        last_agent = agent_router.get_last_agent_used()
        st.info(f"🤖 **Último agente:** {last_agent or 'Ninguno'}")
    with status_col3:
        st.info(f"🕐 **Hora:** {datetime.now().strftime('%H:%M:%S')}")

    st.divider()

    # Initialize messages in session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.conversation_id = int(time.time())
        logger.debug("Initializing new chat session")

        # Welcome message
        welcome_msg = """
¡Bienvenido a **Digiliencia**! 🛡️

Soy tu asistente de ciberseguridad. Puedo ayudarte con:

- 📰 **Noticias de ciberseguridad** - Amenazas, vulnerabilidades e incidentes
- 🎓 **Educación** - Conceptos y mejores prácticas
- 💡 **Consultas generales** - Cualquier pregunta sobre seguridad digital

**Memoria compartida activa**: Recuerdo toda la conversación, incluso cuando diferentes agentes te responden.

¿En qué puedo ayudarte?
        """
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": welcome_msg,
                "timestamp": time.time(),
                "agent": "Sistema",
            }
        )

    # Render chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            if message["role"] == "assistant":
                agent_name = message.get("agent", "")
                if agent_name:
                    emoji = get_agent_emoji(agent_name)
                    st.caption(f"{emoji} {agent_name}")
                process_think_content(message["content"])

                # Show metadata
                if "metadata" in message and message["metadata"]:
                    with st.expander("📋 Detalles"):
                        st.json(message["metadata"])
            else:
                st.markdown(message["content"])

    # Chat input
    if user_input := st.chat_input("Escribe tu pregunta sobre ciberseguridad..."):
        # Add user message to session state
        st.session_state.messages.append(
            {"role": "user", "content": user_input, "timestamp": time.time()}
        )

        with st.chat_message("user"):
            st.markdown(user_input)

        logger.info(f"New user query: {user_input[:100]}...")

        # Process with agent
        with st.chat_message("assistant"):
            start_time = time.time()

            with st.spinner("Procesando..."):
                try:
                    response = agent_router.send_msg(user_input)
                    processing_time = time.time() - start_time

                    if isinstance(response, dict) and "error" in response:
                        st.error(f"Error: {response['error']}")
                        response_content = response.get(
                            "fallback_response", str(response)
                        )
                        agent_used = "Error"
                    else:
                        response_content = str(response)
                        agent_used = agent_router.get_last_agent_used() or "RouterAgent"

                        # Show agent info
                        emoji = get_agent_emoji(agent_used)
                        st.caption(f"{emoji} {agent_used}")
                        process_think_content(response_content)

                    # Record metrics
                    monitor = get_performance_monitor()
                    monitor.record_request(
                        agent_type="router",
                        response_time=processing_time,
                        success="error"
                        not in (response if isinstance(response, dict) else {}),
                    )

                    # Build metadata
                    metadata = {
                        "tiempo_procesamiento": f"{processing_time:.2f}s",
                        "longitud_respuesta": len(response_content),
                        "modelo": model_name,
                        "agente": agent_used,
                        "timestamp": datetime.now().isoformat(),
                        "memoria_mensajes": st.session_state.shared_memory.message_count,
                    }

                    try:
                        routing_stats = agent_router.get_routing_stats()
                        metadata["routing"] = routing_stats
                    except Exception as e:
                        logger.warning(f"Could not get routing stats: {e}")

                except Exception as e:
                    error_message = f"Ha ocurrido un error: {e}"
                    st.error(error_message)
                    response_content = error_message
                    agent_used = "Error"
                    metadata = {
                        "error": str(e),
                        "tiempo_procesamiento": f"{time.time() - start_time:.2f}s",
                    }
                    logger.error(f"Query failed: {e}")

        # Add assistant message to session state
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response_content,
                "metadata": metadata,
                "timestamp": time.time(),
                "agent": agent_used,
            }
        )

        st.rerun()

    # Bottom action buttons
    st.divider()
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📊 Métricas de Agentes", use_container_width=True):
            try:
                metrics = agent_router.get_agent_metrics()
                st.json(metrics)
            except Exception as e:
                st.error(f"Error: {e}")

    with col2:
        if st.button("📜 Ver Memoria Compartida", use_container_width=True):
            history = agent_router.get_conversation_history()
            if history:
                st.subheader("Historial de Memoria")
                for msg in history:
                    role_icon = "👤" if msg["role"] == "user" else "🤖"
                    agent_info = (
                        f" ({msg.get('agent_name', '')})"
                        if msg.get("agent_name")
                        else ""
                    )
                    content = (
                        msg["content"][:300] + "..."
                        if len(msg["content"]) > 300
                        else msg["content"]
                    )
                    st.markdown(
                        f"**{role_icon} {msg['role'].capitalize()}{agent_info}:**"
                    )
                    st.markdown(f"> {content}")
                    st.divider()
            else:
                st.info("No hay historial disponible")

    with col3:
        if st.button("💾 Exportar Conversación", use_container_width=True):
            if st.session_state.messages:
                conversation_data = {
                    "conversation_id": st.session_state.conversation_id,
                    "shared_memory": st.session_state.shared_memory.export_conversation(),
                    "ui_messages": st.session_state.messages,
                    "export_time": datetime.now().isoformat(),
                }
                json_str = json.dumps(
                    conversation_data, indent=2, default=str, ensure_ascii=False
                )
                st.download_button(
                    label="📥 Descargar JSON",
                    data=json_str,
                    file_name=f"digiliencia_{st.session_state.conversation_id}.json",
                    mime="application/json",
                )
            else:
                st.info("No hay conversación para exportar")


if __name__ == "__main__":
    logger.info("Running Digiliencia interface in standalone mode")
    render_ui()
