from fastapi import Depends, FastAPI, status, Response, HTTPException
from sqlalchemy.orm import Session

from .crud import new_account, check_account
from .database import SessionLocal, engine
from .schemas import Account
from .models import User
from . import models

TOO_SHORT = 0
TOO_LONG = 1
INVALID = 2

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/create_account')
def create_account(account: Account, response: Response, db: Session = Depends(get_db)):
    result = {'success':False, 'reason':''}
    try:
        if account.username is TOO_SHORT:
            result['reason'] = 'Username is too short.'
            response.status_code = status.HTTP_400_BAD_REQUEST
        elif account.password is TOO_LONG:
            result['reason'] = 'Username is too long.'
            response.status_code = status.HTTP_400_BAD_REQUEST
        elif account.password is TOO_SHORT:
            result['reason'] = 'Password is too short.'
            response.status_code = status.HTTP_400_BAD_REQUEST
        elif account.password is TOO_LONG:
            result['reason'] = 'Passord is too long.'
            response.status_code = status.HTTP_400_BAD_REQUEST
        elif account.password is INVALID:
            result['reason'] = 'Passord should contain at least 1 uppercase letter, 1 lowercase letter, and 1 number.'
            response.status_code = status.HTTP_400_BAD_REQUEST
        else:
            state, result['reason'] = new_account(db, account)
            if state==1:
                response.status_code = status.HTTP_201_CREATED
            elif state==2:
                response.status_code = status.HTTP_400_BAD_REQUEST
            else:
                response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    except Exception as e:
        result['reason'] = 'Some error occurred during creating account.'
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    finally:
        return result



@app.post('/verify_account')
def verify_account(account:Account, response: Response, db: Session = Depends(get_db)):
    result = {'success':False, 'reason':''}
    state, result['reason'] = check_account(db, account)
    if state==1:
        result['success'] = True
        response.status_code = status.HTTP_202_ACCEPTED
    elif state==2:
        result['success'] = False
        response.status_code = status.HTTP_429_TOO_MANY_REQUESTS
    else:
        result['success'] = False
        response.status_code = status.HTTP_400_BAD_REQUEST
    return result
