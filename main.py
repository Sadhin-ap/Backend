from fastapi import FastAPI
from user.route import router as user_router
from core.base import Base
from core.session import engine
from product.router import router as product_router

app = FastAPI(title="E-commerce API")

Base.metadata.create_all(bind = engine)
app.include_router(user_router, prefix= "/users")
app.include_router(product_router)