import logging
from src.exceptions import TaskNotFoundError, UserNotFoundError, UserBlockedError
from src.models import Task, User, AnalyticMessage, Notification
from src.repositories.tasks import TaskBaseRepository
from src.repositories.user import UserAlchemyRepository
from src.queues import BaseQueue

logger = logging.getLogger(__name__)

class TaskAssignmentService:

    def __init__(self,
                 task_repo: TaskBaseRepository,
                 user_repo: UserAlchemyRepository,
                 notification_queue: BaseQueue,
                 analytic_message_queue: BaseQueue):
        self.user_repo = user_repo
        self.task_repo = task_repo
        self.notification_queue = notification_queue
        self.analytic_message_queue = analytic_message_queue

    def __call__(self, task_id: str, user_id: str) -> Task:
        return self.run(task_id=task_id, user_id=user_id)

    def run(self, task_id: str, user_id: str) -> Task:
        task = self._get_task(task_id)
        user = self._get_user(user_id)
        self._check_user_blocked(user)

        task.assign(user)
        self.task_repo.update(task)
        logger.info("Задача %s назначана для пользователя %s", task_id, user_id)
        self.notification_queue.publish(
            Notification(email=user.email, body=f"назначана задача {task_id}")
        )
        logger.debug(
            "Уведомление по задаче task_id=%s отправлено в очередь %s",
            task_id,
            self.notification_queue.queue_name
        )
        self.analytic_message_queue.publish(AnalyticMessage(event_name="назначана задача", user_id=str(user_id)))
        return task

    def _get_task(self, task_id: str) -> Task:
        logger.debug("Получаем задачу id=%s", task_id)
        task = self.task_repo.get_by_id(task_id)
        if task is None:
            logger.error("Задача с id=%s не найдена", task_id)
            raise TaskNotFoundError
        logger.debug("Получили задачу id=%s", task_id)
        return task

    def _get_user(self, user_id: str) -> User:
        logger.debug("Получаем пользователя id=%s", user_id)
        user = self.user_repo.get_by_id(user_id)
        if user is None:
            logger.error("Пользователь с id=%s не найден", user_id)
            raise UserNotFoundError
        logger.debug("Получили пользователя id=%s", user_id)
        return user

    def _check_user_blocked(self, user: User):
        if user.is_blocked:
            logger.warning("Попытка назначить задачу на заблокированного пользователя %s", user.id_)
            raise UserBlockedError