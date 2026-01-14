from sqlalchemy.orm import Session
from user.model import User
from user.schemas import UserRegister
from utils.hashing import hash_password, verify_password


def create_user( user:UserRegister, db: Session):
    user_password = user.password
    users_count = db.query(User).count()
    role = "admin" if users_count == 0 else "user"
    user= User(email = user.email, password = hash_password(user_password),role = role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db:Session,user:UserRegister):
    user_db = db.query(User).filter(User.email == user.email).first()
    if not user:
        return None
    if not verify_password(user.password,user_db.password):
        return None
    return user

def create_admin(user:UserRegister,db:Session):
    admin = User(
        email = user.email,
        password = hash_password(user.password),
        role = "admin"
    )
    db.add(admin)
    db.commit()
    return admin