

def _get_err_indices(self, coord_name):
    """
    Get error indices corresponding to a coordinate.
    """
    if coord_name in self.errors:
        return self.errors[coord_name]
    else:
        return []
