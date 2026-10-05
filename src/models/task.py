__all__ = ("Task", )

from dataclasses import dataclass, field, fields
from datetime import datetime
import uuid
from .user import User

# from .tag import Tag


@dataclass
class Task:
    name: str
    deadline: datetime | None = None
    is_closed: bool = False
    id_: uuid.UUID = field(default_factory=uuid.uuid4)
    tags: list[uuid.UUID] = field(default_factory=list)
    assignee_id: uuid.UUID | None = None
    is_deleted: bool = False

    def assign(self, user: User):
        self.assignee_id = user.id_

    def update(self, **kwargs):
        editable = {f.name for f in fields(self)} - {"id_"}
        unknown = set(kwargs) - editable
        if unknown:
            raise TypeError(f"Нельзя изменить поля: {', '.join(sorted(unknown))}")

        for name, value in kwargs.items():
            if value is not None:
                setattr(self, name, value)
        return self
