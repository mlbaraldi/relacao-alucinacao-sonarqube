def _update_context(self, context):
    """
    Update *context* with the properties of this graph.

    *context.error* is appended with indices of errors.
    Example subcontext for a graph with fields "E,t,error_E_low":
    {"error": {"x_low": {"index": 2}}}.
    Note that error names are called "x", "y" and "z"
    (this corresponds to first three coordinates,
    if they are present), which allows to simplify plotting.
    Existing values are not removed
    from *context.value* and its subcontexts.

    Called on "destruction" of the graph (for example,
    in :class:`.ToCSV`). By destruction we mean conversion
    to another structure (like text) in the flow.
    The graph object is not really destroyed in this process.
    """
    non_error_fields = [f for f in self.fields if not f.startswith('error_')]
    for index, field in enumerate(self.fields):
        if field.startswith('error_'):
            parts = field.split('_')[1:]
            if len(parts) < 2:
                continue  # Not enough parts to form a valid error field
            coordinate_part, error_type = parts[0], '_'.join(parts[1:])
            try:
                coord_index = non_error_fields.index(coordinate_part)
            except ValueError:
                continue  # Coordinate part not found in non-error fields
            if coord_index >= 3:
                continue  # Only x, y, z (first three coordinates)
            coord_name = ['x', 'y', 'z'][coord_index]
            error_name = f"{coord_name}_{error_type}"
            if 'error' not in context:
                context['error'] = {}
            context['error'][error_name] = {'index': index}
