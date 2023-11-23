from pymongo import MongoClient
from os import environ

MONGO_URI = environ.get("MONGO_URI")
MONGO_DB = "mongodb://localhost:27017"
DB_NAME = environ.get('DB_NAME')

client = MongoClient(MONGO_URI or MONGO_DB)

db = client[DB_NAME]
