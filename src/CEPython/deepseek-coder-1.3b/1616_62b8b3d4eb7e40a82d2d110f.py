import os


def _should_attempt_c_optimizations():
    """
    Return a true value if we should attempt to use the C optimizations.

    This takes into account whether we're on PyPy and the value of the
    ``PURE_PYTHON`` environment variable, as defined in `_use_c_impl`.
    """
    return os.getenv('PURE_PYTHON') == 'True' and 'PyPy' in os.environ.get('PYTHON_VERSION', '')
