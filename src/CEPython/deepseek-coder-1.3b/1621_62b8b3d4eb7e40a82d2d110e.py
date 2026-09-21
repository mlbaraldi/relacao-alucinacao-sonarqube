import os


def _c_optimizations_ignored():
    """
    The opposite of `_c_optimizations_required`.
    """
    return 'C_OPTIMIZATIONS_IGNORED' not in os.environ
