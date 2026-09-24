import time


def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    def decorator(func):
        cache = {}
        hits = {}
        misses = {}
        timer = timer
        maxsize = maxsize
        ttl = ttl
        typed = typed

        def wrapper(*args, **kwargs):
            key = (args, tuple(kwargs.items()))
            if key in cache:
                hits[key] = hits.get(key, 0) + 1
                return cache[key]
            else:
                misses[key] = misses.get(key, 0) + 1
                result = func(*args, **kwargs)
                cache[key] = result
                return result

        def get_cache_info():
            return {
                'hits': hits,
                'misses': misses,
                'cache': cache
            }

        return wrapper, get_cache_info

    return decorator
