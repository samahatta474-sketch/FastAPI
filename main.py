
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app=FastAPI()

# Decorate
@app.get("/")
def index():
    return {'MSG':'HELLO!!'}


# Route
@app.get('/about')
def about():
    return {'data': {"MSG":"This is about page =)"}}

# ------------------------------- QUERY PARAMS -------------------------------

# blog?limit=10&published=true

# ampersand & is used to separate query parameters.

@app.get('/blog')
def blog_list(limit: int=10 , published: bool=True , sort: Optional[str]=None):
    if published==True:
        return {'data': f'Blog list with limit of {limit}'}
    else:
        return {'Blogs not found'}
    
# path parameter is defined in the path, otherwise it's query parameter.

# ------------------------------- body request -------------------------------

# To declare the request body --> USE pydantic model. OR function parameters
@app.post('/blog')
def new_blog(name:str, id:int, price:float):
    return {'new blog created': f"{name} with ID {id} and price {price}."}

# OR

class Blog(BaseModel):
    name: str
    id: int
    price: float
    published: Optional[bool]

@app.post('/blog2')
def new_blog(request: Blog):
    return {f'new blog created with {request.title}'}

# ------------------------ How to Debug ----------------------------------
# - Define the breakpoint
# - The app will stop at the breakpoint and will fetch all info till that breakpoint
# - Ctrl + shift + p ==> debugging + choose the framework --> fastAPI
 # 1:05:30

# ----------------------------- pydantic schemas -----------------------------------------


