import functools


def mru_cache(maxsize=128, typed=False):
    def decorator(func):
        cache = {}
        mru = []

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, kwargs) if typed else args
            if key in cache:
                mru.remove(key)
                mru.append(key)
                return cache[key]
            else:
                result = func(*args, **kwargs)
                cache[key] = result
                mru.append(key)
                if len(mru) > maxsize:
                    cache.pop(mru.pop(0))
                return result
        return wrapper
    return decorator
