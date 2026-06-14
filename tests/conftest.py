from dotenv import load_dotenv
import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.database.models import Base


load_dotenv()

DB_TEST_URL = os.getenv("DB_TEST_CONN_STRING")
engine = create_engine(DB_TEST_URL)
session_factory = sessionmaker(bind=engine)

@pytest.fixture(autouse=True, scope="session")
def setup_database():
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


def 

