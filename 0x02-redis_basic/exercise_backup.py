#!/usr/bin/env python3
"""
Contains a class that instatiates a Redis Cache
"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """Represents a Redis DB object"""

    def __init__(self) -> None:
        """Instantiates a Redis DB object"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, int, bytes, float]) -> str:
        """Takes args data sets in redisdb with a unique
        uuid and returns a string 'key' of the uuid"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]):
        """Power fantasy"""
        obj = self._redis.get(key)
        if obj:
            return fn(obj)
        return None
    
    def get_str(self):
        pass
    
    def get_int(self):
        pass