import os
from pathlib import Path
from dotenv import load_dotenv


class Config:
    def __init__(self, env_file: str = None):
        dotenv_path = (
            Path(env_file).resolve() if env_file else Path(__file__).resolve().parents[1] / ".env"
        )
        load_dotenv(dotenv_path)
        
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        self.groq_model = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
