import builtins
from datetime import timezone
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.functions import now
from sqlalchemy.sql.schema import ForeignKey, PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import TIMESTAMP, Boolean, Integer, String
from .database import Base
from datetime import datetime

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(400), nullable=False)
    roll_no = Column(Integer, nullable=False)
    subject = Column(String(200), nullable=False)
    monthly_fee = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)
    admin_id = Column(Integer, ForeignKey("admins.id", ondelete="CASCADE"), nullable=False)

    registered_by_admin = relationship("Admin")
    

class Admin(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(200), nullable=False, unique=True)
    password = Column(String(400), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(200), nullable=False, unique=True)
    email = Column(String(200), nullable=False, unique=True)
    password = Column(String(400), nullable=False)
    specialization = Column(String(400), nullable=True)
    joining_date = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=True)

class Result(Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True, nullable=False)
    student_name = Column(String(400), nullable=False)
    student_roll_no = Column(Integer, nullable=False)
    student_subject = Column(String(200), nullable=False)
    student_marks = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id", ondelete="CASCADE"), nullable=False)

    registered_by_teacher = relationship("Teacher")



