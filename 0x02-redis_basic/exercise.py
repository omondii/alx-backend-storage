#!/usr/bin/env python3
""" exercise.py """
import redis
import uuid
from typing import Union, Callable, Optional


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
    
    def get(self, key: str, fn: Optional[callable] = None) -> Union[str, bytes, int, float, None]:
        """ take a key string argument and an optional
        Callable argument named fn
        """
        data = self._redis.get(key)

        if data is not None and fn is not None:
            return fn(data)
        else:
            return data
        
    def get_str(self, key: str) -> Union[str, None]:
        """ Parameterize strings passed """
        return self.get(key, fn=lambda x: x.decode() if x is not None else None)
    
    def get_int(self, key: str) -> Union[str, None]:
        """ Handles parameterazing integers """
        return self.get(key, fn=lambda x: int(x) if x is not None else None)
        
