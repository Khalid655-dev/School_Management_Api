from fastapi import APIRouter, status, HTTPException, Depends, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database import get_db
from utils import verify
import oauth2
from auth_token.schemas import Token, TokenData
from models import Admin, Teacher


auth_router = APIRouter(tags=["Authentication"])

 
@auth_router.post('/login', response_model=Token)
def login(admin_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    admin_ = db.query(Admin).filter(Admin.email == admin_credentials.username).first()

    if not admin_:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    if not verify(admin_credentials.password, admin_.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    # create a auth_token
    # return auth_token

    access_token = oauth2.create_access_token(data={"admin_id": admin_.id})

    return {"access_token": access_token, "token_type": "bearer"}


@auth_router.post("/login/teacher", response_model=Token)
def login_teacher(teacher_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    teacher = db.query(Teacher).filter(
        Teacher.email == teacher_credentials.username).first()

    if not teacher:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    if not verify(teacher_credentials.password, teacher.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    # create a auth_token
    # return auth_token

    access_token = oauth2.create_access_token(data={"teacher_id": teacher.id})

    return {"access_token": access_token, "token_type": "bearer"}


 
