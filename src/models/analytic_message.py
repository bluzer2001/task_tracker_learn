from dataclasses import dataclass, field
import uuid
from .retrieble import Retriable

@dataclass(kw_only=True)
class AnalyticMessage(Retriable):
    id_: str = field(default_factory=lambda: str(uuid.uuid4()))
    event_name: str
    user_id: str
