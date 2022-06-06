from pydantic import BaseModel
from datetime import datetime


class StudentBase(BaseModel):
    name: str
    roll_no: int
    subject: str
    monthly_fee: int


class StudentCreate(StudentBase):
    pass


class StudentSchema(StudentBase):
    id: int
    created_at: datetime
    admin_id: int

    class Config:
        orm_mode = True


class StudentOut(StudentSchema):
    pass

    class Config:
        orm_mode = True
