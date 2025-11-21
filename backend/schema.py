from pydantic import BaseModel
from typing import Optional, List


# User Schemas

class UserBase(BaseModel):
    name: str
    email: str
    
    
class UserCreate(UserBase):
    password: str
    
class UserResponse(UserBase):
    id: int 
    
    class Config:
        orm_mode: True
        

# UserProfile Schemas

class UserProfile(BaseModel):
    full_name: str
    major: str
    degree_level: str
    preferred_cities: List[str]
    preferred_work_type: str
    
class UserProfileCreate(UserProfile):
    user_id: int
    
class UserProfileResponse(UserProfile):
    id: int
    user_id: int
    
    class Config: 
        orm_mode: True
        

# User Skill Schemas
class SkillBase(BaseModel):
    name: str


class SkillCreate(SkillBase):
    pass


class SkillResponse(SkillBase):
    id: int

    class Config:
        orm_mode = True

    
# User Skill Schemas
class UserSkillBase(BaseModel):
    user_id: int
    skill_id: int


class UserSkillResponse(UserSkillBase):
    class Config:
        orm_mode = True
        
    
# Interest Schemas 

class InterestBase(BaseModel):
    name: str
    
class InterestCreate(InterestBase):
    pass

class InterestResponse(InterestBase):
    id: int

    class Config:
        orm_mode = True
    
# USER INTEREST SCHEMAS
class UserInterestBase(BaseModel):
    user_id: int
    interest_id: int


class UserInterestResponse(UserInterestBase):
    class Config:
        orm_mode = True

# INTERNSHIP SCHEMAS

class InternshipBase(BaseModel):
    title: str
    company_name: str
    city: str
    description: str
    required_skills: List[str]
    interests: List[str]
    work_type: str
    major_required: str
    stipend: str


class InternshipCreate(InternshipBase):
    pass


class InternshipResponse(InternshipBase):
    id: int

    class Config:
        orm_mode = True
