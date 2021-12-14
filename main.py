import os
import asyncio
from fastapi import FastAPI
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

# database connection status handling
async def get_server_info():

    load_dotenv()
    MONGODB_URI = os.environ["MONGODB_URI"]

    # instantiation of database object
    client = AsyncIOMotorClient(MONGODB_URI, serverSelectionTimeoutMS=5000)

    try:
        print("Connected to server successfully.")
    except Exception:
        print("Unable to connect to the server.")

loop = asyncio.get_event_loop()
loop.run_until_complete(get_server_info())

app = FastAPI()

# helps convert id data type into string for FastAPI
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

@app.get('/')
async def hello():
    return {
        "message": "Hello, universe."
    }