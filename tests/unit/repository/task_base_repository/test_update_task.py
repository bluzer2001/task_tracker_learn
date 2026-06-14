from unittest.mock import MagicMock
from src.exceptions.task import TaskNotFoundError
from src.models import Task
from tests.factories.task_factory import TaskFactory
from faker import Faker
import random
import pytest
from dataclasses import fields
from datetime import datetime

fake = Faker()

type_to_faker = {
    int: fake.pyint,
    float: fake.pyfloat,
    str: fake.pystr,
    bool: fake.pybool,
    list: lambda : fake.pylist(allowed_types=[str]),
    dict: fake.pydict,
    datetime: fake.date_time,
}

def _generate_by_type(target_type):
    generator = type_to_faker.get(target_type, fake.pystr)
    return generator()

def _generate_kwargs():
    model_field = random.choice(list(filter(lambda x: x.name != "id_", fields(Task))))
    kwarg = {
        model_field.name: _generate_by_type(model_field.type)
    }
    return kwarg


def test_update_task_not_found(task_base_repository):
    repository = task_base_repository
    repository.get_by_id = MagicMock(return_value=None)

    with pytest.raises(TaskNotFoundError):
        task_id = fake.uuid4()
        repository.update_task(task_id)
        repository.get_by_id.assert_called_once_with(task_id)


def test_update_task_success(task_base_repository):
    repository = task_base_repository
    task = TaskFactory()
    repository.get_by_id = MagicMock(return_value=task)

    kwargs = _generate_kwargs()
    repository.update_task(task.id_, **kwargs)
    attr_name, attr_value = list(kwargs.items())[0]
    assert getattr(task, attr_name) == attr_value




