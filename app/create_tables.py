from app.database import engine
from app.models.todo import Todo

# Create tables
Todo.metadata.create_all(bind=engine)
print("Tables created.")
