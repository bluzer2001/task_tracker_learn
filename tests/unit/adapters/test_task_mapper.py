from src.models import Task
from src.database.models import TaskModel as AlchemyTask
from src.adapters import TaskMapper
from tests.factories.task_factory import TaskFactory, TaskAlchemyFactory
from sqlalchemy import inspect
from dataclasses import fields


def _assert_attrs_identity(model, task):
    task_attrs = set(attr.name for attr in fields(task))
    model_attrs = set(attr.name for attr in inspect(model).mapper.columns)
    assert task_attrs == model_attrs
    for attr in model_attrs:
        assert getattr(model, attr) == getattr(task, attr)


def test_entity_to_model():
    task = TaskFactory()
    model = TaskMapper.to_model(task)
    _assert_attrs_identity(model, task)


def test_model_to_entity():
    model = TaskAlchemyFactory()
    task = TaskMapper.to_entity(model)
    _assert_attrs_identity(model, task)
