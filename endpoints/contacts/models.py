from pydantic import BaseModel, Field
from typing import Optional


# ========= /user/contacts Endpoint =========
class Contact(BaseModel):
    title: str = Field(...)
    image: str = Field(...)
    link: str = Field(...)

    class Config:
        allow_population_by_field_name: True
        schema_extra = {
            "example": {
                "title": "Github",
                "image": "public/images/contacts/<file_name>",
                "link": "https://www.github.com/Pochetes"
            }
        }


class UpdateContact(BaseModel):
    title: Optional[str]
    image: Optional[str]
    link: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "Github",
                "image": "public/images/contacts/<file_name>",
                "link": "https://www.github.com/Pochetes"
            }
        }
# ========= END /user/contacts Endpoint =========
