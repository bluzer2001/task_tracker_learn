from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config.database import DB_TEST_URL

engine = create_engine(DB_TEST_URL)
session_factory = sessionmaker(bind=engine)