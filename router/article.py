from typing import List
from fastapi import APIRouter, Depends
from schemas.articleSchema import ArticleBase, ArticleResponse
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_article

router = APIRouter(prefix='/article', tags=['Article'])

# Create Article
@router.post('/', response_model=ArticleResponse, status_code=201)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(db, request)

# Read Article
# Without the ressponse_model, the response will be as it is in the database. By adding the response_model with orm_mode=True, the response will be as it is in the schema.
# The schema fields will be mapped to the database fields and populated in the response. Check the User field in ArticleResponse.
@router.get('/{id}', response_model=ArticleResponse)
def get_article(id: int, db: Session = Depends(get_db)):
    return db_article.get_article(db, id)
