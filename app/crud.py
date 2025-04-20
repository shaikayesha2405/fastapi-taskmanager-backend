from sqlalchemy.orm import Session
from . import models, schemas

# Create a task
def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Get all tasks
def get_tasks(db: Session):
    return db.query(models.Task).all()

# Get single task
def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

# Delete task
def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task

# Update task status
def mark_done(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        task.status = True
        db.commit()
        db.refresh(task)
    return task
