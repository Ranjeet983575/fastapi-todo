# FastAPI TODO Application

A simple TODO application built with FastAPI.

## Features
- Add, list, and delete TODO items
- Modular structure with routers and services

## Requirements
 `uvicorn` (for serving the application)
 `FastAPI` (the web framework)
   ```sh
   pip install uv
   ```

2. **Install dependencies:**
   ```sh
   uv pip install --system
   ```

3. **Run the application:**
   ```sh
   uvicorn app.main:app --reload
   ```

4. **Access the API docs:**
   - Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.

## Notes
- The TODO list is in-memory and will reset on server restart.
- `astral` is included as a dependency as requested, but not used in the core logic.

[
  {
    "title": "Interstellar",
    "description": "A team of explorers travel through a wormhole in space to ensure humanity's survival.",
    "genre": "Sci-Fi",
    "release_year": 2014
  },
  {
    "title": "Inception",
    "description": "A thief steals corporate secrets through dream-sharing technology.",
    "genre": "Sci-Fi",
    "release_year": 2010
  },
  {
    "title": "The Dark Knight",
    "description": "Batman faces the Joker, a criminal mastermind who wants to plunge Gotham into chaos.",
    "genre": "Action",
    "release_year": 2008
  },
  {
    "title": "Titanic",
    "description": "A love story unfolds aboard the ill-fated RMS Titanic.",
    "genre": "Romance",
    "release_year": 1997
  },
  {
    "title": "The Matrix",
    "description": "A hacker discovers reality is a simulation controlled by machines.",
    "genre": "Sci-Fi",
    "release_year": 1999
  },
  {
    "title": "Avengers: Endgame",
    "description": "The Avengers assemble for one final fight to undo Thanos' snap.",
    "genre": "Action",
    "release_year": 2019
  },
  {
    "title": "Forrest Gump",
    "description": "The life journey of a simple man with a kind heart through major historical events.",
    "genre": "Drama",
    "release_year": 1994
  },
  {
    "title": "Gladiator",
    "description": "A betrayed Roman general seeks revenge against the corrupt emperor.",
    "genre": "Action",
    "release_year": 2000
  },
  {
    "title": "The Shawshank Redemption",
    "description": "Two imprisoned men bond over years, finding hope and redemption.",
    "genre": "Drama",
    "release_year": 1994
  },
  {
    "title": "Jurassic Park",
    "description": "Dinosaurs are cloned and a theme park becomes a deadly disaster.",
    "genre": "Adventure",
    "release_year": 1993
  }
]