from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database import Base


class Todos(Base):

    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    priority = Column(Integer, nullable=False)
    completed = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("Users.id"))


class Users(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)
    username = Column(String(50), unique=True, nullable=False)
    full_name = Column(String(100), nullable=True)
    role = Column(String(50), default="user")