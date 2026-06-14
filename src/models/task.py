__all__ = ("Task", )

from dataclasses import dataclass, field, fields
from datetime import datetime
import uuid

# from .tag import Tag


@dataclass
class Task:
    name: str
    deadline: datetime | None = None
    is_closed: bool = False
    id_: str = field(default_factory=lambda : uuid.uuid4())
    tags: list[str] = field(default_factory=list[str])


import inspect

attrs = {
    name: val
    for name, val in Task.__dict__.items()
    if not name.startswith("__")
}

