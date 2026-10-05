__all__ = ("TaskAlchemyRepository",)

from sqlalchemy import select, and_
from sqlalchemy.orm import Session

from .base import TaskBaseRepository
from src.adapters import TaskMapper
from src.models import Task
from src.database.models import TaskModel as AlchemyTask
from ...exceptions import TaskNotFoundError


class TaskAlchemyRepository(TaskBaseRepository):

    def __init__(self, session: Session):
        self.session = session

    def add(self, task: Task, commit: bool = False):
        model_task = TaskMapper.to_model(task)
        self.session.add(model_task)
        if commit:
            self.session.commit()

    def get_by_id(self, task_id: str) -> Task:
        task_model = self.session.get(AlchemyTask, task_id)

        if task_model and not task_model.is_deleted:
            return TaskMapper.to_entity(task_model)
        return None

    def get_all(self) -> list:
        return self.filter(is_deleted=False)

    def update(self, task: Task, commit: bool = False):
        model_task = self.session.get(AlchemyTask, task.id_)
        if not model_task:
            raise TaskNotFoundError(f"Нет задачи с id = {task.id_}")
        TaskMapper.update_model(entity=task, model=model_task)
        if commit:
            self.session.commit()
        return task

    def filter(self, **kwargs):
        stmt = select(AlchemyTask)
        filters = []

        for column_name, value in kwargs.items():
            column = getattr(AlchemyTask, column_name)
            filters.append(column==value)

        if filters:
            stmt = stmt.where(and_(*filters))
        result = self.session.execute(stmt)
        models = result.scalars().all()
        return TaskMapper.many_to_entity(models)

    def delete(self, task_id: str):
        task = self.session.get(AlchemyTask, task_id)
        if not task or task.is_deleted:
            return False
        task.is_deleted = True
        self.session.commit()
        return True

