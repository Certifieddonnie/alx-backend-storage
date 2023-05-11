#!/usr/bin/env python3
"""
Writing strings to Redis
"""
from __future__ import annotations
from typing import Union, Callable, Optional
import redis
import uuid


class Cache():
    """ A Redis Cache Class """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | bytes | int | float) -> str:
        """ Storing method """
        datakey = str(uuid.uuid4())
        self._redis.set(datakey, data)
        return datakey

    def get(self, key: str,
            fn: Optional[callable] = None) -> Union[str, bytes, int, float]:
        """ control the return value type """
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data

    def get_str(self, key: str) -> str:
        """ automatically parametrize Cache.get with the correct
        conversion function."""
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """ automatically parametrize Cache.get with the
        correct conversion function. """
        data = self._redis.get(key)
        try:
            data = int(data.decode("utf-8"))
        except Exception:
            data = 0
        return data
