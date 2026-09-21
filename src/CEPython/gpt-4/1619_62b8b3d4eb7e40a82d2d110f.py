import os
import platform


def _should_attempt_c_optimizations():
    """
    Return a true value if we should attempt to use the C optimizations.

    This takes into account whether we're on PyPy and the value of the
    ``PURE_PYTHON`` environment variable, as defined in `_use_c_impl`.
    """
    # Check if we're on PyPy
    is_pypy = platform.python_implementation() == 'PyPy'

    # Check the value of the PURE_PYTHON environment variable
    pure_python = os.getenv('PURE_PYTHON', '0')

    # We should attempt to use the C optimizations if we're not on PyPy and
    # the PURE_PYTHON environment variable is not set to '1'
    return not is_pypy and pure_python != '1'
