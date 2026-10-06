import ctypes


def _c_optimizations_available():
    """
    Return the C optimization module, if available, otherwise
    a false value.

    If the optimizations are required but not available, this
    raises the ImportError.

    This does not say whether they should be used or not.
    """
    try:
        # replace 'my_module' with the name of your C extension module
        return ctypes.CDLL('my_module')
    except OSError:
        raise ImportError("C optimizations are required but not available")
