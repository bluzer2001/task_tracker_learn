import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, field_serializer, Field


class TaskSchema(BaseModel):
    name: str
    is_closed: bool = False
    deadline: datetime | None = None
    assignee_id: uuid.UUID | None = None
    tags: list[uuid.UUID] | None = None

    model_config = ConfigDict(extra="forbid")

    @field_serializer("tags")
    def serialize_tags(self, tags: list[uuid.UUID]) -> list[str]:
        return [str(tag) for tag in tags]


class TaskCreateSchema(TaskSchema):
    pass


class TaskUpdateSchema(TaskSchema):
    name: str | None = None


class TaskDetailsSchema(TaskSchema):
    id_: uuid.UUID = Field(serialization_alias="id")