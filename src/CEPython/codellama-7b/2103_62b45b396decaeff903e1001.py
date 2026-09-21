

def amend_bzparams(self, params, bug_ids):
    # Add the bug IDs to the params dictionary
    params['bug_ids'] = bug_ids
    # Add the "include_fields" parameter to the params dictionary
    params['include_fields'] = ['id', 'summary', 'status', 'priority', 'assigned_to']
    # Add the "sort_by" parameter to the params dictionary
    params['sort_by'] = 'id'
    # Add the "sort_order" parameter to the params dictionary
    params['sort_order'] = 'asc'
    # Return the amended params dictionary
    return params
