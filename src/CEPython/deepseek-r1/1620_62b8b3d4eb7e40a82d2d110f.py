def _should_attempt_c_optimizations():
    import os
    import platform
    """
    Return a true value if we should attempt to use the C optimizations.

    This takes into account whether we're on PyPy and the value of the
    ``PURE_PYTHON`` environment variable, as defined in `_use_c_impl`.
    """
    if os.environ.get('PURE_PYTHON'):
        return False
    return platform.python_implementation() != 'PyPy'
