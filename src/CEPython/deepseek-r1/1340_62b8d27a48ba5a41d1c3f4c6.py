def cached(cache, key=hashkey, lock=None):
    """
    Decorator to wrap a function with a memoizing callable that saves
    results in a cache.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            cache_key = key(*args, **kwargs)
            # First check if the result is already cached
            if lock is not None:
                with lock:
                    if cache_key in cache:
                        return cache[cache_key]
            else:
                if cache_key in cache:
                    return cache[cache_key]
            # Compute the result if not found in cache
            result = func(*args, **kwargs)
            # Double-check the cache before updating to handle concurrent updates
            if lock is not None:
                with lock:
                    if cache_key in cache:
                        # Another thread might have added the entry while we were computing
                        return cache[cache_key]
                    cache[cache_key] = result
            else:
                if cache_key in cache:
                    return cache[cache_key]
                cache[cache_key] = result
            return result
        return wrapper
    return decorator
