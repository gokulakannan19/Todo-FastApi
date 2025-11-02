from fastapi import FastAPI
import models
from routes import todo_routes
from database import Base, engine



app = FastAPI()
app.include_router(todo_routes.router)
models.Base.metadata.create_all(engine)


@app.get("/")
async def root():
    return {"Get your todos"}
