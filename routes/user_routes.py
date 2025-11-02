from datetime import timedelta
from typing import Annotated
from starlette import status
from fastapi import APIRouter, Depends, HTTPException
from dependency import db_dependency
from models import Users
from schemas import TokenResponse, UserRequest
from config import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, pwd_context
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register")
async def register(db: db_dependency, request: UserRequest):
    user = Users(
        email=request.email,
        password=pwd_context.hash(request.password),
        username=request.username,
        full_name=request.full_name,
        role=request.role,
        is_active=True
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.post("/login", response_model=TokenResponse)
async def login(db: db_dependency, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
    data = {"sub": user.username, "role": user.role, "id": user.id, "username": user.username}
    token = create_access_token(data, timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return {"access_token": token, "token_type": "Bearer"}


def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User Not found")
    if not pwd_context.verify(password, user.password):
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    return user
