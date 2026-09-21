import threading


def cachedmethod(cache, key=hashkey, lock=None):
    """
    Decorator to wrap a class or instance method with a memoizing
    callable that saves results in a cache.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            if lock is not None:
                with lock:
                    if key in cache:
                        return cache[key]
                    result = func(*args, **kwargs)
                    cache[key] = result
                    return result
            else:
                if key in cache:
                    return cache[key]
                result = func(*args, **kwargs)
                cache[key] = result
                return result
        return wrapper
    return decorator
