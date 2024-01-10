from pymongo import MongoClient
from datetime import datetime
import os

def load_data_to_mongodb():
    # Replace with your MongoDB connection string
    mongo_url = os.getenv("MONGO_URL")
    client = MongoClient(mongo_url)
    db = client["products"]

    # Adding more sample data
    for i in range(1, 6):
        product_data = {
            "product_name": f"Sample Product {i}",
            "startDate": datetime(2023, 1, 1),
            "endDate": datetime(2023, 12, 31),
            "status": "Active",
            "category": "Electronics",
            "subcategory": "Smartphones",
            "description": f"This is a sample product description for Product {i}.",
            "price": 499.99,
            "discount": 10,
            "image_url": f"https://example.com/sample_product_image_{i}.jpg",
            "quantity": 100,
            "supplier": f"Sample Supplier {i}",
        }

        # Create a products collection and insert a document
        products_collection = db["products"]
        result = products_collection.insert_one(product_data)


