from pydantic import BaseModel
from typing import Optional

class BlogModel(BaseModel):
    title: str
    content: str
    num_comments: int
    published: Optional[bool] = False