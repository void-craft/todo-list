# controllers/task_controller.py
from database.db import SessionLocal
from models.task_model import Task

def create_task(title: str, fecha, description: str = None):
    db = SessionLocal()
    existing_task = db.query(Task).filter(Task.title == title).first()
    if existing_task:
        db.close()
        return {"error": "Ya existe una tarea con este título."}
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

def update_task(task_id: int, title: str, description: str = None):
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.title = title
        task.description = description
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