__all__ = ("TaskAlchemyRepository",)

from sqlalchemy import select, and_
from sqlalchemy.orm import Session

from .base import TaskBaseRepository
from src.adapters import TaskMapper
from src.models import Task
from src.database.models import TaskModel as AlchemyTask


class TaskAlchemyRepository(TaskBaseRepository):

    def __init__(self, session: Session):
        self.session = session

    def save(self, task: Task):
        model_task = TaskMapper.to_model(task)
        self.session.add(model_task)
        self.session.commit()
        task.id_ = model_task.id_

    def get_by_id(self, task_id: str):
        task_model = self.session.get(AlchemyTask, task_id)
        if task_model:
            return TaskMapper.to_entity(task_model)
        return None

    def get_all(self) -> list:
        task_models = self.session.query(AlchemyTask).all()
        return TaskMapper.many_to_entity(task_models)

    def update_task(self, id_: str, **kwargs) -> Task:
        task = super().update_task(id_=id_, **kwargs)
        self.save(task)
        return task

    def filter(self, **kwargs):
        stmt = select(AlchemyTask)
        filters = []

        for column_name, value in kwargs.items():
            column = getattr(AlchemyTask, column_name)
            filters.append(column==value)
        print(filters, type(filters[0]))

        if filters:
            stmt = stmt.where(and_(*filters))
        result = self.session.execute(stmt).all()
        return TaskMapper.many_to_entity(result)


