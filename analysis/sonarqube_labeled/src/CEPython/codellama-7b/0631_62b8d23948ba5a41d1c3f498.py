import functools


def lru_cache(maxsize=128, typed=False):
    def decorator(func):
        cache = {}
        recent_keys = []

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            if key in cache:
                return cache[key]
            else:
                result = func(*args, **kwargs)
                cache[key] = result
                recent_keys.append(key)
                if len(recent_keys) > maxsize:
                    oldest_key = recent_keys.pop(0)
                    del cache[oldest_key]
                return result
        return wrapper
    return decorator
