from typing import Protocol, Any, ClassVar

class Entity(Protocol):
    _dataclass_fields: ClassVar[dict[str, Any]]


class EntityType(Protocol):

    def __call__(self, **kwargs: Any) -> Entity: ...