

def on(self, hook):
    """
    Decorator function to add a new handler to the registry.

    Args:
        hook (HookType): Hook attribute for which to register the handler.

    Returns:
        callable: Decorator for registering listeners for the specified
        hook.
    """
    def decorator(func):
        # Here you can add the logic to register the function as a handler for the specified hook
        # For example, you can add the function to a list of handlers for the specified hook
        # This is just a placeholder, you should replace it with your actual logic
        print(f"Registering handler {func.__name__} for hook {hook}")

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Call the original function with any arguments it may need
            return func(*args, **kwargs)

        return wrapper

    return decorator
