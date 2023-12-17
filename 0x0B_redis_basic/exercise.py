#!/usr/bin/env python3
"""strings to Redis"""
import redis
from typing import Union, Optional, Callable
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """decorator that takes a single method Callable
    argument and returns a Callable"""
    meth = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """decorator it is useful to use functool.wraps
        to conserve the original function’s name, docstring"""
        self._redis.incr(meth)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """decorator that takes a single method Callable
    argument and returns a Callable"""
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """decorator it is useful to use functool.wraps
        to conserve the original function’s name, docstring"""
        self._redis.incr(meth)
        self._redis.rpush(meth)
        return method(self, *args, **kwds)
    return wrapper


def replay():
    """implement a replay function to display
    the history of calls of a particular function"""
    return


class Cache():
    """Cache class"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method that takes a data argument and returns a string
        generate a random key (e.g. using uuid) store the input data in
        Redis using the random key and return the key"""
        uuid1 = str(uuid.uuid1())
        self._redis.set(uuid1, data)
        return uuid1

    def get(self, key: str, fn: Optional[Callable] = None) -> str:
        """create a get method that take a key string argument and
        an optional Callable argument named fn. This callable will
        be used to convert the data back to the desired format"""
        value = self._redis.get(key)
        return value

    def get_str(self) -> str:
        """get_str"""
        return

    def get_int(self) -> int:
        """get_int"""
        return
