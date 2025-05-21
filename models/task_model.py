from sqlalchemy import Column, Integer, String
from database.db import Base
class Task(Base):
    __tablename__ = "tasks" 

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)

    def __repr__(self):
        return f"<Task id={self.id} title={self.title!r} description={self.description}>"