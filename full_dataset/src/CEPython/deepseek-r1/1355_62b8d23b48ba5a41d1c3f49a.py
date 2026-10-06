def mru_cache(maxsize=128, typed=False):
    from collections import OrderedDict
    """Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Most Recently Used (MRU) algorithm.
    """
    def decorator(func):
        cache = OrderedDict()

        def wrapper(*args, **kwargs):
            if maxsize <= 0:
                return func(*args, **kwargs)

            # Generate the key based on args, kwargs, and typed
            key = args
            if kwargs:
                sorted_kwargs = tuple(sorted(kwargs.items()))
                key += sorted_kwargs
            if typed:
                type_part = tuple(type(arg) for arg in args)
                if kwargs:
                    type_part += tuple(type(value) for _, value in sorted_kwargs)
                key += type_part

            # Check cache hit
            if key in cache:
                cache.move_to_end(key)
                return cache[key]
            else:
                # Compute result if not in cache
                result = func(*args, **kwargs)
                # Apply MRU eviction if necessary
                if len(cache) >= maxsize:
                    cache.popitem(last=True)
                cache[key] = result
                return result

        # Preserve the original function's attributes
        wrapper.__module__ = func.__module__
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        wrapper.__annotations__ = func.__annotations__

        return wrapper
    return decorator
