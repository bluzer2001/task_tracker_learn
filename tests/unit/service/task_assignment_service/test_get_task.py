import uuid

import pytest

from src.exceptions import TaskNotFoundError
from tests.factories import TaskAlchemyFactory


def test_get_task_not_found(task_assignment_service):
    with pytest.raises(TaskNotFoundError):
        task_assignment_service._get_task(uuid.uuid4())


def test_get_task_success(task_assignment_service):
    task = TaskAlchemyFactory()
    result_task = task_assignment_service._get_task(task.id_)
    assert task.id_ == result_task.id_
    assert task.deadline == result_task.deadline
    assert task.name == result_task.name
    assert task.is_closed == result_task.is_closed
    assert task.tags == result_task.tags
    assert task.assignee_id == result_task.assignee_id