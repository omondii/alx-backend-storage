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
        
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
