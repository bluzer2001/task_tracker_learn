__all__ = ("TaskAlchemyRepository",)

from sqlalchemy import select, and_
from sqlalchemy.orm import Session

from src.adapters import TaskMapper
from src.models import Task
from src.database.models import TaskModel as AlchemyTask
from ..alchemy import AlchemyRepository
from ..base import BaseRepository
from ...exceptions import TaskNotFoundError


class TaskAlchemyRepository(AlchemyRepository):

    def get_all(self) -> list:
        return self.filter()

    def update(self, task: Task, commit: bool = False):
        model_task = self.session.get(AlchemyTask, task.id_)
        if not model_task:
            raise TaskNotFoundError(f"Нет задачи с id = {task.id_}")
        TaskMapper.update_model(entity=task, model=model_task)
        if commit:
            self.session.commit()
        return task

    def filter(self, is_deleted: bool = False, **kwargs):
        stmt = select(AlchemyTask)
        filters = []
        kwargs["is_deleted"] = is_deleted

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

