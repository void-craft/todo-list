# controllers/task_controller.py
from database.db import SessionLocal
from models.task_model import Task
from datetime import date

def create_task(title: str, fecha: date, description: str = None):
    db = SessionLocal()
    task = Task(title=title, description=description, fecha=fecha)
    db.add(task)
    db.commit()
    db.refresh(task)
    db.close()
    return task

def get_all_tasks():
    db = SessionLocal()
    tasks = db.query(Task).all()
    db.close()
    return tasks

def get_task_by_id(task_id: int):
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    db.close()
    return task

def update_task(task_id: int, title: str, description: str, fecha: date):
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.title = title
        task.description = description
        task.fecha = fecha  
        db.commit()
        db.refresh(task)
    db.close()
    return task
def delete_task(task_id: int):
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    db.close()
    return task