from typing import Literal, Optional

from pydantic import BaseModel, Field


# ========= /projects Endpoint =========
class Project(BaseModel):
    title: str = Field(...)
    description: str = Field(...)
    image: str = Field(...)
    link: str = Field(...)

    class Config:
        allow_population_by_field_name: Literal[True]
        schema_extra = {
            "example": {
                "title": "Navi Web Companion",
                "description": "A Google Chrome extension",
                "image": "public/images/projects/<file_name>",
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
                "image": "public/images/projects/<file_name>",
                "link": "https://www.Github.com/..."
            }
        }
# ========= END /projects Endpoint =========
