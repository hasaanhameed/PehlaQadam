from sqlalchemy.orm import Session
from backend import models, schema


# CREATE SKILL
def create(db: Session, skill: schema.SkillCreate):
    new_skill = models.Skill(name=skill.name)
    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)
    return new_skill


# GET ALL SKILLS
def get_all(db: Session):
    return db.query(models.Skill).all()


# GET SKILL BY ID
def get_by_id(db: Session, skill_id: int):
    return db.query(models.Skill).filter(models.Skill.id == skill_id).first()
