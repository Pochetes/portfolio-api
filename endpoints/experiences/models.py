from pydantic import BaseModel, Field
from typing import Optional

# ========= /experience Endpoint =========
class Experience(BaseModel):
    company: str = Field(...)
    position: str = Field(...)
    dateStarted: str = Field(...)
    dateEnded: str = Field(...)
    image: str = Field(...)

    class Config:
        allow_population_by_field_name = True
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