from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app import models, utils, oauth2
from sqlalchemy.orm import Session
from app.db import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post('/login')
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")

    if utils.verify_password(user_credentials.password, user.pwd):
        oauth2_token = oauth2.create_access_token(data={"user_id": user.id})
        return {"token": oauth2_token, "token_type": "bearer"}

    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
