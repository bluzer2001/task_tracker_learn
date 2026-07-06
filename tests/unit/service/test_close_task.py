from src.service import TasksService
from tests.factories.task_factory import TaskFactory
from tests.unit.service.fake_repositry import TaskFakeRepository
from random import randint, sample


def test_close_by_id():
    task = TaskFactory()
    repository = TaskFakeRepository([task])
    service = TasksService(repository)

    service.close_task_by_id(task.id_)
    assert task.is_closed


def test_close_tasks():
    tasks_to_close = TaskFactory.create_batch(randint(2, 100))
    tasks_other = TaskFactory.create_batch(randint(2, 100), is_closed=False)
    repository = TaskFakeRepository(tasks_to_close + tasks_other)
    service = TasksService(repository)

    task_to_close_ids = [task.id_ for task in tasks_to_close]

    service.close_tasks(task_to_close_ids)

    assert all(task.is_closed for task in tasks_to_close)
    assert all(not task.is_closed for task in tasks_other)


def test_get_active_tasks():
    closed_tasks = TaskFactory.create_batch(randint(2, 100), is_closed=True)
    active_tasks = TaskFactory.create_batch(randint(2, 100), is_closed=False)
    repository = TaskFakeRepository(closed_tasks + active_tasks)
    service = TasksService(repository)

    result_tasks = service.get_active_tasks()

    assert set(task.id_ for task in active_tasks) == set(task.id_ for task in result_tasks)


def