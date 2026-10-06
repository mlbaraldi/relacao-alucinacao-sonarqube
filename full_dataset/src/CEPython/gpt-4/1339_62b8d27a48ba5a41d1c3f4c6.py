import threading
from collections import defaultdict


def cached(cache, key=hashkey, lock=None):
    if cache is None:
        cache = defaultdict(lambda: None)
    if lock is None:
        lock = threading.Lock()

    def decorator(func):
        def wrapper(*args, **kwargs):
            cache_key = key(args, kwargs)
            with lock:
                if cache_key not in cache:
                    cache[cache_key] = func(*args, **kwargs)
                return cache[cache_key]
        return wrapper
    return decorator
