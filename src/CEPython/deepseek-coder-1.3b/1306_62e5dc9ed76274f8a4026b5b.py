import warnings
import functools


def deprecated(message):
    """
    Decorator for deprecating functions and methods.

    Usage:

    @deprecated("'foo' has been deprecated in favour of 'bar'")
    def foo(x):
        pass
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            message = message.format(func.__name__, "'" + func.__doc__ + "'")
            warnings.warn(message, category=DeprecationWarning, stacklevel=2)
            return func(*args, **kwargs)
        return wrapper
    return decorator
