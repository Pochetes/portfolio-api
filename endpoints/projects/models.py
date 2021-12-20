from pydantic import BaseModel, Field
from typing import Optional

# ========= /projects Endpoint =========
class Project(BaseModel):
    title: str = Field(...)
    description: str = Field(...)
    image: str = Field(...)
    link: str = Field(...)

    class Config:
        allow_population_by_field_name: True
        schema_extra = {
            "example": {
                "title": "Navi Web Companion",
                "description": "A Google Chrome extension",
                "image": "<link_to_image>",
                "link": "https://www.Github.com/..."
            }
        }

class UpdateProject(BaseModel):
    title: Optional[str]
    description: Optional[str]
    image: Optional[str]
    link: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "Navi Web Companion",
                "description": "A Google Chrome extension",
                "image": "<link_to_image>",
                "link": "https://www.Github.com/..."
            }
        }
# ========= END /projects Endpoint =========