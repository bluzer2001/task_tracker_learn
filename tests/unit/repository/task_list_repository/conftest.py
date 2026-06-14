from .fake_repository import TaskListRepository
from src.models import Task
from pytest import fixture


@fixture
def task_base_repository():
    return TaskFakeRepository()
