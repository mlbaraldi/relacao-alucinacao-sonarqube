def integral(bins, edges):
    import numpy as np
    """
    Compute the integral of a histogram by summing each bin's value multiplied by its corresponding volume.

    Parameters:
    bins (numpy.ndarray): The values of the histogram bins.
    edges (list of numpy.ndarray): The edges defining the bins for each dimension.

    Returns:
    float: The computed integral of the histogram.
    """
    # Calculate the widths for each dimension's edges
    widths = [np.diff(edge) for edge in edges]
    
    # Initialize the volumes array with ones of the same shape as bins
    volumes = np.ones(bins.shape, dtype=np.float64)
    
    # Iterate over each dimension to compute the product of widths
    for i, w in enumerate(widths):
        # Determine the new shape for broadcasting
        shape = list(volumes.shape)
        for j in range(len(shape)):
            if j != i:
                shape[j] = 1
        shape[i] = -1  # Set current dimension to the size of the width array
        
        # Reshape the width array and multiply into volumes
        w_reshaped = w.reshape(shape)
        volumes *= w_reshaped
    
    # Calculate the integral by summing the product of bins and volumes
    return np.sum(bins * volumes)
