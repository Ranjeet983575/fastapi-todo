from sqlalchemy.orm import Session
from app.models.todo import Todo
from app.database import SessionLocal
from fastapi import HTTPException

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_todos():
    db = SessionLocal()
    todos = db.query(Todo).all()
    db.close()
    return [todo.item for todo in todos]

def add_todo(item: str):
    db = SessionLocal()
    db_todo = Todo(item=item)
    db.add(db_todo)
    try:
        db.commit()
        db.refresh(db_todo)
    except Exception as e:
        db.rollback()
        db.close()
        raise HTTPException(status_code=400, detail="Item already exists or DB error")
    db.close()
    return db_todo.item

def delete_todo(item: str):
    db = SessionLocal()
    db_todo = db.query(Todo).filter(Todo.item == item).first()
    if not db_todo:
        db.close()
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_todo)
    db.commit()
    db.close()
    return item
