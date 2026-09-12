from dataclasses import dataclass, field
from .retrieble import Retriable
import uuid

@dataclass(kw_only=True)
class Notification(Retriable):
    id_: str = field(default_factory=lambda: str(uuid.uuid4()))
    email: str
    body: str