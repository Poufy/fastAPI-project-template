from fastapi import APIRouter, Response, status
from enum import Enum
from typing import Optional
from models import blogs

## write an import line that imports the blogs model from the models folder

router = APIRouter(prefix='/blog', tags=['Blog'])

@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog with id: {id} not found'}
    else:
        return {'message': f'Blog id is {id}'}

# Predefined path parameters
class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@router.get('/types/{type}')
def get_blog_Type(type: BlogType):
    return {'message': f'Blog type is {type}'}

# Query parameters. All the query parameters are optional.
# The function parameter name should match the query parameter name.
@router.get('/all/')
def get_all_blogs(page=1, page_size=20):
    return {'message': f'Page: {page}, Page Size: {page_size}'}

# Optional query parameters
@router.get('/optional/')
def get_blogs_optional(page=1, page_size: Optional[int] = None):
    return {'message': f'Page: {page}, Page Size: {page_size}'}

# Query and path parameters together
@router.get('/{id}/comments/{comment_id}', tags=['Comments'])
def get_blog_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {'message': f'Blog id: {id}, Comment id: {comment_id}, Valid: {valid}, Username: {username}'}

# Post operations
# Notice we have automatic type validation and automatic conversion of the request body from JSON to a python object that we declared in the models folder.
@router.post('/new', status_code=status.HTTP_201_CREATED)
def create_blog(blog: blogs.BlogModel):
    return {'data': blog}