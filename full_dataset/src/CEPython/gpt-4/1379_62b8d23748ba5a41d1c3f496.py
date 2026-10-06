import collections
import functools


def lfu_cache(maxsize=128, typed=False):
    def decorating_function(user_function):
        cache = LFUCache(maxsize=maxsize)

        @functools.wraps(user_function)
        def wrapper(*args, **kwargs):
            key = args
            if typed:
                key += tuple(type(v) for v in args)
                key += tuple(kwargs.items())
            try:
                return cache[key]
            except KeyError:
                value = user_function(*args, **kwargs)
                cache[key] = value
                return value

        return wrapper

    return decorating_function
