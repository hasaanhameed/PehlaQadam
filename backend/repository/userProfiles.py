from sqlalchemy.orm import Session
from backend import models, schema


# CREATE PROFILE
def create(db: Session, profile: schema.UserProfileCreate):
    new_profile = models.UserProfile(
        user_id=profile.user_id,
        full_name=profile.full_name,
        major=profile.major,
        degree_level=profile.degree_level,
        preferred_cities=profile.preferred_cities,
        preferred_work_type=profile.preferred_work_type
    )
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return new_profile


# GET PROFILE BY USER ID
def get_by_id(db: Session, user_id: int):
    return db.query(models.UserProfile).filter(models.UserProfile.user_id == user_id).first()


# UPDATE PROFILE
def update_by_id(db: Session, user_id: int, updates: schema.UserProfile):
    profile = get_by_id(db, user_id)
    if not profile:
        return None

    profile.full_name = updates.full_name
    profile.major = updates.major
    profile.degree_level = updates.degree_level
    profile.preferred_cities = updates.preferred_cities
    profile.preferred_work_type = updates.preferred_work_type

    db.commit()
    db.refresh(profile)
    return profile
