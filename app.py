import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# Importaciones desde la carpeta src
from src.config import load_config
from src.chatbot import get_chatbot_chain

# Carga de configuración
try:
    config = load_config()
    api_key = config["api_key"]
except Exception as e:
    st.error(f"Error de configuración: {e}")
    st.stop()

# Configuración inicial de la página
st.set_page_config(page_title="Chatbot Básico", page_icon="🤖")
st.title("🤖 Chatbot Básico con LangChain")
st.markdown("Este es un *chatbot de ejemplo* construido con LangChain + Streamlit. ¡Escribe tu mensaje abajo para comenzar!")

# Barra lateral de configuración
with st.sidebar:
    st.header("Configuración")
    temperature = st.slider("Temperatura", 0.0, 1.0, 0.5, 0.1)
    model_name = st.selectbox("Modelo", ["gemini-3.1-flash-lite", "gemini-2.0-flash", "gemini-1.5-flash"])

# Inicializar la cadena del chatbot basándose en la configuración de la barra lateral
cadena = get_chatbot_chain(model_name, temperature, api_key)

# Inicializar el historial de mensajes en session_state
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

# Renderizar historial existente
for msg in st.session_state.mensajes:
    if isinstance(msg, SystemMessage):
        continue  # no mostrar mensajes del sistema al usuario

    role = "assistant" if isinstance(msg, AIMessage) else "user"
    with st.chat_message(role):
        st.markdown(msg.content)

# Botón para limpiar conversación
if st.button("🗑️ Nueva conversación"):
    st.session_state.mensajes = []
    st.rerun()

# Input de usuario
pregunta = st.chat_input("Escribe tu mensaje:")

if pregunta:
    # Mostrar y almacenar mensaje del usuario
    with st.chat_message("user"):
        st.markdown(pregunta)

    # Generar y mostrar respuesta del asistente
    try:
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            full_response = ""

            # Streaming de la respuesta
            for chunk in cadena.stream({"mensaje": pregunta, "historial": st.session_state.mensajes}):
                # Extraer el texto si el contenido es una lista (bloques)
                content = chunk.content
                if isinstance(content, list):
                    text_chunk = content[0].get('text', '') if content else ""
                else:
                    text_chunk = content

                full_response += text_chunk
                response_placeholder.markdown(full_response + "▌")

            response_placeholder.markdown(full_response)

        st.session_state.mensajes.append(HumanMessage(content=pregunta))
        st.session_state.mensajes.append(AIMessage(content=full_response))

    except Exception as e:
        st.error(f"Error al generar respuesta: {str(e)}")
        st.info("Verifica que tu API Key de Google Gemini esté configurada correctamente.")
