from fastapi import FastAPI
from user.route import router as user_router
from core.base import Base
from core.session import engine


app = FastAPI(title="E-commerce API")

Base.metadata.create_all(bind = engine)
app.include_router(user_router, prefix= "/users")
# app.include_router(product_router,prefix="/products")