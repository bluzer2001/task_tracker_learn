import uuid
from datetime import datetime

from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from src.database.models.base import Base



class TaskModel(Base):
    __tablename__ = "task"

    id_: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str]
    is_closed: Mapped[bool] = mapped_column(default=False)
    deadline: Mapped[datetime] = mapped_column(nullable=True)
    tags: Mapped[list[str]] = mapped_column(JSON, default=list)
    assignee_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id_"), nullable=True)

    assignee: Mapped["UserModel"] = relationship("UserModel", back_populates="tasks")
