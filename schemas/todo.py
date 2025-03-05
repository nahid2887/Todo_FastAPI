from pydantic import BaseModel
from datetime import datetime

class TodoCreat(BaseModel):
    title :str
    description: str | None = None
    completed: bool = False

class TodoResponce(TodoCreat):
    id: int
    created_at: datetime

  