from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from schemas.userSchema import UserBase
from models.User import DbUser
from util.hash import Hash

def create_user(db: Session, request: UserBase):
    new_user = DbUser(username=request.username,
                      email=request.email, password=Hash.bycrypt(request.password))
    db.add(new_user)
    db.commit()
    # refresh will get the id to the new user
    db.refresh(new_user)
    return new_user

def get_users(db: Session):
    users = db.query(DbUser).all()
    return users

def get_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first();
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found')
    return user

def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found')
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bycrypt(request.password)
    })
    db.commit()
    return 'updated successfully'

def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found')
    db.delete(user)
    db.commit()
    return 'deleted successfully'