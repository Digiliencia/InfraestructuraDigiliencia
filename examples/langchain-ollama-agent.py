import random
import wikipedia
import streamlit as st
from langchain.agents import AgentExecutor, create_react_agent
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate
from langchain.tools import tool
from pydantic import BaseModel, Field
import requests
import time
from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema.agent import AgentAction, AgentFinish
from langchain_ollama import OllamaLLM


# --- Tool 1: Wikipedia Article Exporter ---
class WikipediaArticleExporter(BaseModel):
    article: str = Field(description="The canonical name of the Wikipedia article")


@tool(
    "wikipedia_text_exporter", args_schema=WikipediaArticleExporter, return_direct=False
)
def wikipedia_text_exporter(article: str) -> dict:
    """Fetches the content of a Wikipedia article."""
    article = article.strip()

    try:
        wiki = wikipedia.page(article)
        text = wiki.content
        text = text.replace("==", "")
        text = text.replace("\n", "")[:-12]
        return {"text": text}

    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch Wikipedia article: {e}"}
    except KeyError as e:
        return {"error": f"Unexpected response structure from Wikipedia API: {e}"}


# --- Tool 2: Weather Fetcher ---
class Weather(BaseModel):
    city: str = Field(description="The name of the city to fetch the weather for")


@tool("current_temperature_in", args_schema=Weather, return_direct=False)
def current_temperature_in(city: str) -> dict[str, str]:
    """Fetches the current temperature of a given city."""
    temp = random.randint(-10, 30)
    print(f"Fetching temperature for {city.strip()}...")
    return {f"{city}": f"{temp}ºC"}


@tool("current_sky_condition_in", args_schema=Weather, return_direct=False)
def current_sky_condition_in(city: str) -> dict[str, str]:
    """Fetches the current sky condition of a given city."""
    sky_conditions = ["Clear", "Cloudy", "Partly cloudy", "Rainy", "Stormy"]
    condition = random.choice(sky_conditions)
    print(f"Fetching sky condition for {city.strip()}...")
    return {f"{city}": condition}


# --- LLM and Prompt Setup ---
llm = OllamaLLM(model="mixtral:8x7b", temperature=0)

# Load the prompt template from file
with open("examples/prompts/improved_prompt.txt", "r") as file:
    prompt_content = file.read()

prompt = ChatPromptTemplate.from_template(template=prompt_content)

# --- Tools List ---
tools = [current_temperature_in, current_sky_condition_in, wikipedia_text_exporter]


# --- Custom Callback Handler Mejorado para Streamlit ---
class CustomCallbackHandler(BaseCallbackHandler):
    """Callback mejorado para mostrar pensamientos, acciones y resultados en Streamlit."""

    def __init__(self):
        self.thoughts = []
        self.actions = []
        self.tool_outputs = []

    def on_agent_action(self, action: AgentAction, **kwargs):
        self.thoughts.append(f"🧠 **Pensamiento:** {action.log}")
        self.actions.append(
            f"🔨 **Acción:** Tool: {action.tool}, Input: {action.tool_input}"
        )

    def on_tool_end(self, output, **kwargs):
        self.tool_outputs.append(f"📤 **Resultado de la herramienta:** {output}")

    def on_agent_finish(self, finish: AgentFinish, **kwargs):
        self.thoughts.append(
            f"✅ **Resultado Final:** {finish.return_values['output']}"
        )

    def display_logs(self):
        for thought in self.thoughts:
            st.markdown(thought)
        for action in self.actions:
            st.markdown(action)
        for output in self.tool_outputs:
            st.markdown(output)


# --- Agent and Executor Setup ---
callback_handler = CustomCallbackHandler()
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True,
    callbacks=[callback_handler],
)

# --- Memory Setup ---
chat_history = ConversationBufferMemory(k=10)

# --- Streamlit UI ---
st.title("🤖 Agente Interactivo con LangChain y Streamlit")


# --- Chat History Management ---
def append_chat_history(input_text: str, response: str):
    """Saves the input and response to chat history."""
    chat_history.save_context({"input": input_text}, {"output": response})


# --- User Input Section ---
user_input = st.text_input("🗨️ Escribe tu mensaje:")

if st.button("Enviar"):
    if user_input:
        memory_context = chat_history.load_memory_variables({})
        msg = {"input": user_input, "chat_history": memory_context}

        try:
            response = agent_executor.invoke(msg)
            append_chat_history(user_input, response["output"])

            st.write("🤖 **Respuesta del Agente:**", response["output"])

            # Mostrar pensamientos, acciones y resultados
            callback_handler.display_logs()
        except Exception as e:
            st.error(f"❗ Error durante la ejecución del agente: {e}")

# --- Display Chat History ---
if st.checkbox("Mostrar Historial de Conversación"):
    memory_vars = chat_history.load_memory_variables({})
    st.write(memory_vars.get("history", "Historial vacío."))
