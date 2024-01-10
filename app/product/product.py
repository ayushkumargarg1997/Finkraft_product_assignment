from fastapi import APIRouter, Depends, HTTPException
from app.db.mongo_connection import get_mongo_connection
import logging
from pymongo.collection import Collection
from typing import Optional, List
from pydantic import BaseModel
from app.db.models.product import Product
from app.auth.auth_api import auth_wrapper

router = APIRouter()

# Set up logging
logging.basicConfig(level=logging.DEBUG, filename="app.log")
logger = logging.getLogger(__name__)

@router.get("/listproducts", response_model=List[Product])
async def list_products(db: Collection = Depends(get_mongo_connection), auth: bool = Depends(auth_wrapper)):
    try:
        if not auth:
            raise HTTPException(status_code=401, detail="Authentication required")

        database_name = "products"
        collection_name = "products"
        database = db.get_database(database_name)
        products_collection = database.get_collection(collection_name)

        # Retrieve products from the "products" collection
        products_cursor = products_collection.find()
        products = list(products_cursor)

        logger.info(f"Retrieved {len(products)} products from MongoDB")
        return products
    except HTTPException as http_error:
        logger.error(f"HTTP Exception: {http_error.detail}")
        raise
    except Exception as e:
        logger.error(f"Error fetching products from MongoDB: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post("/add-product", response_model=dict)
async def add_product(new_product: Product, db: Collection = Depends(get_mongo_connection), auth: bool = Depends(auth_wrapper)):
    try:
        if not auth:
            raise HTTPException(status_code=401, detail="Authentication required")

        database_name = "products"
        collection_name = "products"
        database = db.get_database(database_name)
        products_collection = database.get_collection(collection_name)

        # Add products
        product_data = new_product.dict()
        result = products_collection.insert_one(product_data)

        logger.info(f"Added product to MongoDB with ID: {result.inserted_id}")
        return {"message": "Product added successfully", "inserted_id": str(result.inserted_id)}
    except HTTPException as http_error:
        logger.error(f"HTTP Exception: {http_error.detail}")
        raise
    except Exception as e:
        logger.error(f"Error adding product to MongoDB: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post("/remove-product", response_model=dict)
async def remove_product(product_name: str, db: Collection = Depends(get_mongo_connection), auth: bool = Depends(auth_wrapper)):
    try:
        if not auth:
            raise HTTPException(status_code=401, detail="Authentication required")

        database_name = "products"
        collection_name = "products"
        database = db.get_database(database_name)
        products_collection = database.get_collection(collection_name)

        # Remove products
        result = products_collection.delete_one({"product_name": product_name})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Product not found")

        logger.info(f"Removed product from MongoDB with name: {product_name}")
        return {"message": "Product removed successfully", "deleted_count": result.deleted_count}
    except HTTPException as http_error:
        logger.error(f"HTTP Exception: {http_error.detail}")
        raise
    except Exception as e:
        logger.error(f"Error removing product from MongoDB: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
