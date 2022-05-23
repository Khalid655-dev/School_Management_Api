from pydantic import BaseModel, EmailStr
from datetime import datetime


class TeacherSignup(BaseModel):
    name: str
    email: EmailStr
    password: str


class TeacherLogin(BaseModel):
    email: EmailStr
    password: str


class TeacherOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True
