from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.schema import InternshipCreate
from backend.repository.internships import create, get_all, get_by_id

router = APIRouter(prefix="/internship", tags=["internships"])

@router.post("/")
def create_internship(internship: InternshipCreate, db: Session = Depends(get_db)):
    return create(db, internship)

@router.get("/")
def get_internships(db: Session = Depends(get_db)):
    return get_all(db)

@router.get("/{id}")
def get_internship(id: int, db: Session = Depends(get_db)):
    return get_by_id(db, id)
