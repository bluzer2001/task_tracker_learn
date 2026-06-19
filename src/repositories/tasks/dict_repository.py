__all__ = ("TaskDictRepository",)

from .base import TaskBaseRepository
from src.models import Task


class TaskDictRepository(TaskBaseRepository):

    def __init__(self):
        self.tasks = {}

    def save(self, task: Task):
        self.tasks[task.id_] = task

    def get_by_id(self, task_id: str):
        return self.tasks.get(task_id)

    def get_all(self) -> list:
        return list(self.tasks.values())

    def filter(self, **kwargs):
        result = []

        for task in self.tasks.values():
            if all(
                hasattr(task, attr_name) and getattr(task, attr_name) == value
                for attr_name, value in kwargs.items()
            ):
                result.append(task)

        return result