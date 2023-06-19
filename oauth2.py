from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from sqlalchemy.orm import Session

import database
from config import settings
from auth_token import TokenData
from models.admins import Admin
from models.teachers import Teacher


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login",
    scheme_name="Admin_oauth2_scheme"
)
teacher_oauth2_schema = OAuth2PasswordBearer(
    tokenUrl="login/teacher",
    scheme_name="Teacher_oauth2_schema"
)


# SECRET_KEY
# Algorithm
# Expiration Time

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    try:

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id_: str = payload.get("admin_id")
        if id_ is None:
            raise credentials_exception
        token_data = TokenData(id=id_)
    except JWTError:
        raise credentials_exception

    return token_data


def verify_access_teacher_token(token: str, credentials_exception):
    try:

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id_: str = payload.get("teacher_id")
        if id_ is None:
            raise credentials_exception
        token_data = TokenData(id=id_)
    except JWTError:
        raise credentials_exception

    return token_data


def get_current_admin(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

    token = verify_access_token(token, credentials_exception)

    admin = db.query(Admin).filter(Admin.id == token.id).first()
    return admin


def get_current_teacher(token: str = Depends(teacher_oauth2_schema), db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

    token = verify_access_teacher_token(token, credentials_exception)

    teacher = db.query(Teacher).filter(Teacher.id == token.id).first()
    return teacher


