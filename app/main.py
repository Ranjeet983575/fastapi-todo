from fastapi import FastAPI
from app.routers import movie_search_router, todo_router
from app.routers import llm_router

app = FastAPI()

app.include_router(todo_router.router)
app.include_router(llm_router.router)
app.include_router(movie_search_router.router)
