
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models, database, oauth2
from typing import List
from ..repository import blog


# Define tags here
# Make code clean and organized
router=APIRouter(
    prefix='/Blog',
    tags=['Blogs']
)


get_db = database.get_db
#-----------------------------------

# Get ALL
@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

#-----------------------------------------


# Create Blog
@router.post("/", status_code=status.HTTP_201_CREATED )
def create(request: schemas.Blog, db: Session=Depends(database.get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request,db)

#---------------------------------------

# Get Blog by ID
@router.get("/{id}", response_model=schemas.ShowBlog) # to show title and body only
def id_blog(id:int,response:Response ,db: Session=Depends(database.get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_by_id(id, db)


# Delete Blog
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int , db: Session=Depends(database.get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)
    
# Update Blog
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(database.get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)