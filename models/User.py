from db.database import Base
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy import Column
from sqlalchemy.orm import relationship

class DbUser(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    items = relationship("DbArticle", back_populates="user")
    
    