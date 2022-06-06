from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import utils
import oauth2
from database import get_db
import admin
from teacher import TeacherSignup, TeacherOut
from models import Admin, Teacher

admin_router = APIRouter(prefix="/admins", tags=["Admins"])


@admin_router.post("/", status_code=status.HTTP_201_CREATED, response_model=admin.AdminOut)
def create_admin(admin_: admin.AdminSignup, db: Session = Depends(get_db)):
    hashed_password = utils.hash_(admin_.password)
    admin_.password = hashed_password

    new_admin = Admin(**admin_.dict())
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin


@admin_router.get("/{id_}", response_model=admin.AdminOut)
def get_admin(id_: int, db: Session = Depends(get_db)):
    admin_ = db.query(Admin).filter(Admin.id == id_).first()

    if not admin_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"admin with id: {id_} does not exist")

    return admin_


@admin_router.post("/teacher", status_code=status.HTTP_201_CREATED, response_model=TeacherOut)
def create_teacher(teacher: TeacherSignup, db: Session = Depends(get_db),
                   current_admin: int = Depends(oauth2.get_current_admin)):
    hashed_password = utils.hash_(teacher.password)
    teacher.password = hashed_password

    new_teacher = Teacher(admin_id=current_admin.id, **teacher.dict())
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher
