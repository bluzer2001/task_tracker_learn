
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config.database import DB_URL
from .models import Base
from contextlib import contextmanager


engine = None

def get_engine():
    global engine
    if engine:
        return engine
    engine = create_engine(DB_URL)
    return engine

session_factory = sessionmaker(bind=get_engine())

@contextmanager
def init_and_clear_db():
    engine = get_engine()
    Base.metadata.create_all(engine)
    try:
        yield
    finally:
        Base.metadata.drop_all(engine)