from abc import ABC, abstractmethod

from models import Notification


class Serializer(ABC):

    @staticmethod
    @abstractmethod
    def serialize(*args, **kwargs) -> str:
        pass

    @staticmethod
    @abstractmethod
    def deserialize(*args, **kwargs):
        pass