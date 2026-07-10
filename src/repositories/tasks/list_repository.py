__all__ = ("TaskListRepository",)

from .base import TaskBaseRepository
from src.models import Task
import uuid

class TaskListRepository(TaskBaseRepository):

    def __init__(self):
        self.tasks = []

    def add(self, task: Task):
        task.id_ = uuid.uuid4()
        self.tasks.append(task)

    def get_by_id(self, task_id: str):
        for task in self.tasks:
            if task.id_ == task_id:
                return task

    def get_all(self) -> list:
        return self.tasks

    def filter(self, **kwargs):
        result = []

        for task in self.tasks:
            if all(
                hasattr(task, attr_name) and getattr(task, attr_name) == value
                for attr_name, value in kwargs.items()
            ):
                result.append(task)

        return result