from starlette import status
from http.client import HTTPException
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from fastapi import Depends
from database import SessionLocal
from jose import JWTError, jwt

from models import Users


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: db_dependency):
    payload = jwt.decode(token, options={"verify_signature": False})
    user = db.query(Users).filter(Users.id == payload.get("sub")).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
    return user

current_user_dependency = Annotated[Users, Depends(get_current_user)]
