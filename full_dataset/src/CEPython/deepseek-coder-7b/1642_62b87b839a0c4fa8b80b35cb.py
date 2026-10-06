

def _get_err_indices(self, coord_name):
    """
    Get error indices corresponding to a coordinate.
    """
    # Assume self.data is a list of dictionaries, where each dictionary
    # represents a data point and has a 'coord_name' key with a coordinate value
    err_indices = [i for i, d in enumerate(self.data) if d[coord_name] == error_value]
    return err_indices
