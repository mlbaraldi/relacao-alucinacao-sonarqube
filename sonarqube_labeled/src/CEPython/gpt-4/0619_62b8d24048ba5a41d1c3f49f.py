import time
import heapq
import functools


def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    def decorator(func):
        if maxsize == 0:
            return func
        cache = {}
        queue = []
        refcount = 0

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal refcount
            key = args if not typed else (args, frozenset(kwargs.items()))
            now = timer()
            if key in cache:
                expiry, _, result = cache[key]
                if now < expiry:
                    return result
            result = func(*args, **kwargs)
            if len(cache) >= maxsize:
                while queue:
                    _, ref, old_key = heapq.heappop(queue)
                    if ref != refcount:
                        continue
                    del cache[old_key]
                    break
            cache[key] = now + ttl, refcount, result
            heapq.heappush(queue, (now + ttl, refcount, key))
            refcount += 1
            return result
        return wrapper
    return decorator
