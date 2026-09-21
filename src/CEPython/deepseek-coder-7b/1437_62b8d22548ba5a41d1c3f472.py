from functools import lru_cache


def cachedmethod(cache, key=hashkey, lock=None):
    """
    Decorator to wrap a class or instance method with a memoizing callable
    that saves results in a cache.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        wrapper = lru_cache(maxsize=maxsize, typed=typed)(wrapper)
        return wrapper
    return decorator
