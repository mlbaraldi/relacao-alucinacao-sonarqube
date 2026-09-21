def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    import time
    from collections import OrderedDict
    from functools import wraps
    def decorator(func):
        cache = OrderedDict()

        def make_key(args, kwargs, typed_flag):
            new_args = []
            for arg in args:
                if typed_flag:
                    new_args.append((arg, type(arg)))
                else:
                    new_args.append(arg)
            key_parts = tuple(new_args)
            if kwargs:
                sorted_kw = sorted(kwargs.items())
                new_kw = []
                for k, v in sorted_kw:
                    if typed_flag:
                        new_kw.append((k, (v, type(v))))
                    else:
                        new_kw.append((k, v))
                key_parts += tuple(new_kw)
            return key_parts

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = make_key(args, kwargs, typed)
            current_time = timer()

            if key in cache:
                result, timestamp = cache[key]
                if current_time - timestamp < ttl:
                    cache.move_to_end(key)
                    return result
                else:
                    del cache[key]

            result = func(*args, **kwargs)
            cache[key] = (result, current_time)

            if maxsize is not None and len(cache) > maxsize:
                cache.popitem(last=False)

            return result

        return wrapper
    return decorator
