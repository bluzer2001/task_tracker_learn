from pydantic import BaseModel


class TaskCreateSchema(BaseModel):
    name: str
    is_closed: bool = False


class TaskUpdateSchema(BaseModel):
    name: str | None = None
    is_closed: bool | None = None


class TaskDetailsSchema(BaseModel):
    id: int
    name: str
    is_closed: bool