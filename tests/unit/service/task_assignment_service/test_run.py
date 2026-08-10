from unittest.mock import patch, Mock

import pytest

from src.exceptions import UserBlockedError
from tests.factories import UserAlchemyFactory


@patch("src.service.task_assignment.TaskAssignmentService._get_user",)
@patch("src.service.task_assignment.TaskAssignmentService._get_task",)
@patch("src.service.task_assignment.TaskAssignmentService._check_user_blocked", new_callable=Mock)
def test_run_raise_user_blocked(user_blocked, get_task, get_user, task_assignment_service):
    user = Mock()
    task = Mock()

    get_user.return_value = user
    get_task.return_value = task

    with patch.object(task_assignment_service, "task_repo", new_callable=Mock) as task_repo:

        returned_task = task_assignment_service.run(task.id_, user.id_)

        get_task.assert_called_once_with(task.id_)
        get_user.assert_called_once_with(user.id_)
        user_blocked.assert_called_once_with(user)

        task.assign.assert_called_once_with(user)
        task_repo.update.assert_called_once_with(task)
    assert returned_task is task