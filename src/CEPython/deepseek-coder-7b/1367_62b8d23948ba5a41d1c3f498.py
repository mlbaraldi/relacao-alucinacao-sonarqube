from collections import OrderedDict


def lru_cache(maxsize=128, typed=False):
    """
    Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Least Recently Used (LRU)
    algorithm.
    """
    def decorator(func):
        cache = OrderedDict()

        def wrapper(*args, **kwargs):
            # If typed is True, treat different types of arguments as different keys
            if typed:
                key = (func, args, tuple(kwargs.items()))
            else:
                key = (func, args)

            if key in cache:
                # Move the key to the end of the OrderedDict to mark it as recently used
                cache.move_to_end(key)
                return cache[key]
            else:
                if len(cache) >= maxsize:
                    # Remove the least recently used item
                    cache.popitem(last=False)
                result = func(*args, **kwargs)
                cache[key] = result
                return result
        return wrapper
    return decorator
