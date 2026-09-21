import time
from neo4j import unit_of_work


def unit_of_work(metadata=None, timeout=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            duration = end_time - start_time
            if timeout is not None and duration > timeout:
                raise TimeoutError("Transaction timed out after {} seconds".format(timeout))
            return result
        return wrapper
    return decorator
