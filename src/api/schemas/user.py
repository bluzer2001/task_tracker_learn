from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    name: str
    is_blocked: bool = False


class UserUpdateSchema(BaseModel):
    name: str | None = None
    is_blocked: bool | None = None
