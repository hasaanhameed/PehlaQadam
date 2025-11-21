from sqlalchemy.orm import Session
from backend import models, schema
from backend.hashing import Hash

# Logic for User Operations 

# Create a new User
def create(db : Session, user: schema.UserCreate):
    hashed_pw = Hash.bcrypt(user.password)
    new_user = models.User(
        name = user.name,
        email = user.email,
        hashed_password = hashed_pw
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Get all Users
def get_all(db : Session):
    return db.query(models.User).all()

# Get a User by ID
def get_by_id(db : Session, id: int):
    return db.query(models.User).filter(models.User.id == id).first()



