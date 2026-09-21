

def _reset_logging(cls):
    """
    Reset the logging configuration for the given class.
    """
    if hasattr(cls, 'reset_logging'):
        cls.reset_logging()
    else:
        raise NotImplementedError(f"Class {cls.__name__} does not have a 'reset_logging' method.")

# Example usage:
