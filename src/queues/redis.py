from redis import Redis

from src.config.redis import REDIS_HOST, REDIS_PORT
from src.models import Notification
from src.serialisiers import NotificationSerializer
from .base import NotificationsQueue


class RedisNotificationsQueue(NotificationsQueue):

    def __init__(self, client: Redis, queue_name: str):
        self.client = client
        self.queue_name = queue_name

    def publish(self, notification: Notification):
        print("2.1 сериализуем задачу")
        serialised_notification = NotificationSerializer.serialize(notification)
        print(f"2.2 сериализовали задачу {serialised_notification}")
        self.client.lpush(self.queue_name, serialised_notification)
        print(f"2.3 опубликовали задачу в очередь {self.queue_name}")

    def consume(self) -> Notification:
        data = self.client.brpop(self.queue_name)[1]
        notification = NotificationSerializer.deserialize(data)
        return notification
