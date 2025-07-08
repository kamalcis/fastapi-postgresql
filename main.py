from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Blog(BaseModel):
    title: str
    description: str
    published: Optional[bool]

@app.post('/blog/create')
def createBlog(blog: Blog):
    return blog


@app.get('/')
def index():
    return {'data':{'name':'Sarthak '}}

@app.get('/blog')
def index(id: int):
    return {'data': id}


@app.get('/about')
def about():
    return {'data':'About Page details'}