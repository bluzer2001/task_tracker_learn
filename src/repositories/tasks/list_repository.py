__all__ = ("TaskListRepository",)

from .base import TaskBaseRepository
from src.models import Task


class TaskListRepository(TaskBaseRepository):

    def __init__(self):
        self.tasks = []

    def save(self, task: Task):
        self.tasks.append(task)

    def get_by_id(self, task_id: str):
        for task in self.tasks:
            if task.id_ == task_id:
                return task

    def get_all(self) -> list:
        return self.tasks

