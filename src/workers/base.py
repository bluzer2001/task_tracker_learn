from abc import ABC, abstractmethod

from src.queues import RedisNotificationsQueue
from src.models import Retriable


class Worker(ABC):

    def __init__(self, queue: RedisNotificationsQueue, dead_queue: RedisNotificationsQueue, service):
        self.queue = queue
        self.dead_queue = dead_queue
        self.service = service

    @abstractmethod
    def run(self):
        pass

    def _retry_send_message(self, model: Retriable, error: str):
            if model.retries < 3:
                self._give_message_another_try(model)
            else:
                self._send_message_to_dead_queue(model, error)

    def _give_message_another_try(self, model: Retriable):
        model.retries += 1
        self.queue.publish(model)
        print(
            f"Не удалось отправить сообщение, отправляем обратно в очередь"
        )

    def _send_message_to_dead_queue(self, model: Retriable, error: str):
        print(f"Ошибка, отмена отправки уведомления ")
        model.error = error
        self.dead_queue.publish(model)