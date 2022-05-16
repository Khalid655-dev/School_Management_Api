from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime
from pydantic.types import conint

from sqlalchemy.sql.sqltypes import Integer


class StudentBase(BaseModel):
    name: str
    roll_no: int
    subject: str
    monthly_fee: int



class StudentCreate(StudentBase):
    pass

    
class AdminOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
       orm_mode = True 


class Student(StudentBase):
    id: int
    created_at: datetime
    admin_id: int
    registered_by_admin: AdminOut

    class Config:
       orm_mode = True 


class StudentOut(Student):
    pass


    class Config:
        orm_mode = True


class AdminSignup(BaseModel):
    email: EmailStr
    password: str


class AdminLogin(BaseModel):
    email: EmailStr
    password: str  


class Token(BaseModel):
    access_token: str
    token_type: str 


class TokenData(BaseModel):
    id: Optional[str] = None


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


class Result(BaseModel):
    id: int
    student_name: str
    student_roll_no: str
    student_subject: str
    student_marks: int
    created_at: datetime
    teacher_id: int
    registered_by_teacher: TeacherOut

    class Config:
       orm_mode = True

class ResultOut(Result):
    pass

    class Config:
        orm_mode = True

class ResultCreate(BaseModel):
    student_name: str
    student_roll_no: int
    student_subject: str
    student_marks: int
    #teacher_id : int