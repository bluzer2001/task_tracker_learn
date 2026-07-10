__all__ = ("BaseRepository",)

from abc import ABC, abstractmethod


class BaseRepository(ABC):

    @abstractmethod
    def add(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_all(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_by_id(self, *args, **kwargs):
        pass

    @abstractmethod
    def update(self, *args, **kwargs):
        pass
