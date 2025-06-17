from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    pwd = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
