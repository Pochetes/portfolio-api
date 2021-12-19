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

# ========= /experience Endpoint =========
class Experience(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    company: str = Field(...)
    position: str = Field(...)
    dateStarted: str = Field(...)
    dateEnded: str = Field(...)
    image: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "company": "Meta Platforms Inc.",
                "position": "Software Engineer Intern",
                "dateStarted": "June 2021",
                "dateEnded": "August 2021",
                "image": "<link_to_image>"
            }
        }

class UpdateExperience(BaseModel):
    company: Optional[str]
    position: Optional[str]
    dateStarted: Optional[str]
    dateEnded: Optional[str]
    image: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "company": "Meta Platforms Inc.",
                "position": "Software Engineer Intern",
                "dateStarted": "June 2021",
                "dateEnded": "August 2021",
                "image": "<link_to_image>"
            }
        }
# ========= END /experience Endpoint =========