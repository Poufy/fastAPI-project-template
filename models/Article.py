from db.database import Base
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from sqlalchemy import Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

class DbArticle(Base):
    __tablename__ = "Articles"
    id = Column(Integer, primary_key=True, index=True)
    title= Column(String)
    content = Column(String)
    is_published = Column(Boolean)
    user_id = Column(Integer, ForeignKey('Users.id'))
    user = relationship("DbUser", back_populates="items")
    # "items" matches the name of the attribute inside user that retrieves all related Articles to the User
    