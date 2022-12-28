from pydantic import BaseModel
from typing import Optional, List, Dict

# Subtype 
from models import images
    
class BlogModel(BaseModel):
    title: str
    content: str
    num_comments: int
    published: Optional[bool] = False
    tags: List[str] = []
    metadata: Dict[str, str] = {'key1': 'value1'}
    image: Optional[images.Image] = None