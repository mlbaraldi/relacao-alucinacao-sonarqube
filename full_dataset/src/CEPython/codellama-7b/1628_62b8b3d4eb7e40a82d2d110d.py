

def _c_optimizations_required():
    return _use_c_impl() and not PURE_PYTHON
