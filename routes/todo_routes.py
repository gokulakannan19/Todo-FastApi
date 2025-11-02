from fastapi import APIRouter, HTTPException
from starlette import status
from dependency import db_dependency, current_user_dependency
from models import Todos
from schemas import TodoRequest


router = APIRouter(
    prefix="/todos",
    tags=["todos"]
)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_todos(db: db_dependency, user: current_user_dependency):
    todos = db.query(Todos).filter(Todos.owner_id == user.id).all()
    return todos


@router.get("/{todo_id}", status_code=status.HTTP_200_OK)
async def get_todo_by_id(db: db_dependency, user: current_user_dependency, todo_id):
    todo = db.query(Todos).filter(Todos.id == todo_id, Todos.owner_id == user.id).first()
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No todo found")
    return todo


@router.post("/create-todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, user: current_user_dependency, request: TodoRequest):
    todo = Todos(**request.model_dump(), owner_id=user.id)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


@router.put("/update-todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(db: db_dependency, user: current_user_dependency, request: TodoRequest, todo_id):
    todo = db.query(Todos).filter(Todos.id == todo_id, Todos.owner_id == user.id).first()
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    for key, value in request.model_dump().items():
        setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return todo


@router.delete("/delete-todo/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, user: current_user_dependency, todo_id):
    todo = db.query(Todos).filter(Todos.id == todo_id, Todos.owner_id == user.id).first()
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return {"detail": "Todo deleted successfully"}
