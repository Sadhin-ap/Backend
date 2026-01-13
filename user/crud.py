from sqlalchemy.orm import Session
from user.model import User
from user.schemas import UserRegister
from utils.hashing import hash_password, verify_password


def create_user(db: Session,user:UserRegister):
    user= User(email = user.email, password = hash_password(user.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db:Session,user:UserRegister):
    user = db.query(User).filter(User.email == user.email).first()
    if not user:
        return None
    if not verify_password(User.password,user.password):
        return None
    return user