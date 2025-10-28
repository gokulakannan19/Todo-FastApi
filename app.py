from fastapi import FastAPI
from routes import todos
from database import Base, engine
import models


app = FastAPI()

app.include_router(todos.router)

models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}