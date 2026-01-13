
from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from database import session
from database.session import SessionLocal
from user import schemas,crud,auth



router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(data: schemas.UserRegister ,db:Session = Depends(get_db)):
    return crud.create_user(db = db, user = data)

@router.post("/login")
def login(data:schemas.UserRegister,db:Session=Depends(get_db)):
    user = crud.authenticate_user(db = db , user= data)
    if not user:
        raise HTTPException(status_code=401,detail="Invalid credentials")
    token = auth.create_access_token({"sub":user.email})
    return {"access_token":token}