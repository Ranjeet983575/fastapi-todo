from typing import List, Dict, Any

from app.services.open_search_service import OpenSearchService
from app.services.config import Config


class MovieSearchService:

    def __init__(self, config: Config = None):
        self.config = config or Config()
        self.opensearch_service = OpenSearchService(self.config)
        self.client = self.opensearch_service.get_client()

    # =========================
    # Create Index
    # =========================
    def create_index(self) -> Dict[str, Any]:

        index_name = self.config.opensearch_index

        if self.client.indices.exists(index=index_name):
            return {
                "message": f"Index '{index_name}' already exists",
                "created": False
            }

        mapping = {
            "settings": {
                "index": {
                    "number_of_shards": 1,
                    "number_of_replicas": 0
                }
            },
            "mappings": {
                "properties": {
                    "title": {"type": "text"},
                    "description": {"type": "text"},
                    "genre": {"type": "keyword"},
                    "release_year": {"type": "integer"}
                }
            }
        }

        self.client.indices.create(
            index=index_name,
            body=mapping
        )

        return {
            "message": f"Index '{index_name}' created successfully",
            "created": True
        }

    # =========================
    # Index Movie
    # =========================
    def index_movie(
        self,
        movie_id: str,
        title: str,
        description: str,
        genre: str,
        release_year: int
    ) -> Dict[str, Any]:

        document = {
            "title": title,
            "description": description,
            "genre": genre,
            "release_year": release_year
        }

        response = self.client.index(
            index=self.config.opensearch_index,
            id=movie_id,
            body=document,
            refresh=True
        )

        return {
            "message": "Movie indexed successfully",
            "movie_id": movie_id,
            "result": response.get("result")
        }

    # =========================
    # Full-Text Search
    # =========================
    
    def search_movies(self, query: str, size: int = 5):

        body = {
            "size": size,
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["title^3", "description", "genre"]
                }
            }
        }

        resp = self.client.search(index=self.config.opensearch_index, body=body)
        hits = [hit["_source"] for hit in resp["hits"]["hits"]]
        return {"results": hits, "total": resp["hits"]["total"]["value"]}
            
    # =========================
    # Get All Movies
    # =========================
    def get_all_movies(self) -> List[Dict[str, Any]]:

        resp = self.client.search(index=self.config.opensearch_index, body={"query": {"match_all": {}}}, size=1000)
        docs = []
        for hit in resp["hits"]["hits"]:
            doc = hit["_source"]
            doc["_id"] = hit["_id"]
            docs.append(doc)
        return docs
