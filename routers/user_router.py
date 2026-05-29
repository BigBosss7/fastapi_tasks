from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 

from database import SessionLocal 
from schemas.user_schema import (
    UserCreate, 
    UserResponse,
    UserLogin
)
from services.user_service import (
    create_user_service, 
    login_user_service
)


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users", response_model=UserResponse)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user_service(user, db)

@router.post("/login")
def login(
    user_data: UserLogin,
    db: Session = Depends(get_db)    
): 
   return login_user_service(user_data, db)