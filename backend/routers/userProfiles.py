from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.schema import UserProfileCreate, UserProfile
from backend.repository.userProfiles import create, get_by_id, update_by_id

router = APIRouter(prefix="/userProfile", tags=["userProfiles"])

@router.post("/")
def create_user_profile(profile: UserProfileCreate, db: Session = Depends(get_db)):
    return create(db, profile)

@router.get("/{id}")
def get_user_profile(id: int, db: Session = Depends(get_db)):
    return get_by_id(db, id)

@router.put("/{id}")
def update_user_profile(id: int, profile: UserProfile, db: Session = Depends(get_db)):
    return update_by_id(db, id, profile)
