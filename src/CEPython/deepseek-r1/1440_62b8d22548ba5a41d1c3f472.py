def cachedmethod(cache, key=hashkey, lock=None):
    from threading import Lock
    """
    Decorator to wrap a class or instance method with a memoizing callable that saves results in a cache.
    """
    def decorator(method):
        def wrapper(*args, **kwargs):
            instance = args[0] if args else None

            # Resolve the actual cache
            if callable(cache):
                actual_cache = cache(instance)
            elif isinstance(cache, str):
                actual_cache = getattr(instance, cache)
            else:
                actual_cache = cache

            # Resolve the lock
            actual_lock = None
            if lock is not None:
                if callable(lock):
                    actual_lock = lock(instance)
                elif isinstance(lock, str):
                    actual_lock = getattr(instance, lock)
                else:
                    actual_lock = lock

            # Compute the cache key
            cache_key = key(args, kwargs)

            # Handle the case with a lock
            if actual_lock is not None:
                with actual_lock:
                    if cache_key in actual_cache:
                        return actual_cache[cache_key]
                    result = method(*args, **kwargs)
                    actual_cache[cache_key] = result
                    return result
            else:
                if cache_key in actual_cache:
                    return actual_cache[cache_key]
                result = method(*args, **kwargs)
                actual_cache[cache_key] = result
                return result

        return wrapper
    return decorator
