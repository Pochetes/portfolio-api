from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class InfoModel(BaseModel):
    firstName: str = Field(...)
    lastName: str = Field(...)
    email: EmailStr = Field(...)
    description: str = Field(...)

# model for the PUT /personal/info endpoint
class UpdateInfoModel(BaseModel):
    firstName: Optional[str]
    lastName: Optional[str]
    email: Optional[EmailStr]
    description: Optional[str]