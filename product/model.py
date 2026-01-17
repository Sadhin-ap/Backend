
from sqlalchemy import Column, Identity,Integer,String,Float,DateTime
from datetime import datetime
from core.base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer,Identity(start=100, increment=1),primary_key=True)
    name = Column(String,nullable=False)
    description = Column(String)
    price = Column(Float,nullable=False)
    stock = Column(Integer,default=0)
    
