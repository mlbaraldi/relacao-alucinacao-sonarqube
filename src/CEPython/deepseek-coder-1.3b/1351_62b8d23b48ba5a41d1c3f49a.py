

def mru_cache(maxsize=128, typed=False):
    cache = {}
    call_order = []

    def decorator(func):
        def wrapper(*args, **kwargs):
            key = (func.__name__, str(args), str(kwargs)) if typed else func.__name__
            if key in cache:
                call_order.remove(key)
                call_order.append(key)
            elif len(cache) == maxsize:
                call_order.pop(0)
                cache.pop(call_order[0])
            cache[key] = func(*args, **kwargs)
            call_order.append(key)
            return cache[key]
        return wrapper
    return decorator
