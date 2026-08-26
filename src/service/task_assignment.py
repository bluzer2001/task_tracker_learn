from src.exceptions import TaskNotFoundError, UserNotFoundError, UserBlockedError
from src.models import Task, User
from src.repositories.tasks import TaskBaseRepository
from src.repositories.user import UserAlchemyRepository
from src.service.notification import Notification
from src.queues import NotificationsQueue


class TaskAssignmentService:

    def __init__(self,
                 task_repo: TaskBaseRepository,
                 user_repo: UserAlchemyRepository,
                 notification_queue: NotificationsQueue):
        self.user_repo = user_repo
        self.task_repo = task_repo
        self.notification_queue = notification_queue

    def __call__(self, task_id: str, user_id: str) -> Task:
        return self.run(task_id=task_id, user_id=user_id)

    def run(self, task_id: str, user_id: str) -> Task:
        task = self._get_task(task_id)
        user = self._get_user(user_id)
        self._check_user_blocked(user)

        task.assign(user)
        print("1 обновляем задачу")
        self.task_repo.update(task)
        print("2 Задача обновлена")
        self.notification_queue.publish(Notification(user.email, f"назначана задача {task_id}"))
        print("3 опубликовали задачу")
        return task

    def _get_task(self, task_id: str) -> Task:
        task = self.task_repo.get_by_id(task_id)
        if task is None:
            raise TaskNotFoundError
        return task

    def _get_user(self, user_id: str) -> User:
        user = self.user_repo.get_by_id(user_id)
        if user is None:
            raise UserNotFoundError

        return user

    def _check_user_blocked(self, user: User):
        if user.is_blocked:
            raise UserBlockedError