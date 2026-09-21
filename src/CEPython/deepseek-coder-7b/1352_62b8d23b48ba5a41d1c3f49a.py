from collections import OrderedDict
from functools import wraps


def mru_cache(maxsize=128, typed=False):
    """
    Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Most Recently Used (MRU)
    algorithm.
    """
    def decorating_function(func):
        cache = TypedCache(maxsize) if typed else Cache(maxsize)

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (func, args, frozenset(kwargs.items()))
            if key not in cache:
                cache[key] = func(*args, **kwargs)
            return cache[key]

        def cache_info():
            return cache.cache_info()

        def cache_clear():
            cache.cache_clear()

        wrapper.cache_info = cache_info
        wrapper.cache_clear = cache_clear

        return wrapper

    return decorating_function
