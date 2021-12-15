import os
from pymongo import MongoClient
from fastapi import FastAPI, Body, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from bson import ObjectId
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List

load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

# instantiation of database object
client = AsyncIOMotorClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
db = client.person

app = FastAPI()

# setup CORS middleware
origins = [
    "http://pochetes.herokuapp.com/personal",
    "http://pochetes.herokuapp.com/experiences",
    "http://pochetes.herokuapp.com/projects",
    "https://pochetes.herokuapp.com/personal",
    "https://pochetes.herokuapp.com/experiences",
    "https://pochetes.herokuapp.com/projects",
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8000/personal",
    "http://localhost:8000/experiences",
    "http://localhost:8000/projects",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

# model for the GET /personal/info endpoint
class PersonalInfoModel(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    description: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = { ObjectId: str }
        # schema (response example) for the GET /personal/info endpoint
        schema_extra = {
            "example": {
                "firstName": "John",
                "lastName": "Doe",
                "email": "johndoe@gmail.com",
                "description": "What a nice guy!"
            }
        }

# model for the PUT /personal/info endpoint
class UpdatePersonalInfoModel(BaseModel):
    firstName: Optional[str]
    lastName: Optional[str]
    email: Optional[EmailStr]
    description: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = { ObjectId: str }
        # schema (response example) for the PUT /personal/info endpoint
        schema_extra = {
            "example": {
                "firstName": "John",
                "lastName": "Doe",
                "email": "johndoe@gmail.com",
                "description": "What a nice guy!"
            }
        }

@app.get('/')
async def hello():
    return {
        "message": "Hello, universe."
    }