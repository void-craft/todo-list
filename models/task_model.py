# models/task_model.py
from sqlalchemy import Column, Integer, String, Date
from database.db import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    fecha = Column(Date, nullable=False)
   
    def __repr__(self):
        return f"<Task id={self.id} title={self.title!r}>"
