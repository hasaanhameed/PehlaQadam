from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

databaseURL = DATABASE_URL = "postgresql://postgres:hasaan@localhost:5432/pehlaqadam"
engine = create_engine(DATABASE_URL)

session = sessionmaker(bind = engine, autocommit=False, autoflush=False)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

