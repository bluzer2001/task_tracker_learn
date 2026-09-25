__all__ = ("TasksService",)

from src.models import Task
from src.repositories.tasks import TaskBaseRepository
from datetime import datetime


class TasksService:

    def __init__(self, repository: TaskBaseRepository):
        self.repository = repository

    def close_task_by_id(self, id_: str):
        task = self.repository.get_by_id(id_)
        task.is_closed = True
        self.repository.update(task)

    def close_tasks(self, ids: list[str]):
        for task_id in ids:
            self.close_task_by_id(task_id)

    def get_tasks(self, is_closed: bool | None = None) -> list[Task]:
        if is_closed is None:
            return self.repository.get_all()
        return self.repository.filter(is_closed=is_closed)

    def get_tasks_by_deadline(self, start_date: datetime | None = None, end_date: datetime | None= None):
        tasks = self.repository.get_all()
        if start_date:
            tasks = filter(lambda task: task.deadline >= start_date, tasks)

        if end_date:
            tasks = filter(lambda task: task.deadline <= end_date, tasks)
        return list(tasks)



