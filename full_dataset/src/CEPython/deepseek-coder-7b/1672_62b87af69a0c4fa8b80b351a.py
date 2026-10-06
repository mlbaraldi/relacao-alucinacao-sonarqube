

def is_fill_compute_el(obj):
    if hasattr(obj, 'fill') and hasattr(obj, 'compute'):
        return True
    return False


# Test
