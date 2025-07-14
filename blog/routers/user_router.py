from fastapi import APIRouter, Depends
from .. import database, schemas
from sqlalchemy.orm import Session
from ..repository import user_repository

router = APIRouter(
    prefix='/user',
    tags=['users']
)
get_db = database.get_db

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user_repository.create(request, db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user_repository.show(id, db)