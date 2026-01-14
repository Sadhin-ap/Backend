 

from pydantic import BaseModel


class UserRegister(BaseModel):
    email : str
    password : str

class AdminCreate(UserRegister):
    pass

class UserLogin(UserRegister):
     pass

class UserResponse(BaseModel):
    id : int 
    email : str

    class Config:
        from_attribures = True