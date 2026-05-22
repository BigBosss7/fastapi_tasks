from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class TaskModel(Base):
    __tablename__ = "tasks" # CREATE TABLE tasks

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True) #TITLE VARCHAR
    description = Column(String)
    completed = Column(Boolean, default=False)