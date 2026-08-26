from abc import ABC, abstractmethod
from src.models import Notification

class NotificationsQueue(ABC):

    @abstractmethod
    def publish(self, notification: Notification):
        pass

    @abstractmethod
    def consume(self) -> Notification | None:
        pass
