#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

rlist = [1, 2, 3, 4, 5]
data = bytes(rlist)
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))

