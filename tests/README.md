# INSTRUCCIONES RÁPIDAS:
"""
⚡ COMANDOS ESENCIALES:

1. Instalar: pip install -r requirements-test.txt

2. Ejecutar todos: pytest tests/ -v

3. Ejecutar por marcador:
   - pytest -m create tests/    # Solo tests de crear
   - pytest -m read tests/      # Solo tests de leer
   - pytest -m validate tests/  # Solo tests de validación

4. Ver cobertura: pytest tests/ --cov=controllers

5. Ejecutar test específico:
   pytest tests/test_tasks.py::test_tc002_crear_tarea_basica -v

6. Parar en primer error: pytest tests/ -x
"""