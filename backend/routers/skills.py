from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.schema import SkillCreate
from backend.repository.skills import create, get_all, get_by_id

router = APIRouter(prefix="/skill", tags=["skills"])

@router.post("/")
def create_skill(skill: SkillCreate, db: Session = Depends(get_db)):
    return create(db, skill)

@router.get("/")
def get_skills(db: Session = Depends(get_db)):
    return get_all(db)

@router.get("/{id}")
def get_skill(id: int, db: Session = Depends(get_db)):
    return get_by_id(db, id)
