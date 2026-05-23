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
        self.opensearch_host = os.getenv("OPENSEARCH_HOST", "localhost")
        self.opensearch_port = int(os.getenv("OPENSEARCH_PORT", 9200))
        self.opensearch_user = os.getenv("OPENSEARCH_USER", "admin")
        self.opensearch_password = os.getenv("OPENSEARCH_PASSWORD", "")
        self.opensearch_index = os.getenv("OPENSEARCH_INDEX", "movie_search_index")
        self.embedding_model = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
