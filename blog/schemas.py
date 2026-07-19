from pydantic import BaseModel, ConfigDict
from typing import List, Optional

# pydantic model == schema


class Blog(BaseModel):
    title: str
    body: str
    user_id: int
    class Config():
        orm_mode=True

# Response schema -- what user gets back
class ShowUser(BaseModel):
    name:str
    email:str
    blogs: List[Blog]=[]
    class Config():
        orm_mode=True

class ShowBlog(BaseModel):
    title:str
    body: str
    user_id: int
    creator: ShowUser
    class Config():
        orm_mode=True

# User schema -- what user sends
class User(BaseModel):
    name:str
    email:str
    password:str

class Login(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None

