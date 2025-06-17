from fastapi import APIRouter, Depends
from typing import List
from app import models, schemas, utils
from sqlalchemy.orm import Session
from app.db import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/", response_model=List[schemas.UserBase])
async def root(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.post("/create-user", response_model=schemas.UserResponse)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = user.dict()
    new_user["pwd"] = utils.hash_password(new_user["pwd"])
    db_user = models.User(**new_user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
