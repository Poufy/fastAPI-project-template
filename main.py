from fastapi import FastAPI
from api import blogs, greet

app = FastAPI()

app.include_router(blogs.router)
app.include_router(greet.router)

@app.get('/')
def index():
    return {'message': 'Hello World!'}
