from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"],deprecated = "auto")

def hash_password(passwor:str):
    return pwd_context.hash(passwor)

def verify_password(plain:str,hashed: str)-> bool:
    return pwd_context.verify(plain,hashed)