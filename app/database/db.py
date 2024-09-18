from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

def connect():
    url = os.environ['MONGODB_CONNECTION_URI']
    
    
    client = MongoClient(url)

    if client:
        return client
    else:
        print("Failed to return the mongo client")


