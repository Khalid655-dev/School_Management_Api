from .admins import Admin
from .results import Result
from .students import Student
from .teachers import Teacher
from database import Base


__all__ = (
    "Admin", "Result", "Student", "Teacher", "Base"
)
