# controllers/task_controller.py
from database.db import SessionLocal
from models.task_model import Task
from datetime import date, datetime

def _validate_date(date_str: str):
    """Funcion ayudante - valida y analisa la fecha"""
    if not date_str:
        return None
    
    try:
        if len(date_str) == 8 and date_str.isdigit():  # DDMMYYYY formato
            date_str = f"{date_str[:2]}/{date_str[2:4]}/{date_str[4:]}"
        
        parsed_date = datetime.strptime(date_str, "%d/%m/%Y").date()
        if parsed_date < date.today():
            return None, "La fecha no puede ser anterior a hoy."
        return parsed_date, None
    except ValueError:
        return None, "Fecha inválida. Asegúrate de que la fecha existe."

def create_task(title: str, date_input: str = None, description: str = None):
    """Crea Una Tarea"""
    db = SessionLocal()
    
    if date_input:
        task_date, error = _validate_date(date_input)
        if error:
            db.close()
            return None, error
    else:
        task_date = date.today()

    task = Task(title=title, description=description, date=task_date)
    db.add(task)
    db.commit()
    db.refresh(task)
    db.close()
    return task, None

def update_task(task_id: int, title: str, description: str, date_input: str = None):
    """Actualiza tarea"""
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        db.close()
        return None, "Tarea no encontrada."

    task.title = title
    task.description = description

    if date_input:
        task_date, error = _validate_date(date_input)
        if error:
            db.close()
            return None, error
        task.date = task_date

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

def delete_task(task_id: int):
    """ Borra una Tarea por ID """
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    db.close()
    return task
