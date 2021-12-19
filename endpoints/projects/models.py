from pydantic import BaseModel, Field
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

# ========= /projects Endpoint =========
class Project(BaseModel):
    # id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
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