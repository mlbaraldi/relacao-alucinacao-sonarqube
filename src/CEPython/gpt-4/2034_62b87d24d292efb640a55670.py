import sys


def get_versions():
    """
    Get version information or return default if unable to do so.
    """
    try:
        version_info = sys.version_info
        return f"Python version: {version_info.major}.{version_info.minor}.{version_info.micro}"
    except Exception:
        return "Default version: 0.0.0"
