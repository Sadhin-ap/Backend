from sqlalchemy import Column, Integer, String
from backend.database.base import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer,primary_key=True,)
    email = Column(String,unique=True)
    password = Column(String)
