def get_versions():
    """
    Get version information or return default if unable to do so.
    """
    try:
        from ._version import version
        return version
    except ImportError:
        return "0.0.0"
