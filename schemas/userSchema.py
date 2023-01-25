from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    password: str

# When orm_mode is set to True, it tells Pydantic to treat the model as an SQLAlchemy ORM model and allows to use the class with the ORM.
# This means that the model will use the fields and column types of the SQLAlchemy model,
# instead of the fields defined in the Pydantic model.
class UserResponse(BaseModel):
    username: str
    email: str
    class Config():
        orm_mode = True
