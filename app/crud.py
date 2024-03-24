from sqlalchemy.orm import Session
import datetime

from .models import User
from .schemas import Account

def check_username(db: Session, username: str) -> bool:
    account = db.query(User).filter(User.username == username).first()
    return account

def new_account(db: Session, account: Account):
    try:
        if not check_username(db, account.username):
            user = User(username=account.username, password=account.password)
            db.add(user)
            db.commit()
            db.refresh(user)
            return 1, ''
        else:
            return 2, 'Username already exists.'
    except Exception as e:
        return 0, 'Some error occurred during creating account.'


def check_account(db: Session, account: Account):
    try:
        user = check_username(db, account.username)
        if user is not None:
            if user.failed_time and user.failed_time > datetime.datetime.today():
                return 2, 'Please wait for 1 minute to try again.'
            elif user.password == account.password:
                user.attempt = 0
                user.failed_time = None
                db.commit()
                db.refresh(user)
                return 1, ''
            else:
                user.attempt += 1
                if user.attempt >= 5:
                    user.failed_time = datetime.datetime.today() + datetime.timedelta(minutes=1)
                db.commit()
                db.refresh(user)
                return 0, 'Password is not correct.'
        else:
            return 0, 'Username is not exist.'
    except Exception as e:
        return 0, 'Some error occurred during verifying account.'
