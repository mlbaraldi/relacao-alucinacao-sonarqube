import threading


def cached(cache, key=hashkey, lock=None):
    """
    Decorator to wrap a function with a memoizing callable that saves
    results in a cache.
    """
    if lock is None:
        lock = threading.Lock()

    def decorator(func):
        def wrapper(*args, **kwargs):
            with lock:
                if key is not None:
                    k = key(*args, **kwargs)
                    if k not in cache:
                        cache[k] = func(*args, **kwargs)
                else:
                    if func not in cache:
                        cache[func] = func(*args, **kwargs)
            return cache[func]
        return wrapper
    return decorator
