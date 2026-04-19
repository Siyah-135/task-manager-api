from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.models.task_model import Task
from app.schemas.task_schema import TaskCreate

router = APIRouter()


# Create Task
@router.post("/tasks")
def create_task(task: TaskCreate):
    db: Session = SessionLocal()
    try:
        new_task = Task(
            title=task.title,
            description=task.description,
            due_date=task.due_date,
            status=task.status
        )
        
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        
        return {"message": "Task created", "task": new_task}
    finally:
        db.close()


# Get All Tasks
@router.get("/tasks")
def get_tasks():
    db: Session = SessionLocal()
    try:
        tasks = db.query(Task).all()
        return {"tasks": tasks}
    finally:
        db.close()


# Get Single Task by ID
@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    db: Session = SessionLocal()
    try:
        task = db.query(Task).filter(Task.id == task_id).first()
        
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        
        return {"task": task}
    finally:
        db.close()


# Update Task
@router.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: TaskCreate):
    db: Session = SessionLocal()
    try:
        task = db.query(Task).filter(Task.id == task_id).first()
        
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        
        task.title = updated_task.title
        task.description = updated_task.description
        task.due_date = updated_task.due_date
        task.status = updated_task.status
        
        db.commit()
        
        return {"message": "Task updated", "task": task}
    finally:
        db.close()


# Delete Task
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    db: Session = SessionLocal()
    try:
        task = db.query(Task).filter(Task.id == task_id).first()
        
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        
        db.delete(task)
        db.commit()
        
        return {"message": "Task deleted"}
    finally:
        db.close()