from sqlalchemy import Column, Integer, String, Boolean, Date
from .database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(Boolean, default=False)  # False = pending, True = done
    due_date = Column(Date)
