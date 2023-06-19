from sqlalchemy import Column
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import DateTime, Integer, String, TIMESTAMP
from sqlalchemy.sql.schema import ForeignKey

from database import Base


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False, unique=True)
    password = Column(String(400), nullable=False)
    specialization = Column(String(400), nullable=True)
    joining_date = Column(DateTime, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=True)
    admin_id = Column(Integer, ForeignKey("admins.id", ondelete="CASCADE"), nullable=False)



