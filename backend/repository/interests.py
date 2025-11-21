from sqlalchemy.orm import Session
from backend import models, schema


# CREATE INTEREST
def create(db: Session, interest: schema.InterestCreate):
    new_interest = models.Interest(name=interest.name)
    db.add(new_interest)
    db.commit()
    db.refresh(new_interest)
    return new_interest


# GET ALL INTERESTS
def get_all(db: Session):
    return db.query(models.Interest).all()


# GET INTEREST BY ID
def get_by_id(db: Session, interest_id: int):
    return db.query(models.Interest).filter(models.Interest.id == interest_id).first()
