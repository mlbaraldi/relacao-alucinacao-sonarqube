

def _get_err_indices(self, coord_name):
    # Get the indices of the error values corresponding to the given coordinate
    err_indices = []
    for i, coord in enumerate(self.coords):
        if coord.name == coord_name:
            err_indices.append(i)
    return err_indices
