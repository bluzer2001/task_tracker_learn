import logging
from redis import Redis

from src.serialisiers import NotificationSerializer, AnalyticMessageSerializer
from .base import BaseQueue

logger = logging.getLogger(__name__)


class RedisQueue(BaseQueue):
    serializer_class = None

    def __init__(self, client: Redis, queue_name: str):
        self.client = client
        self.queue_name = queue_name
        self.processing_queue_name = queue_name + ":processing"

    def publish(self, object_to_send):
        logger.debug(
            "Сериализуем объект id=%s для очереди %s",
            object_to_send.id_,
            self.queue_name
        )
        serialised_object = self.serializer_class.serialize(object_to_send)
        self.client.lpush(self.queue_name, serialised_object)
        logger.info("Сообщение отправлено в очередь сериализованный объект id=%s", object_to_send.id_)

    def consume(self):
        data = self.client.brpoplpush(self.queue_name, self.processing_queue_name)
        logger.debug("Получили данные из очереди %s", self.queue_name)
        deserialized_object = self.serializer_class.deserialize(data)
        logger.info("Получили объект %s из очереди %s", deserialized_object.id_, self.queue_name)
        return deserialized_object

    def ack(self, object_to_ack):
        self._remove_from_processing_queue(object_to_ack)

    def reject(self, object_to_reject):
        serialised_object = self._remove_from_processing_queue(object_to_reject)
        self.client.lpush(self.queue_name, serialised_object)

    def _remove_from_processing_queue(self, object_to_remove):
        serialised_object = self.serializer_class.serialize(object_to_remove)
        self.client.lrem(self.processing_queue_name, 1, serialised_object)
        return serialised_object


class RedisNotificationsQueue(RedisQueue):
    serializer_class = NotificationSerializer


class RedisAnalyticsQueue(RedisQueue):
    serializer_class = AnalyticMessageSerializer