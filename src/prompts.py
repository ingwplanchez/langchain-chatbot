from langchain_core.prompts import PromptTemplate

# Definición del template de prompt con comportamiento específico
CHATBOT_PRO_TEMPLATE = PromptTemplate(
    input_variables=["mensaje", "historial"],
    template="""Eres un asistente útil y amigable llamado ChatBot Pro.

Historial de conversación:
{historial}

Responde de manera clara y concisa a la siguiente pregunta: {mensaje}"""
)
