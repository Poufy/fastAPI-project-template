from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from schemas.articleSchema import ArticleBase
from models.Article import DbArticle

def create_article(db: Session, request: ArticleBase):
    new_article = DbArticle(title=request.title,
                      content=request.content, is_published=request.is_published, user_id=request.creator_id)
    db.add(new_article)
    db.commit()
    # refresh will get the id to the new article
    db.refresh(new_article)
    return new_article

def get_article(db: Session, id: int):
    article = db.query(DbArticle).filter(DbArticle.id == id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found')
    return article