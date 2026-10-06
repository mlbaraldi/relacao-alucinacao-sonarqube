def lfu_cache(maxsize=128, typed=False):
    import collections
    from functools import wraps
    def decorator(func):
        cache = LFUCache(maxsize, typed)
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = make_key(args, kwargs, typed)
            result = cache.get(key)
            if result is not cache._missing:
                return result
            result = func(*args, **kwargs)
            cache.put(key, result)
            return result
        return wrapper
    return decorator
