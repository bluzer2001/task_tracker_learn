import pytest
from src.exceptions import UserBlockedError
from tests.factories import UserAlchemyFactory


def test_user_is_blocked(task_assignment_service):
    user = UserAlchemyFactory(is_blocked=True)
    with pytest.raises(UserBlockedError):
        task_assignment_service._check_user_blocked(user)


def test_user_noy_blocked(task_assignment_service):
    user = UserAlchemyFactory(is_blocked=False)
    task_assignment_service._check_user_blocked(user)