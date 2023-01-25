from sqlalchemy.orm.session import Session
from schemas import userSchema
from models.Users import DbUser
from util.hash import Hash


def create_user(db: Session, request: userSchema):
    new_user = DbUser(username=request.username,
                      email=request.email, password=Hash.bycrypt(request.password))
    db.add(new_user)
    db.commit()
    # refresh will get the id to the new user
    db.refresh(new_user)
    return new_user
