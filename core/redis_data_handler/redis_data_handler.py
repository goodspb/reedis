from abc import ABC, abstractmethod

from PySide6.QtCore import QModelIndex
from redis import Redis


class RedisDataHandler(ABC):

    def __init__(self, r: Redis, window):
        self.r = r
        self.window = window

    @abstractmethod
    def update_content(self, key: str, *args, **kw):
        pass

    @abstractmethod
    def delete_content(self, key: str, current_index, current_data, *args, **kw):
        pass

    @abstractmethod
    def edit_content(self, key: str, index: QModelIndex, *args, **kw):
        pass
