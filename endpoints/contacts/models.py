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

# ========= /user/contacts Endpoint =========
class Contact(BaseModel):
    title: str = Field(...)
    link: str = Field(...)

class UpdateContact(BaseModel):
    title: Optional[str]
    link: Optional[str]
# ========= END /user/contacts Endpoint =========