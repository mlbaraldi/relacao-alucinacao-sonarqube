import platform


def get_versions():
    """
    Get version information or return default if unable to do so.
    """
    try:
        return platform.system(), platform.release(), platform.version()
    except AttributeError:
        return "Unable to retrieve version information."
