from fastapi import Depends
from sqlalchemy.orm import Session

from database.sqllite import get_session
from src.repositories.tasks import TaskAlchemyRepository


def get_task_repository(session: Session = Depends(get_session())):
    return TaskAlchemyRepository(session)