def _c_optimizations_available():
    import os
    """
    Return the C optimization module, if available, otherwise
    a false value.

    If the optimizations are required but not available, this
    raises the ImportError.

    This does not say whether they should be used or not.
    """
    try:
        import _c_optimizations
        return _c_optimizations
    except ImportError as e:
        if os.environ.get('REQUIRE_C_OPTIMIZATIONS') == '1':
            raise ImportError("C optimizations required but not available.") from e
        return False
