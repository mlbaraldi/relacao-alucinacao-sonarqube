

def deprecated(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{func.__name__} is deprecated: {message}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
