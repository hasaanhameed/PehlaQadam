from sqlalchemy.orm import Session
from backend import models, schema


# CREATE INTERNSHIP
def create(db: Session, internship: schema.InternshipCreate):
    new_internship = models.Internship(
        title=internship.title,
        company_name=internship.company_name,
        city=internship.city,
        description=internship.description,
        required_skills=internship.required_skills,
        interests=internship.interests,
        work_type=internship.work_type,
        major_required=internship.major_required,
        stipend=internship.stipend
    )
    db.add(new_internship)
    db.commit()
    db.refresh(new_internship)
    return new_internship


# GET ALL INTERNSHIPS
def get_all(db: Session):
    return db.query(models.Internship).all()


# GET INTERNSHIP BY ID
def get_by_id(db: Session, internship_id: int):
    return db.query(models.Internship).filter(models.Internship.id == internship_id).first()
