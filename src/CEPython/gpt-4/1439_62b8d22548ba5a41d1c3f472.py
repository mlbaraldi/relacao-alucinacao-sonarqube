import functools
import threading


def cachedmethod(cache, key=hashkey, lock=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            cache_key = key(*args, **kwargs)
            # If the result is in the cache, return it
            if cache_key in cache:
                return cache[cache_key]
            # Otherwise, compute the result and add it to the cache
            else:
                if lock:
                    with lock:
                        # Double-checking locking pattern to prevent
                        # unnecessary computation in case of race condition
                        if cache_key in cache:
                            return cache[cache_key]
                        else:
                            result = func(*args, **kwargs)
                            cache[cache_key] = result
                            return result
                else:
                    result = func(*args, **kwargs)
                    cache[cache_key] = result
                    return result
        return wrapper
    return decorator
