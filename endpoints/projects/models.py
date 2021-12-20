from pydantic import BaseModel, Field
from typing import Optional

# ========= /projects Endpoint =========
class Project(BaseModel):
    title: str = Field(...)
    description: str = Field(...)
    image: str = Field(...)
    link: str = Field(...)

class UpdateProject(BaseModel):
    title: Optional[str]
    description: Optional[str]
    image: Optional[str]
    link: Optional[str]
# ========= END /projects Endpoint =========