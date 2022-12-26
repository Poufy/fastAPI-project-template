from fastapi import FastAPI
from api import blogs, greet

app = FastAPI()

app.include_router(blogs.blogsRouter)
app.include_router(greet.greetRouter)

@app.get('/')
def index():
    return {'message': 'Hello World!'}
