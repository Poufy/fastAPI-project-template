from fastapi import APIRouter, Depends
from schemas.userSchema import UserBase, UserResponse
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_user

router = APIRouter(prefix='/user', tags=['User'])

# Create User
@router.post('/', response_model=UserResponse, status_code=201)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


# Read User


# Update User


# Delete User
