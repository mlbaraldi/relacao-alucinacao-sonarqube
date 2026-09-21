import time
from functools import wraps


def unit_of_work(metadata=None, timeout=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = None

            while True:
                try:
                    result = func(*args, **kwargs)
                    break
                except Exception as e:
                    if timeout is not None and time.time() - start_time > timeout:
                        raise Exception(f"Transaction timeout after {timeout} seconds")

            return result

        if metadata is not None:
            wrapper.dbms_meta_data = metadata

        return wrapper

    return decorator
