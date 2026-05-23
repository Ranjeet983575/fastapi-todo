from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

from app.services.movie_search_service import MovieSearchService


router = APIRouter(
    prefix="/movie-search",
    tags=["movie-search"]
)

movie_search_service = MovieSearchService()


# =========================
# Request Models
# =========================

class MovieRequest(BaseModel):
    movie_id: str
    title: str
    description: str
    genre: str
    release_year: int


class SearchRequest(BaseModel):
    query: str
    size: Optional[int] = 5


# =========================
# Create Index API
# =========================

@router.post("/create-index")
def create_index():

    try:

        movie_search_service.create_index()

        return {
            "message": "Movie index created successfully"
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# =========================
# Index Movie API
# =========================

@router.post("/index")
def index_movie(movie: MovieRequest):

    try:

        movie_search_service.index_movie(
            movie_id=movie.movie_id,
            title=movie.title,
            description=movie.description,
            genre=movie.genre,
            release_year=movie.release_year
        )

        return {
            "message": "Movie indexed successfully"
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# =========================
# Search Movies API
# =========================

@router.post("/search")
def search_movies(request: SearchRequest):

    try:

        results = movie_search_service.search_movies(
            query=request.query,
            size=request.size
        )

        formatted_results = []

        for result in results:

            formatted_results.append({
                "id": result["_id"],
                "score": result["_score"],
                "movie": result["_source"]
            })

        return {
            "total_results": len(formatted_results),
            "results": formatted_results
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@router.get("/all")
def get_all_movies():

    try:

        results = movie_search_service.get_all_movies()
        return {"documents": results}

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )        