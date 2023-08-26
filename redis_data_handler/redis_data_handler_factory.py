from redis import Redis

from redis_data_handler.hash_handler import HashHandler
from redis_data_handler.list_handler import ListHandler
from redis_data_handler.redis_data_handler import RedisDataHandler
from redis_data_handler.set_handler import SetHandler
from redis_data_handler.stream_handler import StreamHandler
from redis_data_handler.string_handler import StringHandler
from redis_data_handler.zset_handler import ZsetHandler


class RedisDataHandlerFactory:
    @staticmethod
    def get_data_handler(r: Redis, window, key_type) -> RedisDataHandler:
        if key_type == "string":
            return StringHandler(r, window)
        if key_type == "list":
            return ListHandler(r, window)
        if key_type == "hash":
            return HashHandler(r, window)
        if key_type == "set":
            return SetHandler(r, window)
        if key_type == "zset":
            return ZsetHandler(r, window)
        if key_type == "stream":
            return StreamHandler(r, window)
        raise NotImplementedError()
