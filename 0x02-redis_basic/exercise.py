#!/usr/bin/env python3
"""
Contains a class that instatiates a Redis Cache
"""
import redis
import uuid
from typing import Union


class Cache():
    """Instantiates a Redis DB object"""

    def __init__(self):
        self.__redis = redis.Redis()

        if self.__redis:
            self.__redis.flushdb()

    def store(self, data: Union[str, int, bytes, float]) -> str:
        """Takes args data sets in redisdb with a unique
        uuid and returns a string 'key' of the uuid"""
        key = str(uuid.uuid4())
        self.__redis.set(key, data)
        return key
