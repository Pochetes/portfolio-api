from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# ========= /user Endpoint =========
class User(BaseModel):
    firstName: str = Field(...)
    lastName: str = Field(...)
    email: EmailStr = Field(...)
    description: str = Field(...)

    class Config:
        allow_population_by_field_name: True
        schema_extra = {
            "example": {
                "firstName": "John",
                "lastName": "Doe",
                "email": "johndoe@email.com",
                "description": "A very nice guy indeed!"
            }
        }
class UpdateUser(BaseModel):
    firstName: Optional[str]
    lastName: Optional[str]
    email: Optional[EmailStr]
    description: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "firstName": "John",
                "lastName": "Doe",
                "email": "johndoe@email.com",
                "description": "A very nice guy indeed!"
            }
        }
# ========= END /user Endpoint =========