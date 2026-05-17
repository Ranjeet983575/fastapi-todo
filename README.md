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
