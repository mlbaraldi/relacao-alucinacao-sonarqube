import os
import platform


def _should_attempt_c_optimizations():
    """
    Return a true value if we should attempt to use the C optimizations.

    This takes into account whether we're on PyPy and the value of the
    ``PURE_PYTHON`` environment variable, as defined in `_use_c_impl`.
    """
    # Check if we're on PyPy
    if platform.python_implementation() == 'PyPy':
        return True

    # Check if the PURE_PYTHON environment variable is set to a true value
    pure_python = os.getenv('PURE_PYTHON')
    if pure_python:
        return pure_python.lower() not in ['true', '1', 'yes']

    # If neither condition is met, return False
    return False
