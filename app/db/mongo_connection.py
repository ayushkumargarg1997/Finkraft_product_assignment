from pymongo import MongoClient
import os

mongo_connection_string = os.getenv("MONGO_URL")

def get_mongo_connection():
    client = MongoClient(mongo_connection_string)
    return client
