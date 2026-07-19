
from blog import hashing
from sqlalchemy.orm import Session
from ..import models, schemas
from fastapi import HTTPException, status

def get_by_id(id: int, db: Session):
    user = db.query(models.User).filter(models.User.ID == id).first()
    if not user:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with ID {id} not found')     
    return user


def create(request:schemas.User, db:Session):
    new_user=models.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    print(new_user.password) # the results on the terminal
    return new_user # returning NULL may cause problems in FastAPI server