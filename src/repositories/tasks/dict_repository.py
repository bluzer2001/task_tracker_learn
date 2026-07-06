__all__ = ("TaskDictRepository",)

import uuid

from .base import TaskBaseRepository
from src.models import Task
import operator

filter_dict = {
    "eq": operator.eq,
    "gt": operator.gt,
    "lt": operator.lt,
    "gte": operator.ge,
    "lte": operator.le,
}


class TaskDictRepository(TaskBaseRepository):

    def __init__(self):
        self.tasks = {}

    def save(self, task: Task):
        task.id_ = uuid.uuid4()
        self.tasks[task.id_] = task

    def get_by_id(self, task_id: str):
        return self.tasks.get(task_id)

    def get_all(self) -> list:
        return list(self.tasks.values())

    def filter(self, **kwargs):
        result = []

        for key, value in kwargs.items():
            if "__" in key:
                attr_name, op = key.split("__")
            else:
                attr_name = key
                op = "eq"

            for task in self.tasks.values():
                if all(
                    hasattr(task, attr_name) and filter_dict[op](getattr(task, attr_name), value)
                    for attr_name, value in kwargs.items()
                ):
                    result.append(task)


        # for task in self.tasks.values():
        #     if all(
        #         hasattr(task, attr_name) and getattr(task, attr_name) == value
        #         for attr_name, value in kwargs.items()
        #     ):
        #         result.append(task)

        return result