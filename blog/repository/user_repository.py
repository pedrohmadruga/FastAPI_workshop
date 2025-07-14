from .. import schemas, models
from ..hashing import Hash
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

def create(request: schemas.User, db: Session):
    hashed_password = Hash.bcrypt(request.password)

    user_data = request.model_dump()
    user_data['password'] = hashed_password

    new_user = models.User(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User with the id {id} not found")
    return user