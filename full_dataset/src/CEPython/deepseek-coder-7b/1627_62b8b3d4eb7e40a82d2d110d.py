

def _c_optimizations_required():
    """
    Return a true value if the C optimizations are required.

    This uses the ``PURE_PYTHON`` variable as documented in `_use_c_impl`.
    """
    try:
        # Assuming PURE_PYTHON is a global variable
        return not PURE_PYTHON
    except NameError:
        # If PURE_PYTHON is not defined, then C optimizations are required
        return True
