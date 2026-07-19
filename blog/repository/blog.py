

from sqlalchemy.orm import Session
from ..import models, schemas
from fastapi import HTTPException, status


def get_all(db: Session):
    blogs=db.query(models.Blog).all() # SQL query to fetch all blogs from the database
    return blogs


def create(request: schemas.Blog, db:Session):
    new_blog=models.Blog(title=request.title, body=request.body, user_id=request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_by_id(id:int, db:Session):
      blog=db.query(models.Blog).filter(models.Blog.ID==id).first()
      if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} was not found')
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {'message': f"Blog with id {id} was not found"} 
      return blog


def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.ID == id)

    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with ID {id} not found"
        )

    blog.delete(synchronize_session=False)
    db.commit()



def update(id:int, request:schemas.Blog, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.ID == id)

    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with ID {id} not found"
        )

    blog.update({'title': request.title, "body": request.body}, synchronize_session=False)
    db.commit()

    return {"message": "Blog updated"}