import os
from pathlib import Path
from dotenv import load_dotenv

def carregar_configuracoes_ambiente():
    "Carrega as configurações das variáveis de ambiente a fim de conectar ao banco de dados"
    dotenv_path = Path.cwd() / ".env"
    load_dotenv(dotenv_path=dotenv_path)

    settings = {
        "POSTGRES_HOST": os.getenv("POSTGRES_HOST"),
        "POSTGRES_USER": os.getenv("POSTGRES_USER"),
        "POSTGRES_PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "POSTGRES_DB": os.getenv("POSTGRES_DB"),
        "POSTGRES_PORT": os.getenv("POSTGRES_PORT")
    }

    return settings

