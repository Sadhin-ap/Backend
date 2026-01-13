from sqlalchemy import Column, Identity, Integer, String
from database.base import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer,Identity(start=1, increment=1), primary_key=True,)
    email = Column(String,unique=True)
    password = Column(String)

