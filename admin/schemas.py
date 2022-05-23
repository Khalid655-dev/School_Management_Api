from pydantic import BaseModel, EmailStr
from datetime import datetime


class AdminSignup(BaseModel):
    email: EmailStr
    password: str


class AdminLogin(AdminSignup):
    pass


class AdminOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True









