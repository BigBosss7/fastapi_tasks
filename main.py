from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel 
from database import engine
from models import TaskModel 
from sqlalchemy.orm import Session 
from fastapi import Depends

from database import SessionLocal, engine 
from models import TaskModel 
import models 
import schemas 

models.Base.metadata.create_all(bind=engine)

TaskModel.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal() #creamos una sesión con db, abre conexion con SQLite
    try:
        yield db #le entrega la conexion al endpoint, el endpoint hace lo que tenga que hacer con la conexion y luego se cierra
    finally:
        db.close()


app = FastAPI()

# "Base de datos" temporal 
#tasks = []

# Modelo de datos
class Task(BaseModel):
    title: str
    description: str 



@app.get("/")
def home():
    return {"message": "Task API funcionando"}


@app.post("/tasks", response_model=schemas.TaskResponse)
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db) #FastAPI, dame una conexión DB automáticamente.
):
    new_task = TaskModel(  # crea objeto ORM, No SQL directo 
        title=task.title,
        description=task.description
    )

    db.add(new_task) #prepara INSERT SQL
    db.commit() #GUARDA realmente en SQLite.
    db.refresh(new_task) #actualiza el objeto ORM con el ID generado por SQLite, id generado, valores reales


    return new_task

@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):

    tasks = db.query(TaskModel).all() #Haz una consulta sobre la tabla tasks, y trae todos los registros
                                      #SELECT * FROM tasks
    return tasks 

@app.get("/tasks/completed")
def get_completed_tasks():

    completed_tasks = []

    for task in tasks:
        if task["completed"]:
            completed_tasks.append(task)

    return completed_tasks

@app.get("/tasks/{task_id}", response_model=schemas.TaskResponse)
def get_task(task_id: int,
             db: Session = Depends(get_db)
):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first() #SELECT * FROM tasks WHERE id = task_id LIMIT 1
    
    if not task:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )

    return task  

@app.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_task(
    task_id: int,
    updated_task: schemas.TaskCreate,
    db: Session = Depends(get_db)
):

    task = db.query(TaskModel).filter(TaskModel.id == task_id).first() #SELECT * FROM tasks WHERE id = task_id LIMIT 1
     
    if not task:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"

        )

    task.title = updated_task.title #UPDATE tasks SET title = updated_task.title, description = updated_task.description WHERE id = task_id
    task.description = updated_task.description

    db.commit()
    db.refresh(task)

    return task 

    
@app.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
   
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
   
    if not task:
       raise HTTPException(
             status_code=404,
             detail="No se encontró la tarea"
        )

    db.delete(task)
    db.commit()
  
    return {"message": "Tarea eliminada exitosamente"}



@app.patch("/tasks/{task_id}/done")
def complete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return task
  
    raise HTTPException(status_code=404, detail="Tarea no encontrada")  



