from abc import ABC, abstractmethod

class BaseQueue(ABC):

    @abstractmethod
    def publish(self, obj):
        pass

    @abstractmethod
    def consume(self):
        pass

    @abstractmethod
    def ack(self, obj):
        pass

    @abstractmethod
    def reject(self, obj):
        pass
