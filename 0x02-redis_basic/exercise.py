#!/usr/bin/env python3
""" exercise.py """
import redis
import uuid
from typing import Union


class Cache():
    """ Class cache:
        private variable named _redis
    """
    def __init__(self):
        """ initialize a redis instance client """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes,int,float]) -> str:
        """ store method that takes a data argument and returns a string """
        key = str(uuid.uuid4())
        # store the input data in redis using the key
        self._redis.set(key, data)
        return key

        
