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
def test_tc001_validar_fecha_valida(setup_database):
    """
    CASO TC-001: Validar fecha futura válida
    ENTRADA: Fecha de mañana en formato DDMMYYYY
    ESPERADO: Fecha válida sin errores
    """
    mañana = date.today() + timedelta(days=1)
    fecha_str = mañana.strftime("%d%m%Y")
    
    fecha_resultado, error = _validate_date(fecha_str)
    
    assert error is None
    assert fecha_resultado == mañana
    print(f"✅ TC-001: Fecha {fecha_str} validada correctamente")

@pytest.mark.validate  
def test_tc007_error_fecha_invalida(setup_database):
    """
    CASO TC-007: Error con fecha inválida
    ENTRADA: Fecha que no existe (99999999)
    ESPERADO: Error de fecha inválida
    """
    fecha_resultado, error = _validate_date("99999999")
    
    assert fecha_resultado is None
    assert "Fecha inválida" in error
    print(f"✅ TC-007: Error de fecha inválida detectado correctamente")

# TESTS DE CREAR
@pytest.mark.create
def test_tc002_crear_tarea_basica(setup_database):
    """
    CASO TC-002: Crear tarea con título solamente
    ENTRADA: title="Mi tarea de prueba"
    ESPERADO: Tarea creada exitosamente
    """
    tarea, error = create_task("Mi tarea de prueba")
    
    assert error is None
    assert tarea is not None
    assert tarea.title == "Mi tarea de prueba"
    assert tarea.id is not None
    print(f"✅ TC-002: Tarea creada con ID {tarea.id}")

# TESTS DE LEER
@pytest.mark.read
def test_tc003_obtener_tarea_por_id(setup_database):
    """
    CASO TC-003: Obtener tarea existente por ID
    ENTRADA: ID de tarea que existe
    ESPERADO: Tarea encontrada correctamente
    """
    # Crear tarea primero
    tarea_creada, _ = create_task("Tarea para buscar")
    
    # Buscar por ID
    tarea_encontrada = get_task_by_id(tarea_creada.id)
    
    assert tarea_encontrada is not None
    assert tarea_encontrada.title == "Tarea para buscar"
    print(f"✅ TC-003: Tarea encontrada por ID {tarea_creada.id}")

@pytest.mark.read
def test_tc004_obtener_todas_las_tareas(setup_database):
    """
    CASO TC-004: Obtener lista de todas las tareas
    ENTRADA: 2 tareas creadas previamente
    ESPERADO: Lista con 2 tareas
    """
    # Crear tareas
    create_task("Tarea 1")
    create_task("Tarea 2")
    
    # Obtener todas
    tareas = get_all_tasks()
    
    assert len(tareas) == 2
    titulos = [t.title for t in tareas]
    assert "Tarea 1" in titulos
    assert "Tarea 2" in titulos
    print(f"✅ TC-004: {len(tareas)} tareas obtenidas correctamente")

# TESTS DE ACTUALIZAR
@pytest.mark.update
def test_tc005_actualizar_tarea(setup_database):
    """
    CASO TC-005: Actualizar tarea existente
    ENTRADA: Tarea existente con nuevos datos
    ESPERADO: Tarea actualizada correctamente
    """
    # Crear tarea
    tarea_original, _ = create_task("Título original")
    
    # Actualizar
    tarea_actualizada, error = update_task(
        tarea_original.id,
        "Título actualizado", 
        "Nueva descripción"
    )
    
    assert error is None
    assert tarea_actualizada.title == "Título actualizado"
    assert tarea_actualizada.description == "Nueva descripción"
    print(f"✅ TC-005: Tarea ID {tarea_original.id} actualizada")

# TESTS DE ELIMINAR
@pytest.mark.delete
def test_tc006_eliminar_tarea(setup_database):
    """
    CASO TC-006: Eliminar tarea existente
    ENTRADA: ID de tarea que existe
    ESPERADO: Tarea eliminada correctamente
    """
    # Crear tarea
    tarea_creada, _ = create_task("Tarea a eliminar")
    tarea_id = tarea_creada.id
    
    # Eliminar
    tarea_eliminada = delete_task(tarea_id)
    
    # Verificar eliminación
    assert tarea_eliminada is not None
    assert get_task_by_id(tarea_id) is None
    print(f"✅ TC-006: Tarea ID {tarea_id} eliminada correctamente")

# TEST DE INTEGRACIÓN
@pytest.mark.integration
def test_tc008_crud_completo(setup_database):
    """
    CASO TC-008: Flujo CRUD completo
    ENTRADA: Operaciones crear, leer, actualizar, eliminar
    ESPERADO: Todas las operaciones funcionan en secuencia
    """
    # 1. CREAR
    tarea, error = create_task("Tarea CRUD", description="Prueba completa")
    assert error is None
    print(f"  ➤ Crear: Tarea ID {tarea.id} creada")
    
    # 2. LEER
    tarea_leida = get_task_by_id(tarea.id)
    assert tarea_leida.title == "Tarea CRUD"
    print(f"  ➤ Leer: Tarea ID {tarea.id} leída")
    
    # 3. ACTUALIZAR
    tarea_actualizada, error = update_task(
        tarea.id, "Tarea CRUD Actualizada", "Descripción nueva"
    )
    assert error is None
    assert tarea_actualizada.title == "Tarea CRUD Actualizada"
    print(f"  ➤ Actualizar: Tarea ID {tarea.id} actualizada")
    
    # 4. ELIMINAR
    tarea_eliminada = delete_task(tarea.id)
    assert tarea_eliminada is not None
    assert get_task_by_id(tarea.id) is None
    print(f"  ➤ Eliminar: Tarea ID {tarea.id} eliminada")
    
    print(f"✅ TC-008: Flujo CRUD completo exitoso")

# FUNCIONES AUXILIARES PARA REPORTES
def pytest_runtest_setup(item):
    """Ejecuta antes de cada test para mostrar información"""
    print(f"\n🧪 Ejecutando: {item.name}")

def pytest_runtest_teardown(item):
    """Ejecuta después de cada test"""
    print(f"📋 Completado: {item.name}")
