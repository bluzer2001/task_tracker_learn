import logging
from src.config.logging import configure_logging
from src.models import Notification
from src.service import EmailService
from src.queues import RedisNotificationsQueue
from src.redis_client import redis_client
from src.constants import NOTIFICATION_QUEUE, DEAD_NOTIFICATION_QUEUE
from src.workers.base import Worker

configure_logging()
logger = logging.getLogger(__name__)


class NotificationWorker(Worker):

    def run(self):
        logger.info("Worker запущен")
        while True:
            model = self.queue.consume()
            try:
                logger.info("Попытка отправить сообщение")
                self.service.send(model)
            except Exception as e:
                logger.warning("Возникла ошибка, возвращаем в очередь")
                self.queue.reject(model)
            else:
                logger.info("Успешно отправили")
                self.queue.ack(model)


            # try:
            #     self.service.send(model)
            # except Exception as e:
            #     self._retry_send_message(model, str(e))


if __name__ == "__main__":
    queue = RedisNotificationsQueue(redis_client, NOTIFICATION_QUEUE)
    dead_queue = RedisNotificationsQueue(redis_client, DEAD_NOTIFICATION_QUEUE)
    worker = NotificationWorker(queue, dead_queue, EmailService())
    worker.run()
