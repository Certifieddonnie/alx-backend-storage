#!/usr/bin/env python3
"""
Writing strings to Redis
"""
from __future__ import annotations
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
