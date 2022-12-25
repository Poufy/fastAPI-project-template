from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()


@app.get('/')
def index():
    return {'message': 'Hello World!'}

# Order of the routes matter. The first route that matches the request will be executed. so if you have a route that matches any path, it should be the last route in the file.
@app.get('/greet/anyone')
def greet():
    return {'message': 'Hello everyone!'}


@app.get('/greet/{name}')
def greet(name: str):
    return {'message': f'Hello {name}! How are you doing today?'}

# Predefined path parameters
class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@app.get('/blogs/types/{type}')
def get_blog_Type(type: BlogType):
    return {'message': f'Blog type is {type}'}

# Query parameters. All the query parameters are optional.
# The function parameter name should match the query parameter name.
@app.get('/blog/all')
def get_all_blogs(page=1, page_size=20):
    return {'message': f'Page: {page}, Page Size: {page_size}'}

# Optional query parameters
@app.get('/blog/optional')
def get_blogs_optional(page=1, page_size: Optional[int] = None):
    return {'message': f'Page: {page}, Page Size: {page_size}'}

# Query and path parameters together
@app.get('/blog/{id}/comments/{comment_id}')
def get_blog_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {'message': f'Blog id: {id}, Comment id: {comment_id}, Valid: {valid}, Username: {username}'}