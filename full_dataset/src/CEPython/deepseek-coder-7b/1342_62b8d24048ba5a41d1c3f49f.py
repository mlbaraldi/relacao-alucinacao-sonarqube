import functools
import time
from collections import OrderedDict


def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    def decorator(func):
        cache = dict()
        def wrapper(*args, **kwargs):
            key = (args, tuple(kwargs.items()))
            if typed:
                key += (type(args), tuple(type(x) for x in kwargs.values()),)
            if key in cache:
                result, timestamp = cache[key]
                if timer() - timestamp < ttl:
                    return result
            result = func(*args, **kwargs)
            cache[key] = (result, timer())
            if len(cache) > maxsize:
                cache.popitem(last=False)
            return result
        return wrapper
    return decorator
