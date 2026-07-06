import pytest

from src.database.models import Base
from tests.session_for_test import engine


@pytest.fixture(autouse=True, scope="session")
def setup_database():
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


