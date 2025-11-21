from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.schema import UserCreate
from backend.repository.user import create, get_all, get_by_id

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create(db, user)

@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return get_all(db)

@router.get("/{id}")
def get_user(id: int, db: Session = Depends(get_db)):
    return get_by_id(db, id)
