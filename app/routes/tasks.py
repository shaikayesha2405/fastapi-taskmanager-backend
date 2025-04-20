from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import get_db

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)

@router.get("/", response_model=list[schemas.Task])
def get_all_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)

@router.get("/{task_id}", response_model=schemas.Task)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.delete_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}

@router.put("/{task_id}/done", response_model=schemas.Task)
def mark_task_done(task_id: int, db: Session = Depends(get_db)):
    task = crud.mark_done(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
