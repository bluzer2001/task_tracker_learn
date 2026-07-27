import pytest

from src.repositories import UserAlchemyRepository, TaskAlchemyRepository
from src.service import TaskAssignmentService
from tests.session_for_test import session_factory

@pytest.fixture
def user_repo():
    return UserAlchemyRepository(session_factory)

@pytest.fixture
def task_repo():
    return TaskAlchemyRepository(session_factory)

@pytest.fixture
def task_assignment_service(user_repo, task_repo):
    return TaskAssignmentService(task_repo, user_repo)
