# database/db.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("DATABASE_URL")

# Crear el motor
engine = create_engine(DATABASE_URL)

# Base de clase para modelos
Base = declarative_base()

# Session factory (lo que importar como SessionLocal)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
