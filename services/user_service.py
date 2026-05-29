from sqlalchemy.orm import Session

from models.user_model import UserModel 
from schemas.user_schema import UserCreate
from core.security import hash_password
from core.security import verify_password
from fastapi import HTTPException 

def create_user_service(user: UserCreate, db: Session):
    new_user = UserModel(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user 

def login_user_service(
    user_data,
    db: Session
):

  user = (
    db.query(UserModel)
    .filter(UserModel.email == user_data.email)
    .first()
  )

  if not user:
    raise HTTPException(
        status_code=401,
        detail="Credenciales inválidas"
    )

  valid_password = verify_password(
    user_data.password,
    user.hashed_password
  )

  if not valid_password:
    raise HTTPException(
        status_code=401,
        detail="Credenciales inválidas"
    )

  return {
        "message": "Login correcto"
    }