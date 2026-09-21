from collections import OrderedDict
from typing import Callable


def mru_cache(maxsize=128, typed=False):
    def decorating_function(user_function):
        cache = OrderedDict()

        def wrapper(*args, **kwargs):
            key = args
            if typed:
                key += tuple(sorted(kwargs.items()))
            else:
                key += tuple(kwargs.items())
            if key in cache:
                cache.move_to_end(key, last=False)
            else:
                if len(cache) >= maxsize:
                    cache.popitem(last=False)
                cache[key] = user_function(*args, **kwargs)
            return cache[key]

        return wrapper

    return decorating_function
