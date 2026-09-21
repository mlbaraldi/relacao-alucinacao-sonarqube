import platform
import sys


def get_versions():
    """
    Get version information or return default if unable to do so.
    """
    try:
        python_version = sys.version
        system_info = platform.uname()
        return {
            'python_version': python_version,
            'system_info': system_info
        }
    except Exception as e:
        return {'error': str(e)}
