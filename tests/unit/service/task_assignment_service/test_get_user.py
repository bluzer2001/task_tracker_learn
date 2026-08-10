import uuid

import pytest

from src.exceptions import UserNotFoundError
from tests.factories import UserAlchemyFactory


def test_get_user_not_found(task_assignment_service):
    with pytest.raises(UserNotFoundError):
        task_assignment_service._get_user(uuid.uuid4())


def test_get_user_success(task_assignment_service):
    user = UserAlchemyFactory()
    result_user = task_assignment_service._get_user(user.id_)
    assert user.id_ == result_user.id_
    assert user.email == result_user.email
    assert user.name == result_user.name
    assert user.is_blocked == result_user.is_blocked


