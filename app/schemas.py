from pydantic import BaseModel, validator
import re

TOO_SHORT = 0
TOO_LONG = 1
INVALID = 2

class Account(BaseModel):
    username: str
    password: str
    @validator('username')
    def username_check(cls, v):
        if len(v) < 3:
            return TOO_SHORT
        elif len(v) > 32:
            return TOO_LONG
        return v
    @validator('password')
    def password_check(cls, v):
        if len(v) < 8:
            return TOO_SHORT
        elif len(v) > 32:
            return TOO_LONG
        elif not bool(re.match(r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d).+', v)):
            return INVALID
        return v
    
    class Config:
        orm_mode = True