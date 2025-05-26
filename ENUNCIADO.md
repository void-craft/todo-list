
# 🧩 Proyecto: To-Do List por consola con arquitectura MVC

---

## 🎯 Objetivo

Desarrollar una aplicación por consola que permita gestionar tareas (crear, listar, actualizar, eliminar) utilizando **Python**, **PostgreSQL**, **SQLAlchemy** y **arquitectura MVC**, sin usar frameworks.

Este ejercicio servirá como base para entender cómo se estructura un backend y facilitar la posterior transición a frameworks como Django.

---

## 🧠 Aprendizajes clave

- En este ejercicio tendrás que poner en práctica lo aprendido y hacer un proceso de investigación por parejas. Pero tendras pistas en los enunciados así como en el README.md
- Uso de entornos virtuales y organización profesional de un proyecto
- Conexión a una base de datos PostgreSQL desde Python
- ORM con SQLAlchemy para definir modelos y operar con la base de datos
- Uso de Alembic para gestionar migraciones
- Implementación del patrón arquitectónico MVC
- Uso de consola como interfaz de usuario (`input()` / `print()`)

---

## 📋 Requisitos funcionales

1. El usuario debe poder:
   - ✅ Crear una tarea con título y descripción
   - ✅ Ver todas las tareas existentes
   - ✅ Consultar una tarea por ID
   - ✅ Actualizar una tarea existente (título, descripción o estado)
   - ✅ Eliminar una tarea

2. Las tareas deben persistirse en una base de datos PostgreSQL (`todo_db`).

---

## 🔧 Restricciones técnicas

- ❌ No se debe usar ningún framework web (como Flask o Django)
- ✅ La lógica debe estar separada en:
  - `models/`: clases que representan la base de datos
  - `controllers/`: lógica del negocio
  - `views/`: menú por consola
  - `database/`: configuración y conexión
- ✅ Usar `pg8000` como driver de PostgreSQL
- ✅ Usar Alembic para crear y aplicar migraciones -> Más limpio.

---

## 🗂️ Entrega esperada

Estructura del proyecto:

```
todo_list/
├── models/              # Modelos SQLAlchemy
├── controllers/         # Funciones CRUD
├── database/            # Conexión a la base de datos
├── views/               # Menú de interacción por consola
├── alembic/             # Migraciones de base de datos
├── requirements.txt     # Dependencias
├── README.md            # Documentación técnica
├── ENUNCIADO.md         # (Este archivo)
```

---

## 🧪 Criterios de evaluación

- ✅ Separación clara y coherente en capas (MVC)
- ✅ Funcionamiento completo del CRUD
- ✅ Uso adecuado de SQLAlchemy y Alembic
- ✅ Código limpio, legible y probado
- ✅ Interacción clara a través del menú en consola

---

## ✨ Bonus (opcional)

- Validación de entradas del usuario
- Decorar el menú con estilo
- Colores o mensajes amigables
- El Bonus del Bonus que Nico quiera implementar... 😉

---

¡Mucho ánimo y a disfrutar de aprender a aprender código! 🐍💡


# 📝 Proyecto TODO List - Python Vanilla + PostgreSQL

Este proyecto es un ejemplo funcional de una aplicación de consola que permite gestionar tareas (CRUD) utilizando **Python**, **arquitectura MVC**, **SQLAlchemy** y **PostgreSQL**, sin frameworks.

---

## 📦 Requisitos previos

- Python 3.10 o superior
- PostgreSQL instalado
- Acceso a `psql` desde consola
- Git (opcional)

---

## ⚙️ Configuración inicial

### 1. Clona el repositorio (si es necesario)

```bash
git clone <url-del-repo>
cd todo_list
```

### 2. Crea y activa entorno virtual

```bash
python -m venv venv
.venv/Scripts/Activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

---

## 🛠️ Base de datos

### 1. Crea la base de datos en PostgreSQL

Usa este comando (fuera del entorno virtual):

```bash
psql -U postgres -c "CREATE DATABASE todo_db;"
```

> Asegúrate de tener acceso a `psql` y que tu contraseña sea `1234`.  
> Puedes modificarla en `database/db.py`.

---

## 🔗 Conexión a PostgreSQL

Edita `database/db.py` y asegúrate de que esta línea esté así:

```python
DATABASE_URL = "postgresql+pg8000://postgres:1234@localhost/todo_db"
```

> Usamos el driver `pg8000` en lugar de `psycopg2`.

---

## 🔄 Migraciones

### 1. Inicializa Alembic (si no está hecho)

```bash
alembic init alembic
```

### 2. Configura Alembic

- En `alembic.ini` revisa:

  ```ini
  sqlalchemy.url = postgresql+pg8000://postgres:1234@localhost/todo_db
  ```

- En `alembic/env.py`, importa el modelo y apunta a los metadatos:

  ```python
  from database.db import Base
  from models.task_model import Task
  target_metadata = Base.metadata
  ```

### 3. Crea y aplica la migración

```bash
alembic revision --autogenerate -m "crear tabla tasks"
alembic upgrade head
```

---

## 🚀 Ejecutar la aplicación

Lanza el menú desde la raíz del proyecto:

```bash
python views/task_view.py
```

Y verás:

```
--- MENÚ TO-DO LIST ---
1. Crear tarea
2. Ver todas las tareas
3. Ver tarea por ID
4. Actualizar tarea
5. Eliminar tarea
6. Salir
```

---

## 🧠 Estructura del proyecto

```
todo_list/
│
├── alembic/              # Archivos de migración
├── controllers/          # Lógica de negocio (CRUD)
├── database/             # Conexión a la DB
├── models/               # Definición de modelos SQLAlchemy
├── views/                # Interfaz por consola
│
├── alembic.ini
├── requirements.txt
├── README.md
```

---

## 🧹 Notas finales

- No necesitas frontend, puedes ver la salida por consola.
- El objetivo es entender cómo se estructura un proyecto con MVC y SQLAlchemy.

¡Disfruta programando! 🐍✨
