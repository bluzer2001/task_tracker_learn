from datetime import datetime

from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base


class Task(Base):
    __tablename__ = "task"

    id_: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    is_closed: Mapped[bool] = mapped_column(default=False)
    deadline: Mapped[datetime] = mapped_column(nullable=True)
    tags: Mapped[list[str]] = mapped_column(JSON, default=list)

