# from sqlalchemy.orm import declarative_base

# DATABASE_URL = "postgresql+pg8000://postgres:1234@localhost/todo_db"

# from sqlalchemy.orm import declarative_base
# Base = declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+pg8000://postgres:1234@localhost/todo_db"

# Create the engine
engine = create_engine(DATABASE_URL, echo=True)

# Base class for models
Base = declarative_base()

# Session factory (this is what you import as SessionLocal)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)