
from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


# sqlalchemy == model
class Blog(Base):
    __tablename__ = "blogs"

    ID: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String, index=True)
    body: str = Column(String)
    user_id: int=Column(Integer, ForeignKey('Users.ID'))

    creator=relationship('User', back_populates='blogs') # relationship

class User(Base):
    __tablename__='Users'
    ID: int = Column(Integer, primary_key=True, index=True)
    name: str=Column(String)
    email: str=Column(String)
    password: str=Column(String)

    blogs=relationship('Blog', back_populates='creator') #relationship

