from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Todos(Base):

    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    priority = Column(Integer, nullable=False)
    completed = Column(Boolean, default=False)