from src.service import EmailService
from src.queues import RedisNotificationsQueue
from src.redis_client import redis_client
from src.constants import NOTIFICATION_QUEUE
import multiprocessing


class NotificationWorker:

    def __init__(self, queue: RedisNotificationsQueue, email_service: EmailService):
        self.queue = queue
        self.email_service = email_service

    def run(self):
        print("worker запущен")
        while True:
            notification = self.queue.consume()
            self.email_service.send(notification)


if __name__ == "__main__":
    queue = RedisNotificationsQueue(redis_client, NOTIFICATION_QUEUE)
    worker = NotificationWorker(queue, EmailService())
    worker.run()
