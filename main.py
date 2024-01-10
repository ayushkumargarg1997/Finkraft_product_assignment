# main.py

from fastapi import FastAPI
# from app.auth.auth import router as auth_router
from app.product.product import router as product_router
from app.user.user import user_router
# from app.db.database import DatabaseManager
from dotenv import load_dotenv

load_dotenv()
from app.data.product_data import load_data_to_mongodb

load_dotenv()
load_data_to_mongodb() ## loading sample product data

app = FastAPI()

# app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(product_router, prefix="/product", tags=["product"])
app.include_router(user_router, prefix="/user", tags=["user"])

