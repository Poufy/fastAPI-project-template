from fastapi import FastAPI
from router import blogs, greet, user
from models import Users
from db.database import engine

app = FastAPI()

app.include_router(user.router)
app.include_router(blogs.router)
app.include_router(greet.router)

@app.get('/')
def index():
    return {'message': 'Hello World!'}

Users.Base.metadata.create_all(engine)