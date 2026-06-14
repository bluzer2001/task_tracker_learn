_all__ = ("Tag", )

from dataclasses import dataclass, field
import uuid


@dataclass
class Tag:
    name: str
    id_: str = field(default_factory=lambda : uuid.uuid4())
