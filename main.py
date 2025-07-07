from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'Sarthak '}}

@app.get('/blog')
def index(id: int):
    return {'data': id}


@app.get('/about')
def about():
    return {'data':'About Page details'}