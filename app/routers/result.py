from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import func

from app import oauth
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/results", tags=["Teachers"])


@router.get("/", response_model=List[schemas.ResultOut])
def get_results(db: Session = Depends(get_db), current_teacher: int = Depends(oauth.get_current_teacher), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    results = db.query(models.Result).filter(models.Result.student_subject.contains(search)).limit(limit).offset(skip).all()
    return results


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Result)
def create_results(result: schemas.ResultCreate, db: Session = Depends(get_db), current_teacher: int = Depends(oauth.get_current_teacher)):
    ## coursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
    ## new_post = coursor.fetchone()
    ## conn.commit()

    new_result = models.Result(teacher_id=current_teacher.id, **result.dict())
    db.add(new_result)
    db.commit()
    db.refresh(new_result)
    return new_result


@router.get("/{id}", response_model=schemas.ResultOut)
def get_result(id: int, db: Session = Depends(get_db), current_teacher: int = Depends(oauth.get_current_teacher)):
    ## coursor.execute("""SELECT * from posts where id = %s """, (str(id)))
    ##post = coursor.fetchone()
    # post = db.query(models.Post).filter(models.Post.id == id).first()

    result = db.query(models.Result).filter(models.Result.id == id).first()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"result with id: {id} was not found")

    return result


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_result(id: int, db: Session = Depends(get_db), current_teacher: int = Depends(oauth.get_current_teacher)):
    ##coursor.execute("""Delete from posts where id = %s returning *""", (str(id)))
    ## deleted_post = coursor.fetchone()
    ## conn.commit()
    result_query = db.query(models.Result).filter(models.Result.id == id)
    result = result_query.first()

    if result_query.first == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The result with id: {id} is not found")

    if result.teacher_id != current_teacher.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not Authorized to perform the requested action")

    result_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.Result)
def update_result(id: int, updated_student: schemas.ResultCreate, db: Session = Depends(get_db), current_teacher: int = Depends(oauth.get_current_teacher)):
    ##coursor.execute("""update posts SET title = %s, content = %s, published = %s where id = %s RETURNING *""", (post.title, post.content, post.published, str(id)))
    ##updated_post = coursor.fetchone()
    ##conn.commit()
    result_query = db.query(models.Result).filter(models.Result.id == id)
    result = result_query.first()

    if result == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"reslut with id: {id} does not exist")

    if result.teacher_id != current_teacher.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not Authorized to perform the requested action")

    result_query.update(updated_student.dict(), synchronize_session=False)

    db.commit()

    return result_query.first()