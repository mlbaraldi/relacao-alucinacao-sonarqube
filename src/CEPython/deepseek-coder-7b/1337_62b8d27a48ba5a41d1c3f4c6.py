import functools
import inspect


def cached(cache, key=hashkey, lock=None):
    """
    Decorator to wrap a function with a memoizing callable that saves
    results in a cache.
    """
    if key is None:
        def hashkey(func, *args, **kwargs):
            return (func.__name__, args, frozenset(kwargs.items()))
        key = hashkey

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func_key = key(func, *args, **kwargs)
            if func_key in cache:
                return cache[func_key]
            if lock:
                with lock:
                    if func_key not in cache:
                        result = func(*args, **kwargs)
                        cache[func_key] = result
                        return result
            else:
                result = func(*args, **kwargs)
                cache[func_key] = result
                return result
        return wrapper
    return decorator
