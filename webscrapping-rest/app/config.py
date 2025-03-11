from dotenv import load_dotenv
import os

# Cargar variables desde el archivo .env
load_dotenv()

# Configuración de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL")

# Token de autenticación de la API
API_SECRET_KEY = os.getenv("API_SECRET_KEY")

# Configuración de tiempos de espera para scraping
MIN_TIMEOUT = int(os.getenv("MIN_TIMEOUT", 120))  # 2 minutos por defecto
MAX_TIMEOUT = int(os.getenv("MAX_TIMEOUT", 300))  # 5 minutos por defecto
