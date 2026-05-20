# FastAPI Tasks API 🚀

Mi primer backend real construido con FastAPI y SQLite.

## 📌 Características

- Crear tareas
- Listar tareas
- Obtener tarea por ID
- Actualizar tareas
- Eliminar tareas
- Persistencia con SQLite
- ORM con SQLAlchemy
- Validación con Pydantic

---

# 🛠 Tecnologías

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Uvicorn

---

# 📂 Estructura del proyecto

```txt
fastapi_tasks/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── tasks.db
├── README.md
└── venv/
```

---

# ⚙️ Instalación

## 1. Clonar repositorio

```bash
git clone https://github.com/TUUSUARIO/fastapi_tasks.git
```

---

## 2. Entrar al proyecto

```bash
cd fastapi_tasks
```

---

## 3. Crear entorno virtual

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Instalar dependencias

```bash
pip install fastapi uvicorn sqlalchemy
```

---

## 5. Ejecutar servidor

```bash
uvicorn main:app --reload
```

---

# 📡 Endpoints

| Método | Endpoint | Descripción |
|---|---|---|
| GET | /tasks | Obtener todas las tareas |
| GET | /tasks/{id} | Obtener tarea por ID |
| POST | /tasks | Crear tarea |
| PUT | /tasks/{id} | Actualizar tarea |
| DELETE | /tasks/{id} | Eliminar tarea |

---

# 📘 Swagger Docs

Disponible en:

```txt
http://127.0.0.1:8000/docs
```

---

# 🧠 Lo aprendido

Este proyecto me ayudó a entender:

- APIs REST
- CRUD
- SQLAlchemy ORM
- SQLite
- Persistencia de datos
- Arquitectura backend básica
- Manejo de endpoints
- Validación con Pydantic

---

# 🚀 Próximas mejoras

- PATCH endpoints
- Query parameters
- PostgreSQL
- Docker
- Autenticación JWT
- Deploy en Render/Railway

---

# 👨‍💻 Autor

Saul Barrera
