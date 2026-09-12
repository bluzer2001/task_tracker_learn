import logging
from src.service import TaskAssignmentService
from src.config.logging import configure_logging
from src.queues import RedisNotificationsQueue
from src.repositories import TaskAlchemyRepository, UserAlchemyRepository
from src.database.sqllite import session_factory, init_and_clear_db
from src.redis_client import redis_client
from src.constants import NOTIFICATION_QUEUE, ANALYSIS_QUEUE
from src.models import User, Task
from time import time

configure_logging()

def assign_to_user():
    # with session_factory() as session:
    session = session_factory()
    task_repo = TaskAlchemyRepository(session)
    user_repo = UserAlchemyRepository(session)

    notification_queue = RedisNotificationsQueue(redis_client, NOTIFICATION_QUEUE)
    analytic_message_queue = RedisNotificationsQueue(redis_client, ANALYSIS_QUEUE)
    task_user_service = TaskAssignmentService(task_repo, user_repo, notification_queue, analytic_message_queue=analytic_message_queue)

    user = User(name="test_user", email="example")
    task = Task(name="test_task")

    with init_and_clear_db():
        user_repo.add(user)
        task_repo.add(task)
        time_start = time()
        task = task_user_service(task_id=task.id_, user_id=user.id_)
        time_end = time()
        print(f"Время работы {time_end - time_start}")
        session.close()
        return task


if __name__ == "__main__":
    from time import sleep
    while True:
        assign_to_user()
        sleep(2)
