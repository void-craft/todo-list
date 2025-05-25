# tests/conftest.py
# Configuración básica para todos los tests

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.db import Base

# Base de datos de prueba en memoria
TEST_DATABASE_URL = "sqlite:///:memory:"
test_engine = create_engine(TEST_DATABASE_URL)
TestSessionLocal = sessionmaker(bind=test_engine, autoflush=False, autocommit=False)

@pytest.fixture(scope="function")
def setup_database():
    """
    CONFIGURACIÓN: Base de datos limpia para cada test
    - Crea tablas nuevas
    - Al terminar, las borra
    """
    # Crear tablas
    Base.metadata.create_all(bind=test_engine)
    
    # Cambiar la sesión temporalmente
    import controllers.task_controller
    original_session = controllers.task_controller.SessionLocal
    controllers.task_controller.SessionLocal = TestSessionLocal
    
    yield  # Ejecuta el test
    
    # Restaurar y limpiar
    controllers.task_controller.SessionLocal = original_session
    Base.metadata.drop_all(bind=test_engine)

@pytest.fixture
def test_case_info(request):
    """
    FIXTURE: Información del caso de prueba
    Agrega ID y descripción a cada test
    """
    return {
        'test_id': getattr(request.node, 'test_id', 'TC-000'),
        'description': getattr(request.node, 'description', 'Sin descripción'),
        'test_name': request.node.name
    }