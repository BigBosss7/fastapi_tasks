from sqlalchemy.orm import Session
from models.task_model import TaskModel 
from schemas.task_schema import TaskCreate, TaskUpdate
from fastapi import HTTPException

def get_all_tasks(
    db: Session,
    completed: bool | None = None,
    search: str | None = None,
    skip: int = 0,
    limit: int = 10 
):
    query = db.query(TaskModel)

    if completed is not None:
        query = query.filter(
            TaskModel.completed == completed
        )

    if search is not None:
        query = query.filter(
            TaskModel.title.contains(search)
        )

    tasks = (
        query.
        order_by(TaskModel.id.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

    return tasks

def create_task_service(task: TaskCreate, db: Session):
    new_task = TaskModel(
        title=task.title,
        description=task.description
    )
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

def get_task_by_id(task_id: int, db: Session):

    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail= "Tarea no encontrada"
        )

    return task

def update_task_service(
    task_id: int,
    updated_task: TaskCreate,
    db: Session
):

    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail= "Tarea no encontrada"
        )

    task.title = updated_task.title
    task.description = updated_task.description

    db.commit()
    db.refresh(task)

    return task 

def patch_task_service(
    task_id: int,
    task_update: TaskUpdate,
    db: Session
):

    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()

    if not task:
        raise HTTPException(
            satus_code=404,
            detail="Tarea no encontrada"
        )

    if task_update.title is not None:
        task.title = task_update.title

    if task_update.description is not None:
        task.description = task_update.description

    if task_update.completed is not None:
        task.complpeted = task_update.completed

    db.commit()
    db.refresh(task)

    return task 

def delete_task_service(task_id: int, db: Session):

    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )

    db.delete(task)
    db.commit()

    return {"message": "Tarea eliminada correctamente"}