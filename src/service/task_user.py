from src.exceptions import TaskNotFoundError, UserNotFoundError, UserBlockedError
from src.models import Task
from src.repositories.tasks import TaskBaseRepository
from src.repositories.user import UserAlchemyRepository


class TaskUserService:

    def __init__(self, task_repo: TaskBaseRepository, user_repo: UserAlchemyRepository):
        self.user_repo = user_repo
        self.task_repo = task_repo

    def assigne_task_to_user(self, task_id: str, user_id: str) -> Task:
        task = self.task_repo.get_by_id(task_id)
        if task is None:
            raise TaskNotFoundError

        user = self.user_repo.get_by_id(user_id)
        if user is None:
            raise UserNotFoundError

        if user.is_blocked:
            raise UserBlockedError

        task.assign(user)
        self.task_repo.save(task)
        return task



