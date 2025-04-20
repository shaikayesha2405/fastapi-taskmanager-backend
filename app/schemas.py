from pydantic import BaseModel
from datetime import date
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[date] = None

class TaskCreate(TaskBase):
    pass  # For now, it’s the same as TaskBase

class Task(TaskBase):
    id: int
    status: bool

    class Config:
        orm_mode = True
