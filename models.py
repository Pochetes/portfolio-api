from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from bson import ObjectId

# Converting ObjectId (BSON) into str for JSON
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

# ========= /user/contacts Endpoint =========
class Contact(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(...)
    link: str = Field(...)

class UpdateContact(BaseModel):
    title: Optional[str]
    link: Optional[str]
# ========= END /user/contacts Endpoint =========

# ========= /interests Endpoint =========
class Interest(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    topic: str = Field(...)
    image: str = Field(...)

class UpdateInterest(BaseModel):
    topic: Optional[str]
    image: Optional[str]
# ========= END /interests Endpoint =========

# ========= /skills Endpoint =========
class Skill(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    skill: str = Field(...)
    image: str = Field(...)

class UpdateSkill(BaseModel):
    skill: Optional[str]
    image: Optional[str]
# ========= END /skills Endpoint =========

# ========= /projects Endpoint =========
class Project(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(...)
    description: str = Field(...)
    image: str = Field(...)
    link: str = Field(...)

class UpdateProject(BaseModel):
    title: Optional[str]
    description: Optional[str]
    image: Optional[str]
    link: Optional[str]
# ========= END /projects Endpoint =========

# ========= /experience Endpoint =========
class Experience(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    company: str = Field(...)
    position: str = Field(...)
    dateStarted: str = Field(...)
    dateEnded: str = Field(...)
    image: str = Field(...)

class UpdateExperience(BaseModel):
    company: Optional[str]
    position: Optional[str]
    dateStarted: Optional[str]
    dateEnded: Optional[str]
    image: Optional[str]
# ========= END /experience Endpoint =========

# ========= /user Endpoint =========
class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    firstName: str = Field(...)
    lastName: str = Field(...)
    email: EmailStr = Field(...)
    description: str = Field(...)
    contacts: List[Contact] = []

class UpdateUser(BaseModel):
    firstName: Optional[str]
    lastName: Optional[str]
    email: Optional[EmailStr]
    description: Optional[str]
    contacts: Optional[List[Contact]]
# ========= END /user Endpoint =========