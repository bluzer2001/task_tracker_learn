from fastapi import Depends
from src.api.dependencies import get_task_repository

from src.service.tasks import TasksService
from src.repositories.tasks import TaskAlchemyRepository


def get_task_service(task_repo: TaskAlchemyRepository = Depends(get_task_repository)):
    return TasksService(task_repo)