from pydantic import BaseModel, Field


class TodoRequest(BaseModel):
    title: str = Field(max_length=50, min_length=3, example="Buy groceries")
    description: str = Field(max_length=300, min_length=3, example="Buy milk, eggs, and bread")
    priority: int = Field(gt=0, lt=6, example=3)
    completed: bool = Field(default=False, example=False)