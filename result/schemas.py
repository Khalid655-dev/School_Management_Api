from pydantic import BaseModel
from datetime import datetime
from teacher.schemas import TeacherOut


class ResultSchema(BaseModel):
    id: int
    student_name: str
    student_roll_no: int
    student_subject: str
    student_marks: int
    created_at: datetime
    teacher_id: int
    created_by_teacher: TeacherOut

    class Config:
        orm_mode = True


class ResultOut(ResultSchema):
    pass

    class Config:
        orm_mode = True


class ResultCreate(BaseModel):
    student_name: str
    student_roll_no: int
    student_subject: str
    student_marks: int
    teacher_id: int
