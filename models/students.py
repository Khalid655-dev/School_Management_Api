from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.schema import ForeignKey, PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import TIMESTAMP, Boolean, Integer, String
from database import Base


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(400), nullable=False)
    roll_no = Column(Integer, nullable=False)
    subject = Column(String(200), nullable=False)
    monthly_fee = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)

