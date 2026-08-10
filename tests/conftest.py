import pytest

from src.database.models import Base
from tests.session_for_test import engine, session_factory

from src.repositories import UserAlchemyRepository, TaskAlchemyRepository
from src.service import TaskAssignmentService


@pytest.fixture(autouse=True, scope="session")
def setup_database():
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


@pytest.fixture
def session():
    session = session_factory()
    try:
        yield session
    finally:
        session.rollback()
        session.close()


@pytest.fixture
def user_repo(session):
    return UserAlchemyRepository(session)


@pytest.fixture
def task_repo(session):
    return TaskAlchemyRepository(session)


@pytest.fixture
def task_assignment_service(user_repo, task_repo):
    return TaskAssignmentService(task_repo, user_repo)
