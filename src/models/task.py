__all__ = ("Task", )

from dataclasses import dataclass, field
from datetime import datetime
import uuid
from .user import User

# from .tag import Tag


@dataclass
class Task:
    name: str
    deadline: datetime | None = None
    is_closed: bool = False
    id_: uuid.UUID | None = None
    tags: list[str] = field(default_factory=list[str])
    assignee_id: str | None = None

    def assign(self, user: User):
        self.assignee_id = user.id_

