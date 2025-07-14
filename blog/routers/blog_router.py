from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog_repository
router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)
get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db)):
    return blog_repository.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog, db: Session = Depends(get_db)):
    return blog_repository.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db:Session = Depends(get_db)):
    return blog_repository.destroy(id, database)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request:schemas.Blog, db:Session = Depends(get_db), tags=['blogs']):
    return blog_repository.update(id, request, db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db)):
    return blog_repository.show(id, db)