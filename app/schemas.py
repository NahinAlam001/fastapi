from pydantic import BaseModel
from datetime import datetime
from pydantic.networks import EmailStr

class UserBase(BaseModel):
    id: int
    email:EmailStr
    pwd:str
    created_at:datetime

class UserCreate(BaseModel):
    email: EmailStr
    pwd: str

class UserUpdate(BaseModel):
    pwd: str

class UserResponse(BaseModel):
    id: int
    email:EmailStr
    created_at:datetime

class TokenData(BaseModel):
    id: str
