from typing import List
from pydantic import BaseModel

# Article inside UserResponse    
class Article(BaseModel):
    title: str
    content: str
    is_published: bool
    class Config():
        orm_mode = True
        
# Data that we want to receive from the user
class UserBase(BaseModel):
    username: str
    email: str
    password: str

# Data that we want to send back to the user
# When orm_mode is set to True, it tells Pydantic to treat the model as an SQLAlchemy ORM model and allows to use the class with the ORM.
# This means that the model will use the fields and column types of the SQLAlchemy model,
# instead of the fields defined in the Pydantic model.
class UserResponse(BaseModel):
    username: str
    email: str
    id: int
    items: List[Article] = []
    class Config():
        orm_mode = True
