from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from bson import ObjectId

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

class Contact(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(...)
    link: str = Field(...)

class Interest(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    topic: str = Field(...)
    image: str = Field(...)

class Skill(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    skill: str = Field(...)
    image: str = Field(...)

class Project(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(...)
    description: str = Field(...)
    image: str = Field(...)
    link: str = Field(...)

class Experience(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    company: str = Field(...)
    position: str = Field(...)
    dateStarted: str = Field(...)
    dateEnded: str = Field(...)
    image: str = Field(...)

class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    firstName: str = Field(...)
    lastName: str = Field(...)
    email: EmailStr = Field(...)
    description: str = Field(...)
    contacts: List[Contact] = []

# model for the PUT /personal/info endpoint
class UpdateUser(BaseModel):
    firstName: Optional[str]
    lastName: Optional[str]
    email: Optional[EmailStr]
    description: Optional[str]
    contacts: Optional[List[Contact]]