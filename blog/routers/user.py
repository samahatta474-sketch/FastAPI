
from blog.repository import user
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, oauth2
from blog import hashing, schemas


router=APIRouter(
    prefix='/User',
    tags=['Users']
)


# Create User
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session=Depends(database.get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.create(request,db)


# show user
@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int, db: Session=Depends(database.get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.get_by_id(id,db)