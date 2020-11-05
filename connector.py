from pymongo import MongoClient
from config.config import Config


def connect_mongo(): 
    client = MongoClient(Config.MONGO_HOST)
    db = client[Config.MONGO_DB]
    return db