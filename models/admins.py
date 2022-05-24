from sqlalchemy import Column
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import Integer, String, TIMESTAMP

from database import Base


class Admin(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(200), nullable=False, unique=True)
    password = Column(String(400), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)