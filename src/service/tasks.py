__all__ = ("TasksService",)

from src.repositories.tasks import TaskBaseRepository
from datetime import datetime


class TasksService:

    def __init__(self, repository: TaskBaseRepository):
        self.repository = repository

    def close_task_by_id(self, id_: str):
        self.repository.update_task(id_=id_, is_closed=True)

    def close_tasks(self, ids: list[str]):
        for task_id in ids:
            self.close_task_by_id(task_id)

    def get_active_tasks(self):
        return list(filter(lambda task: not task.is_closed, self.repository.get_all()))

    def get_tasks_by_deadline(self, start_date: datetime | None = None, end_date: datetime | None= None):
        tasks = self.repository.get_all()
        if start_date:
            tasks = filter(lambda task: task.deadline >= start_date, tasks)

        if end_date:
            tasks = filter(lambda task: task.deadline <= end_date, tasks)
        return list(tasks)



