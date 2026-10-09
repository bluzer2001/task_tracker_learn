from abc import abstractmethod

from sqlalchemy import select, and_
from sqlalchemy.orm import Session
from typing import Type

from src.adapters.base import Mapper
from src.database.models import Base
from src.repositories.base import BaseRepository
from src.protocols import EntityType, Entity


class AlchemyRepository(BaseRepository):

    def __init__(self, session: Session):
        self.session = session

    @property
    @abstractmethod
    def model_class(self) -> Type[Base]:
        pass

    @property
    @abstractmethod
    def mapper(self) -> Mapper:
        pass

    def add(self, entity: Entity, commit: bool = False):
        model = self.mapper.to_model(entity)
        self.session.add(model)
        if commit:
            self.session.commit()

    def get_by_id(self, id_: str) -> Entity | None:
        model = self.session.get(self.model_class, id_)

        if not model:
            return None

        if hasattr(model, "is_deleted") and model.is_deleted:
            return None

        return self.mapper.to_entity(model)

    # TODO: Подумать над None и False
    def filter(self, is_deleted: bool | None = None, **kwargs):
        if not hasattr(self.model_class, "is_deleted"):

        stmt = select(self.model_class)
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
