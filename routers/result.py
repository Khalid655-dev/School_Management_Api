from fastapi import APIRouter, Depends, HTTPException, Response, status
from typing import List, Optional
from sqlalchemy.orm import Session

from models import Result
from database import get_db
from result import ResultSchema, ResultCreate, ResultOut

result_router = APIRouter(prefix="/results", tags=["Teachers"])


@result_router.get("/", response_model=List[ResultOut])
def get_results(db: Session = Depends(get_db), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    results = db.query(Result).filter(Result.student_subject.contains(search)).limit(limit).offset(skip).all()
    return results


@result_router.post("/", status_code=status.HTTP_201_CREATED, response_model=ResultSchema)
def create_results(result: ResultCreate, db: Session = Depends(get_db)):

    new_result = Result(**result.dict())
    db.add(new_result)
    db.commit()
    db.refresh(new_result)
    return new_result


@result_router.get("/{id_}", response_model=ResultOut)
def get_result(id_: int, db: Session = Depends(get_db)):

    result = db.query(Result).filter(Result.id == id_).first()
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"result with id: {id_} was not found")

    return result


@result_router.delete("/{id_}", status_code=status.HTTP_204_NO_CONTENT)
def delete_result(id_: int, db: Session = Depends(get_db)):

    result_query = db.query(Result).filter(Result.id == id_)
    result = result_query.first()

    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The result with id: {id_} is not found")

    result_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@result_router.put("/{id_}", response_model=ResultSchema)
def update_result(id_: int, updated_result: ResultCreate, db: Session = Depends(get_db)):

    result_query = db.query(Result).filter(Result.id == id_)
    result = result_query.first()

    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"result with id: {id_} does not exist")

    result_query.update(updated_result.dict(), synchronize_session=False)

    db.commit()

    return result_query.first()
