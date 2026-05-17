from fastapi import APIRouter, HTTPException
from app.services import todo_service
from typing import List

router = APIRouter(prefix="/todos", tags=["todos"])

@router.get("/", response_model=List[str])
def get_todos():
    return todo_service.get_todos()

@router.post("/", response_model=str)
def add_todo(item: str):
    return todo_service.add_todo(item)

@router.delete("/{item}", response_model=str)
def delete_todo(item: str):
    return todo_service.delete_todo(item)
