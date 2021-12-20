from pydantic import BaseModel, Field
from typing import Optional

# ========= /skills Endpoint =========
class Skill(BaseModel):
    technology: str = Field(...)
    image: str = Field(...)

    class Config:
        allow_population_by_field_name: True
        schema_extra = {
            "example": {
                "technology": "Python",
                "image": "<link_to_image>"
            }
        }
class UpdateSkill(BaseModel):
    technology: Optional[str]
    image: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "technology": "Python",
                "image": "<link_to_image>"
            }
        }
# ========= END /skills Endpoint =========