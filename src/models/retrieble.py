from dataclasses import dataclass

@dataclass
class Retriable:

    retries: int = 0
    error: str | None = None