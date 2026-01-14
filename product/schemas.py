from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name:str
    description:Optional[str] = None
    price : float
    stock: int

class ProductUpdate(BaseModel):
    name : Optional[str]
    description : Optional[str]
    price : Optional[str]
    stock : Optional[str]

class ProductResponse(BaseModel):
    id : int 
    name : str 
    descripton : Optional[str]
    price : float
    stock : int

    class Config:
        from_atribute = True
     

    
        


