from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.schema import InterestCreate
from backend.repository.interests import create, get_all, get_by_id

router = APIRouter(prefix="/interest", tags=["interests"])

@router.post("/")
def create_interest(interest: InterestCreate, db: Session = Depends(get_db)):
    return create(db, interest)

@router.get("/")
def get_interests(db: Session = Depends(get_db)):
    return get_all(db)

@router.get("/{id}")
def get_interest(id: int, db: Session = Depends(get_db)):
    return get_by_id(db, id)
