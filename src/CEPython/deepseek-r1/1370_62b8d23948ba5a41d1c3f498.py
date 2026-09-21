def lru_cache(maxsize=128, typed=False):
    from collections import OrderedDict
    """Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Least Recently Used (LRU) algorithm.
    """
    def decorator(func):
        if maxsize is not None and maxsize <= 0:
            # If maxsize is zero or negative, disable caching
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            wrapper.cache_info = lambda: "CacheInfo(hits=0, misses=0, maxsize=0, currsize=0)"
            return wrapper

        cache = OrderedDict()
        hits = 0
        misses = 0

        def make_key(args, kwargs):
            key = []
            for arg in args:
                key.append(arg)
                if typed:
                    key.append(type(arg))
            if kwargs:
                sorted_kwargs = sorted(kwargs.items())
                for k, v in sorted_kwargs:
                    key.append(k)
                    key.append(v)
                    if typed:
                        key.append(type(v))
            return tuple(key)

        def wrapper(*args, **kwargs):
            nonlocal hits, misses
            key = make_key(args, kwargs)
            if key in cache:
                hits += 1
                cache.move_to_end(key)
                return cache[key]
            else:
                misses += 1
                result = func(*args, **kwargs)
                cache[key] = result
                if maxsize is not None and len(cache) > maxsize:
                    cache.popitem(last=False)
                return result

        def cache_info():
            from collections import namedtuple
            CacheInfo = namedtuple('CacheInfo', ['hits', 'misses', 'maxsize', 'currsize'])
            return CacheInfo(hits, misses, maxsize, len(cache))

        wrapper.cache_info = cache_info
        wrapper.cache_clear = lambda: cache.clear()
        return wrapper

    return decorator
