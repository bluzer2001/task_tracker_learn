__all__ = ("TaskAlchemyRepository",)

from sqlalchemy.orm import Session

from .base import TaskBaseRepository
from src.database.models import Task as AlchemyTask


class TaskAlchemyRepository(TaskBaseRepository):
    _model_cls = AlchemyTask

    def __init__(self, session: Session):
        self.session = session

    def save(self, task: AlchemyTask):
        self.session.add(task)
        self.session.commit()

    def get_by_id(self, task_id: str):
        return self.session.get(self._model_cls, task_id)

    def get_all(self) -> list:
        return self.session.query(self._model_cls).all()