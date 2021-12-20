from pydantic import BaseModel, Field
from typing import Optional

# ========= /interests Endpoint =========
class Interest(BaseModel):
    topic: str = Field(...)
    image: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "topic": "Blockchain",
                "image": "<link_to_image>"
            }
        }

class UpdateInterest(BaseModel):
    topic: Optional[str]
    image: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "topic": "Blockchain",
                "image": "<link_to_image>"
            }
        }
# ========= END /interests Endpoint =========