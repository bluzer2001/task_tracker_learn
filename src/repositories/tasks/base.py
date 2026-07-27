__all__ = ("TaskBaseRepository",)

from abc import abstractmethod
from src.exceptions.task import TaskNotFoundError
from src.repositories.base import BaseRepository
from datetime import datetime

from src.models.task import Task


class TaskBaseRepository(BaseRepository):

    @abstractmethod
    def filter(self, **kwargs):
        pass