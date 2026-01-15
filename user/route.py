import logging
from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from core import session
from core.session import SessionLocal, get_db
from user.schemas import UserRegister
from user.crud import create_user,authenticate_user
from user.auth import create_access_token



router = APIRouter()


@router.post("/register")
def register(data: UserRegister ,db:Session = Depends(get_db)):
    logging.error(data.password)
    return create_user(db = db, user = data)

@router.post("/login")
def login(data:UserRegister,db:Session=Depends(get_db)):
    user = authenticate_user(db = db , user= data)
    if not user:
        raise HTTPException(status_code=401,detail="Invalid credentials")
    token = create_access_token({"sub":user.email})
    return {"access_token":token}