from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    
class UserProfile(Base):
    __tablename__ = 'user_profiles'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)

    full_name = Column(String, index=True)
    major = Column(String, index=True)
    degree_level = Column(String, index=True)  

    preferred_cities = Column(ARRAY(String))        
    preferred_work_types = Column(ARRAY(String))    

class Skill(Base):
    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    
class UserSkill(Base):
    __tablename__ = 'user_skills'

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    skill_id = Column(Integer, ForeignKey("skills.id"), primary_key=True)

class Interest(Base):
    __tablename__ = 'interests'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class UserInterest(Base):
    __tablename__ = 'user_interests'
    
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    interest_id = Column(Integer, ForeignKey("interests.id"), primary_key=True)

class Internship(Base):
    __tablename__ = 'internships'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    company_name = Column(String)
    city = Column(String, index=True)
    description = Column(String)

    required_skills = Column(ARRAY(String))    
    interests = Column(ARRAY(String))           
    work_type = Column(String)                 
    major_required = Column(String)          
    stipend = Column(String)
