from fastapi import FastAPI
from backend.routers import users, internships, skills, interests
from backend import models
from backend.database import engine

app = FastAPI()

models.Base.metadata.create_all(engine) # Creates all tables

app.include_router(users.router)
app.include_router(internships.router)
app.include_router(skills.router)
app.include_router(interests.router)

