from fastapi import APIRouter, HTTPException


router = APIRouter(
    prefix="/todos",
    tags=["todos"]
)


@router.get("/")
async def get_todos():
    pass


@router.get("/{id}")
async def get_todo_by_id(id):
    pass


@router.post("/create-todo")
async def create_todo():
    pass


@router.put("/update-todo")
async def update_todo():
    pass


@router.delete("/delete-todo")
async def delete_todo():
    pass