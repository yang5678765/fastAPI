from sqlalchemy import Column, Integer, String, DateTime

from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    attempt = Column(Integer, default=0)
    failed_time = Column(DateTime)