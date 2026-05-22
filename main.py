from fastapi import FastAPI

from database import engine
from models.task_model import TaskModel 
from routers.task_router import router as task_router

app = FastAPI()

TaskModel.metadata.create_all(bind=engine)

app.include_router(task_router)
