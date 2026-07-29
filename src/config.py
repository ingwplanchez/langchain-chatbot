import os
from dotenv import load_dotenv

def load_config():
    """Carga las variables de entorno y retorna la configuración."""
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("La variable de entorno GOOGLE_API_KEY no está configurada.")
    return {"api_key": api_key}
