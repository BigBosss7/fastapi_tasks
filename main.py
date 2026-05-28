from fastapi import FastAPI

from fastapi.responses import JSONResponse
from exceptions.task_exceptions import TaskNotFoundException
from database import engine
from models.task_model import TaskModel 
from routers.task_router import router as task_router

app = FastAPI()

@app.exception_handler(TaskNotFoundException) #"si aparece TaskNotFoundException:devuelve este JSON"
def task_not_found_handler(request, exc):

    return JSONResponse(
        status_code=404,
        content={
            "error": exc.message
        }
    )

TaskModel.metadata.create_all(bind=engine)

app.include_router(task_router)
