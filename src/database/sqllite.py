
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config.database import DB_URL

engine = None

def get_engine():
    global engine
    if engine:
        return engine
    engine = create_engine(DB_URL)
    return engine

session_factory = sessionmaker(bind=get_engine())
