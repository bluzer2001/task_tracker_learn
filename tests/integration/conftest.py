import pytest

from src.repositories import UserAlchemyRepository, TaskAlchemyRepository
from src.service import TaskAssignmentService
from tests.session_for_test import session_factory

@pytest.fixture
def user_repo(session):
    return UserAlchemyRepository(session)

@pytest.fixture
def task_repo(session):
    return TaskAlchemyRepository(session)

@pytest.fixture
def task_assignment_service(user_repo, task_repo):
    return TaskAssignmentService(task_repo, user_repo)
