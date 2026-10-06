import importlib


def _c_optimizations_available():
    try:
        importlib.import_module('__main__')  # This will raise ImportError if the module does not exist
        return True
    except ImportError:
        return False
