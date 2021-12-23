from typing import Literal, Optional

from pydantic import BaseModel, Field


# ========= /skills Endpoint =========
class Skill(BaseModel):
    technology: str = Field(...)
    image: str = Field(...)

    class Config:
        allow_population_by_field_name: Literal[True]
        schema_extra = {
            "example": {
                "technology": "Python",
                "image": "public/images/skills/<file_name>"
            }
        }


class UpdateSkill(BaseModel):
    technology: Optional[str]
    image: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "technology": "Python",
                "image": "public/images/skills/<file_name>"
            }
        }
# ========= END /skills Endpoint =========
