#/models/todo.py
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from database.database import Base
import pytz

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(String(500), nullable=True)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=lambda: datetime.now(pytz.timezone('Asia/Dhaka')))

    def __repr__(self):
        return f"<Todo(id={self.id}, title='{self.title}', completed={self.completed})>"