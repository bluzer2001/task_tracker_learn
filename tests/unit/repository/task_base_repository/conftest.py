
from .fake_repository import TaskFakeRepository
from pytest import fixture


@fixture
def task_base_repository():
    return TaskFakeRepository()
