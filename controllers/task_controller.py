# controllers/task_controller.py
from database.db import SessionLocal
from models.task_model import Task
from datetime import date, datetime


def create_task(title: str, date_input: str = None, description: str = None):
    """ Crea Una Tarea """
    db = SessionLocal()
    task_date = date.today()

    if date_input:
        # Si hay fecha, parse(analisa) y valida la fecha
        try:
            task_date = datetime.strptime(date_input, "%d/%m/%Y").date()
            if task_date < date.today():
                db.close()
                return None, "La fecha no puede ser anterior a hoy."
        except ValueError:
            db.close()
            return None, "Fecha inválida. Asegúrate de que la fecha existe."
    
    # Si no fecha, deja SQLAlchemy usa le fecha del hoy

    task = Task(title=title, description=description, date=task_date)
    db.add(task)
    db.commit()
    db.refresh(task)
    db.close()
    return task, None


def get_all_tasks():
    """ Mostra Todas las Tareas """
    db = SessionLocal()
    tasks = db.query(Task).all()
    db.close()
    return tasks


def get_task_by_id(task_id: int):
    """ Trea Tarea por ID """
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    db.close()
    return task


def update_task(task_id: int, title: str, description: str, date_input: str = None):
    """ Actualize tarea """
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        db.close()
        return None, "Tarea no encontrada."

    task.title = title
    task.description = description

    if date_input:
        try:
            task_date = datetime.strptime(date_input, "%d/%m/%Y").date()
            if task_date < date.today():
                db.close()
                return None, "La fecha no puede ser anterior a hoy."
            task.date = task_date
        except ValueError:
            db.close()
            return None, "Fecha inválida."
    # Si no fecha, deja lo que existe

    db.commit()
    db.refresh(task)
    db.close()
    return task, None


def delete_task(task_id: int):
    """ Borra una Tarea por ID """
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    db.close()
    return task
