__all__ = ("TaskBaseRepository",)

from abc import abstractmethod
from src.exceptions.task import TaskNotFoundError
from src.repositories.base import BaseRepository
from datetime import datetime

from src.models.task import Task


class TaskBaseRepository(BaseRepository):

    def create(self, name: str, deadline: datetime | None = None):
        new_task = Task(name=name, deadline=deadline)
        self.save(new_task)

    def update_task(self, id_: str, **kwargs) -> Task:
        task = self.get_by_id(id_)
        if not task:
            raise TaskNotFoundError(f"Нет task с id {id_}")

        for key, val in kwargs.items():
            if key in dir(task):
                setattr(task, key, val)
        return task

    @abstractmethod
    def filter(self, **kwargs):
        pass