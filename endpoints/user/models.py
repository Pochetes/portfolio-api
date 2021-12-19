from pydantic import BaseModel, EmailStr, Field
from typing import Optional
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

# ========= /user Endpoint =========
class User(BaseModel):
    # id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    firstName: str = Field(...)
    lastName: str = Field(...)
    email: EmailStr = Field(...)
    description: str = Field(...)

class UpdateUser(BaseModel):
    firstName: Optional[str]
    lastName: Optional[str]
    email: Optional[EmailStr]
    description: Optional[str]
# ========= END /user Endpoint =========