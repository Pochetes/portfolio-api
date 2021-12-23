from typing import Optional

from pydantic import BaseModel, Field


# ========= /interests Endpoint =========
class Interest(BaseModel):
    topic: str = Field(...)
    image: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "topic": "Blockchain",
                "image": "public/images/interests/<file_name>"
            }
        }


class UpdateInterest(BaseModel):
    topic: Optional[str]
    image: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "topic": "Blockchain",
                "image": "public/images/interests/<file_name>"
            }
        }
# ========= END /interests Endpoint =========
