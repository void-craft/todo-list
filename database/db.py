# database/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+pg8000://postgres:1234@localhost/todo_db"

# Crear el motor
engine = create_engine(DATABASE_URL)

# Base de clase para modelos
Base = declarative_base()

# Session factory (lo que importar como SessionLocal)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)