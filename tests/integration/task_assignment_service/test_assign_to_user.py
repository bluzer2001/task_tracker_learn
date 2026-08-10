import pytest

from src.exceptions import TaskNotFoundError, UserNotFoundError, UserBlockedError
from tests.factories import TaskAlchemyFactory, UserAlchemyFactory
import uuid

def test_assign_to_user_success(task_assignment_service):
    task = TaskAlchemyFactory()
    user = UserAlchemyFactory(is_blocked=False)
    returned_task = task_assignment_service(task_id=task.id_, user_id=user.id_)
    assert returned_task.assignee_id == user.id_


def test_assign_to_user_task_not_found(task_assignment_service):
    user = UserAlchemyFactory(is_blocked=False)
    with pytest.raises(TaskNotFoundError):
        task_assignment_service(task_id=uuid.uuid4(), user_id=user.id_)


def test_assign_to_user_user_not_found(task_assignment_service):
    task = TaskAlchemyFactory()
    with pytest.raises(UserNotFoundError):
        task_assignment_service(task_id=task.id_, user_id=uuid.uuid4())


def test_assign_to_user_user_blocked(task_assignment_service):
    task = TaskAlchemyFactory()
    user = UserAlchemyFactory(is_blocked=True)
    with pytest.raises(UserBlockedError):
        task_assignment_service(task_id=task.id_, user_id=user.id_)