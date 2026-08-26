from dataclasses import dataclass


@dataclass
class Notification:
    email: str
    body: str
