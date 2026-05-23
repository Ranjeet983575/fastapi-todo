from sentence_transformers import SentenceTransformer
from app.services.config import Config


class EmbeddingService:

    def __init__(self, config: Config = None):

        self.config = config or Config()

        self.model = SentenceTransformer(
            self.config.embedding_model
        )

    def generate_embedding(self, text: str):

        embedding = self.model.encode(text)

        return embedding.tolist()