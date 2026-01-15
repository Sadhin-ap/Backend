# from sqlalchemy.orm import Session
# from user.model import User
# from user.schemas import UserRegister
# from utils.hashing import hash_password, verify_password


# def create_user( user:UserRegister, db: Session):
#     user_password = user.password
#     users_count = db.query(User).count()
#     role = "admin" if users_count == 0 else "user"
#     user= User(email = user.email, password = hash_password(user_password),role = role)
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return user

# def authenticate_user(db:Session,user:UserRegister):
#     user_db = db.query(User).filter(User.email == user.email).first()
#     if not user:
#         return None
#     if not verify_password(user.password,user_db.password):
#         return None
#     return user

# def create_admin(user:UserRegister,db:Session):
#     admin = User(
#         email = user.email,
#         password = hash_password(user.password),
#         role = "admin"
#     )
#     db.add(admin)
#     db.commit()
#     return admin

from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from user.model import User
from user.schemas import UserRegister
from utils.hashing import hash_password, verify_password
from user.auth import create_access_token


def create_user(db: Session, user: UserRegister):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    users_count = db.query(User).count()
    role = "admin" if users_count == 0 else "user"

    new_user = User(
        email=user.email,
        password=hash_password(user.password),
        role=role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def authenticate_user(db: Session, user: UserRegister):
    user_db = db.query(User).filter(User.email == user.email).first()

    if not user_db:
        return None

    if not verify_password(user.password, user_db.password):
        return None

    if not user:
        raise HTTPException(status_code=401,detail="Invalid credentials")
    token = create_access_token({"sub":user.email})
    return {"access_token":token,"token_type":"bearer"}

def create_admin(db: Session, user: UserRegister):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    admin = User(
        email=user.email,
        password=hash_password(user.password),
        role="admin"
    )

    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin
