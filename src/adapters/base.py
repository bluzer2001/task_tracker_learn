from typing import Type
from src.database.models import Base
from src.protocols import EntityType, Entity


class Mapper:

    def __init__(self, model_class: Type[Base], entity_class: EntityType, fields: tuple[str, ...]):
        self._model_class = model_class
        self._entity_class = entity_class
        self.fields = fields

    def to_model(self, entity: Entity) -> Base:
        return self._model_class(**self._values(entity))

    def to_entity(self, model: Base) -> Entity:
        return self._entity_class(**self._values(model))

    def many_to_models(self, entities: list[Entity]) -> list[Base]:
        return [self.to_model(entity) for entity in entities]

    def many_to_entities(self, models: list[Base]) -> list[Entity]:
        return [self.to_entity(model) for model in models]

    def update_model(self, entity: Entity, model: Base):
        entity_fields = self._values(entity)
        for field, value in entity_fields.items():
            setattr(model, field, value)

    def _values(self, source: Base | Entity) -> dict[str, object]:
        return {field: getattr(source, field) for field in self.fields}