from fastapi import APIRouter, Depends, HTTPException, status
from .. import database, schemas, models
from sqlalchemy.orm import Session
from ..hashing import Hash

router = APIRouter()
get_db = database.get_db

@router.post('/user', response_model=schemas.ShowUser, tags=['users'])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    hashed_password = Hash.bcrypt(request.password)

    user_data = request.model_dump()
    user_data['password'] = hashed_password

    new_user = models.User(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/user/{id}', response_model=schemas.ShowUser, tags=['users'])
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User with the id {id} not found")
    return user