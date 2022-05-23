from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.schema import ForeignKey, PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import TIMESTAMP, Boolean, Integer, String
from database import Base


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False, unique=True)
    password = Column(String(400), nullable=False)
    specialization = Column(String(400), nullable=True)
    joining_date = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=True)



