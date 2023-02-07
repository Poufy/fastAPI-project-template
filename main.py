from fastapi import FastAPI
from router import blogs, greet, user, article
from models import User
from db.database import engine

app = FastAPI()

app.include_router(user.router)
app.include_router(blogs.router)
app.include_router(greet.router)
app.include_router(article.router)

@app.get('/')
def index():
    return {'message': 'Hello World!'}

User.Base.metadata.create_all(engine)