from typing import List
from pydantic import BaseModel
    
# User inside ArticleResponse
class User(BaseModel):
    id: int
    username: str
    email: str
    class Config():
        orm_mode = True   
        
# Data that we want to receive from the user when creating an article
class ArticleBase(BaseModel):
    title: str
    content: str
    is_published: bool
    creator_id: int

# Article inside UserResponse
# Data that we want to send back to the user when reading an article
class ArticleResponse(BaseModel):
    title: str
    content: str
    is_published: bool
    user: User
    class Config():
        orm_mode = True