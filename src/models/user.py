__all__ = ("User", )

from dataclasses import dataclass, field, fields
import uuid

@dataclass
class User:
    email: str
    name: str
    id_: uuid.UUID | None = None
    is_blocked: bool = False
