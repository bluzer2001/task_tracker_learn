from dataclasses import dataclass
from .retrieble import Retriable

@dataclass(kw_only=True)
class AnalyticMessage(Retriable):
    event_name: str
    user_id: str
