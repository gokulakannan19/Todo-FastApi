# Todo Project Backend (FastAPI)

This is a simple Todo backend API built with [FastAPI](https://fastapi.tiangolo.com/).

## Features
- Create, read, update, and delete todo items (CRUD)
- Fast, async, and easy to use
- Interactive API docs (Swagger UI and ReDoc)
- Ready for integration with any frontend

## Requirements
- Python 3.8+
- FastAPI
- Uvicorn
- (Optional) SQLAlchemy, Databases, Alembic for persistence

## Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Todo-FastApi
   ```
2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies**
   ```bash
   pip install fastapi uvicorn
   # Add other dependencies as needed
   ```
4. **Run the server**
   ```bash
   uvicorn main:app --reload
   ```
   Replace `main:app` with your FastAPI app's import path if different.

## API Documentation
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Example Endpoints
- `GET /todos` — List all todos
- `POST /todos` — Create a new todo
- `GET /todos/{id}` — Get a todo by ID
- `PUT /todos/{id}` — Update a todo
- `DELETE /todos/{id}` — Delete a todo

## Project Structure
```
.
├── main.py           # FastAPI app entrypoint
├── models.py         # Pydantic models / ORM models
├── crud.py           # CRUD operations
├── database.py       # Database connection (if used)
├── requirements.txt  # Python dependencies
└── ...
```

## License
MIT
