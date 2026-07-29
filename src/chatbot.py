from langchain_google_genai import ChatGoogleGenerativeAI
from .prompts import CHATBOT_PRO_TEMPLATE

def get_chatbot_chain(model_name: str, temperature: float, api_key: str):
    """
    Crea y retorna la cadena LCEL para el chatbot.
    """
    chat_model = ChatGoogleGenerativeAI(
        model=model_name,
        temperature=temperature,
        api_key=api_key
    )

    # Crear cadena usando LCEL (LangChain Expression Language)
    cadena = CHATBOT_PRO_TEMPLATE | chat_model
    return cadena
