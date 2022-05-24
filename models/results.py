from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, TIMESTAMP

from database import Base


class Result(Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True, nullable=False)
    student_name = Column(String(400), nullable=False)
    student_roll_no = Column(Integer, nullable=False)
    student_subject = Column(String(200), nullable=False)
    student_marks = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id", ondelete="CASCADE"), nullable=False)

    created_by_teacher = relationship("Teacher")
