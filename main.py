import os
import asyncio
from fastapi import FastAPI
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

async def get_server_info():

    load_dotenv()
    MONGODB_URI = os.environ["MONGODB_URI"]

    client = AsyncIOMotorClient(MONGODB_URI, serverSelectionTimeoutMS=5000)

    try:
        print("Connected to server successfully.")
    except Exception:
        print("Unable to connect to the server.")

loop = asyncio.get_event_loop()
loop.run_until_complete(get_server_info())

app = FastAPI()

@app.get('/')
async def hello():
    return {
        "message": "Hello, universe."
    }