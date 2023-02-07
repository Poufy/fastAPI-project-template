from typing import List
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

# Read all Users
@router.get('/all', response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db_user.get_users(db)

# Read User
@router.get('/{id}', response_model=UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    return db_user.get_user(db, id)

# Update User
@router.post('/{id}/update')
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    return db_user.update_user(db, id, request)

# Delete User
@router.get('/{id}/delete')
def delete_user(id: int, db: Session = Depends(get_db)):
    return db_user.delete_user(db, id);