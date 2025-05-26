# tests/test_tasks.py
# Todos los tests esenciales para el sistema de tareas

import pytest
from datetime import date, timedelta
from controllers.task_controller import (
    create_task, update_task, get_all_tasks, 
    get_task_by_id, delete_task, _validate_date
)

# TESTS DE VALIDACIÓN
@pytest.mark.validate
def test_tc001_validate_valid_date(setup_database):
    mañana = date.today() + timedelta(days=1)
    date_str = mañana.strftime("%d%m%Y")
    
    validated_date, error = _validate_date(date_str)
    
    assert error is None
    assert validated_date == mañana
    print(f"✅ TC-001: Fecha {date_str} validada correctamente")

@pytest.mark.validate  
def test_tc007_error_invalid_date(setup_database):
    fecha_str = "99999999"
    validated_date, error = _validate_date(fecha_str)
    
    assert validated_date is None
    assert "Fecha inválida" in error
    print(f"✅ TC-007: Error de fecha inválida detectado correctamente")

# TESTS DE CREAR
@pytest.mark.create
def test_tc002_create_basic_task(setup_database):
    task, error = create_task("Mi tarea de prueba")
    
    assert error is None
    assert task is not None
    assert task.title == "Mi tarea de prueba"
    assert task.id is not None
    print(f"✅ TC-002: Tarea creada con ID {task.id}")

# TESTS DE LEER
@pytest.mark.read
def test_tc003_get_task_by_id(setup_database):
    created_task, _ = create_task("Tarea para buscar")
    found_task = get_task_by_id(created_task.id)
    
    assert found_task is not None
    assert found_task.title == "Tarea para buscar"
    print(f"✅ TC-003: Tarea encontrada por ID {created_task.id}")

@pytest.mark.read
def test_tc004_get_all_tasks(setup_database):
    create_task("Tarea 1")
    create_task("Tarea 2")
    
    tasks = get_all_tasks()
    
    assert len(tasks) == 2
    titles = [t.title for t in tasks]
    assert "Tarea 1" in titles
    assert "Tarea 2" in titles
    print(f"✅ TC-004: {len(tasks)} tareas obtenidas correctamente")

# TESTS DE ACTUALIZAR
@pytest.mark.update
def test_tc005_update_task(setup_database):
    original_task, _ = create_task("Título original")
    
    updated_task, error = update_task(
        original_task.id,
        "Título actualizado", 
        "Nueva descripción"
    )
    
    assert error is None
    assert updated_task.title == "Título actualizado"
    assert updated_task.description == "Nueva descripción"
    print(f"✅ TC-005: Tarea ID {original_task.id} actualizada")

# TESTS DE ELIMINAR
@pytest.mark.delete
def test_tc006_delete_task(setup_database):
    created_task, _ = create_task("Tarea a eliminar")
    task_id = created_task.id
    
    deleted_task = delete_task(task_id)
    
    assert deleted_task is not None
    assert get_task_by_id(task_id) is None
    print(f"✅ TC-006: Tarea ID {task_id} eliminada correctamente")

# TEST DE INTEGRACIÓN
@pytest.mark.integration
def test_tc008_full_crud_flow(setup_database):
    task, error = create_task("Tarea CRUD", description="Prueba completa")
    assert error is None
    print(f"  ➤ Crear: Tarea ID {task.id} creada")
    
    read_task = get_task_by_id(task.id)
    assert read_task.title == "Tarea CRUD"
    print(f"  ➤ Leer: Tarea ID {task.id} leída")
    
    updated_task, error = update_task(
        task.id, "Tarea CRUD Actualizada", "Descripción nueva"
    )
    assert error is None
    assert updated_task.title == "Tarea CRUD Actualizada"
    print(f"  ➤ Actualizar: Tarea ID {task.id} actualizada")
    
    deleted_task = delete_task(task.id)
    assert deleted_task is not None
    assert get_task_by_id(task.id) is None
    print(f"  ➤ Eliminar: Tarea ID {task.id} eliminada")
    
    print(f"✅ TC-008: Flujo CRUD completo exitoso")


