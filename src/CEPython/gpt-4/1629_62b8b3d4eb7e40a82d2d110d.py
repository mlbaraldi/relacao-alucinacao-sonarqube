

def _c_optimizations_required():
    """
    Return a true value if the C optimizations are required.

    This uses the ``PURE_PYTHON`` variable as documented in `_use_c_impl`.
    """
    try:
        from os import environ
        return not bool(environ.get('PURE_PYTHON'))
    except ImportError:
        return True
