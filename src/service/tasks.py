__all__ = ("TasksService",)

from src.exceptions import TaskNotFoundError
from src.models import Task
from src.repositories.base import BaseRepository
from datetime import datetime

from tests.unit.repository import task_list_repository


class TasksService:

    def __init__(self, repository: BaseRepository):
        self.repository = repository

    def close_task_by_id(self, id_: str):
        task = self.repository.get_by_id(id_)
        task.is_closed = True
        self.repository.update(task, commit=True)

    def close_tasks(self, ids: list[str]):
        for task_id in ids:
            self.close_task_by_id(task_id)

    def get_tasks(self, is_closed: bool | None = None) -> list[Task]:
        if is_closed is None:
            return self.repository.get_all()
        return self.repository.filter(is_closed=is_closed)

    def get(self, task_id: str) -> Task:
        task = self.repository.get_by_id(task_id)
        if not task:
            raise TaskNotFoundError(task_id)
        return task

    def get_tasks_by_deadline(self, start_date: datetime | None = None, end_date: datetime | None= None):
        tasks = self.repository.get_all()
        if start_date:
            tasks = filter(lambda task: task.deadline >= start_date, tasks)

        if end_date:
            tasks = filter(lambda task: task.deadline <= end_date, tasks)
        return list(tasks)

    def create(self, **kwargs) -> Task:
        task = Task(**kwargs)
        self.repository.add(task, commit=True)
        return task

    def update(self, task_id: str, **kwargs) -> Task:
        task = self.repository.get_by_id(task_id)
        task.update(**kwargs)
        return self.repository.update(task, commit=True)


    def delete(self, task_id: str) -> bool:
        return  self.repository.delete(task_id)


