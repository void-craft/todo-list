from sqlalchemy import Column, Integer, String, Date, func
from database.db import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, unique=True)
    description = Column(String)
    date = Column(Date, server_default=func.date("now"))

    def __repr__(self):
        return f"<Task id={self.id} title={self.title!r}>"
