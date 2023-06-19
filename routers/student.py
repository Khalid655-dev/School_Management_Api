from fastapi import APIRouter, Depends, HTTPException, Response, status
from typing import List, Optional
from sqlalchemy.orm import Session

from student import StudentOut, StudentCreate
import oauth2
from database import get_db
from models.students import Student


std_router = APIRouter(prefix="/students", tags=["Students"])


@std_router.get("/", response_model=List[StudentOut])
def get_students(db: Session = Depends(get_db),
                 current_admin: int = Depends(oauth2.get_current_admin)
                 , limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    students = db.query(Student).filter(Student.subject.contains(search)).limit(limit).offset(skip).all()
    return students


@std_router.post("/", status_code=status.HTTP_201_CREATED, response_model=StudentOut)
def create_students(student_: StudentCreate, db: Session = Depends(get_db)
                    , current_admin: int = Depends(oauth2.get_current_admin)):
    new_student = Student(admin_id=current_admin.id, **student_.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


@std_router.get("/{id_}", response_model=StudentOut)
def get_student(id_: int, db: Session = Depends(get_db), current_admin: int = Depends(oauth2.get_current_admin)):
    student_ = db.query(Student).filter(Student.id == id_).first()
    if not student_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"student with id: {id_} was not found")

    return student_


@std_router.delete("/{id_}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(id_: int, db: Session = Depends(get_db), current_admin: int = Depends(oauth2.get_current_admin)):
    student_query = db.query(Student).filter(Student.id == id_)
    student = student_query.first()

    if student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The student with id: {id_} is not found")

    if student.admin_id != current_admin.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not Authorized to perform the requested action")

    student_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@std_router.put("/{id_}", response_model=StudentOut)
def update_student(id_: int, updated_student: StudentCreate, db: Session = Depends(get_db),
                   current_admin: int = Depends(oauth2.get_current_admin)):
    student_query = db.query(Student).filter(Student.id == id_)
    student = student_query.first()

    if student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"student with id: {id_} does not exist")

    #if student.admin_id != current_admin.id:
        #raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                           # detail="Not Authorized to perform the requested action")

    student_query.update(updated_student.dict(), synchronize_session=False)

    db.commit()

    return student_query.first()
