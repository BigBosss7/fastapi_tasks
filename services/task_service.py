from sqlalchemy.orm import Session
from models.task_model import TaskModel 
from schemas.task_schema import TaskCreate
from fastapi import HTTPException

def get_all_tasks(db: Session):
    return db.query(TaskModel).all()


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