from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from schemas.task_schema import TaskResponse, TaskCreate, TaskUpdate
from services.task_service import (
    get_all_tasks, 
    create_task_service,
    get_task_by_id,
    update_task_service,
    patch_task_service
)


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return get_all_tasks(db)

@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int, 
    db: Session = Depends(get_db)
    ):
    return get_task_by_id(task_id, db)

@router.post("/tasks", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):
    return create_task_service(task, db)

@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    updated_task: TaskCreate,
    db: Session = Depends(get_db)
):
    return update_task_service(task_id, updated_task, db)
    
@router.patch("/tasks/{task_id}", response_model=TaskResponse)
def patch_task(
    task_id: int,
    task_update: TaskUpdate,
    db: Session = Depends(get_db)
    ):

    return patch_task_service(task_id, task_update, db)