__all__ = ("UserModel", )

import uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models import TaskModel
from src.database.models.base import Base


class UserModel(Base):
    __tablename__ = "user"

    id_: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str]
    email: Mapped[str]
    is_blocked: Mapped[bool] = mapped_column(default=False)

    tasks: Mapped[list["TaskModel"]] = relationship("TaskModel", back_populates="assignee")
