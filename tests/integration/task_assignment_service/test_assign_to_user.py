from tests.factories import TaskAlchemyFactory, UserAlchemyFactory

def test_assign_to_user_success(task_assignment_service):
    task = TaskAlchemyFactory()
    user = UserAlchemyFactory()
    returned_task = task_assignment_service(task_id=task.id_, user_id=user.id_)
    assert returned_task.assignee_id == user.id_
