from pydantic import BaseModel, Field


class TodoRequest(BaseModel):
    title: str = Field(max_length=50, min_length=3, example="Buy groceries")
    description: str = Field(max_length=300, min_length=3, example="Buy milk, eggs, and bread")
    priority: int = Field(gt=0, lt=6, example=3)
    completed: bool = Field(default=False, example=False)


class UserRequest(BaseModel):
    email: str = Field(max_length=100, example="user@example.com")
    password: str = Field(max_length=100, example="password123")
    username: str = Field(max_length=50, example="johndoe")
    full_name: str = Field(max_length=100, example="John Doe")
    role: str = Field(max_length=50, example="user")


class TokenResponse(BaseModel):
    access_token: str
    token_type: str